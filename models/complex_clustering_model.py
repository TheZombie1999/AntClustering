import random
from agents.typed_particle_agent import TypedParticelAgent
from models.simpel_clustering_model import SimpleClusteringModel

from entropies.particle_entropy import ParticleEntropy

class ComplexClusteringModel(SimpleClusteringModel):

    def __init__(self,mid ,num_ants, density_of_particels, step_size, jumping_distance, perceptionRadius, particleThreshhold , kPlus, kMinus):
        super().__init__(mid, num_ants, density_of_particels, step_size, jumping_distance)


        self.perceptionRadius = perceptionRadius
        self.particleThreshhold = particleThreshhold
        self.kPlus = kPlus
        self.kMinus = kMinus

        pass

    def particles_in_radius(self, agent, radius):
        view = []
        x = self.grid.get_neighbors(agent.pos, include_center=True, radius=radius, moore=True)
        for i in x:
            if type(i) is TypedParticelAgent:
                view.append(i)
        return view

    def f_i(self, agent):
        if agent.particel == None:
            return 0
        perceptedFields = pow(2 * self.perceptionRadius + 1, 2)
        particleNeighbors = self.particles_in_radius(agent, self.perceptionRadius)
        neighborCount = len(particleNeighbors)
        similarity = 0
        for x in range(neighborCount):
            averageSimilarity =  0 if  (agent.particel.particleType - particleNeighbors[x].particleType) != 0 else 1
            similarity += averageSimilarity
        similarity *= 1/perceptedFields
        return similarity

    def pickProbability(self, agent):
        return pow(self.kPlus / (self.kPlus + self.f_i(agent)), 2)

    def dropProbability(self, agent):
        comparison = self.f_i(agent)
        return pow(comparison / (self.kMinus + comparison), 2)

    def drop_particel(self, agent):
        probability = self.dropProbability(agent)
        print("Drop probability: " + str(probability))

        if random.uniform(0, 1) <= probability:
            super().drop_particel(agent)
        pass

    def pick_particel(self, agent, view):
        probability = self.pickProbability(agent)
        print("Pick probability: " + str(probability))
        if random.uniform(0, 1) <= probability:
            super().pick_particel(agent, view)
        pass

    def init_particels(self):
        particles = []

        for x in range(self.grid_size):
            for y in range(self.grid_size):

                if random.randrange(0, 100, step = 1) < self.density_of_particels:
                    p = TypedParticelAgent(model= self, unique_id= x,pos =(x, y), particleType=random.randint(a = 0, b = 2))
                    particles.append(p)
                    self.grid.place_agent(p, (x, y))
        self.particle_entropy = ParticleEntropy(self.grid, particles)

    def particels_in_view(self, agent):
        view = []

        x = self.grid.get_neighbors(agent.pos, include_center=True, radius=agent.site, moore=True)

        for i in x:
            if type(i) is TypedParticelAgent:
                view.append(i)
        return view

