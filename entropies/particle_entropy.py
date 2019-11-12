from entropies.base_entropy import BaseEntropy
from agents.typed_particle_agent import TypedParticelAgent

class ParticleEntropy(BaseEntropy):
    def __init__(self, grid, particles):
        super().__init__(grid, particles)
        pass

    def same_outer_parrticles(self, agent):
        siblings = 0
        x = self.grid.get_neighbors(agent.pos, include_center=False, radius=1, moore=True)
        for i in x:
            if type(i) is TypedParticelAgent and i.particleType == agent.particleType:
                ++siblings
        return siblings

    def behavioural_entropy_ratio(self, agent):
        neighbours = self.outer_parrticles(agent)
        return self.same_outer_parrticles(agent) / 9

    def get_entropy(self):
        pass