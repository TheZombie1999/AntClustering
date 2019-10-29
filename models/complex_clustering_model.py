import random
from models.base_model import BaseAntModel
from agents.AntAgent import AntAgent
from agents.typed_particle_agent import TypedParticelAgent
from models.simpel_clustering_model import SimpleClusteringModel

perceptionRadius = 2
particleThreshhold = 10 

kPlus = 0.5
kMinus = 1.5

class ComplexClusteringModel(SimpleClusteringModel):
    def particles_in_radius(self, agent, radius):
        view = []
        x = self.grid.get_neighbors(agent.pos, include_center=True, radius=radius, moore=True)
        for i in x:
            if type(x) is TypedParticelAgent:
                view.append(i)
        return view

    def compare(self, agent):
        perceptedFields = pow(perceptionRadius + 1, 2)
        particleNeighbors = self.particles_in_radius(agent, perceptionRadius)
        neighborCount = len(particleNeighbors)

        similarity = 0
        for x in range(1, neighborCount + 1):
            similarity += 1 - (abs(agent.particle.particleType - particleNeighbors[x].particleType) / particleThreshhold)
        similarity *= 1/perceptedFields
        return similarity

    def pickProbability(self, agent):
        return pow(kPlus / (kPlus + self.compare(agent)), 2)

    def dropProbability(self, agent):
        comparison = self.compare(agent)
        return pow(comparison / (kMinus + comparison), 2)

    def drop_particel(self, agent):
        probability = self.dropProbability(agent)
        if random.uniform(0, 1) >= probability:
            super().drop_particel(agent)
        pass

    def pick_particel(self, agent):
        probability = self.pickProbability(agent)
        if random.uniform(0, 1) >= probability:
            super().pick_particel(agent)
        pass

    def init_particels(self):
        for x in range(self.grid_size):
            for y in range(self.grid_size):

                if random.randrange(0, 100, step = 1) < self.density_of_particels:
                    p = TypedParticelAgent(model= self, unique_id= x,pos =(x, y), random.randint(1, particleThreshhold))
                    self.grid.place_agent(p, (x, y))
        pass