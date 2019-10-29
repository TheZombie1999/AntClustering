from mesa import Agent
from agents.particel_agent import ParticelAgent

class TypedParticelAgent (ParticelAgent):

    def __init__(self, unique_id, model, pos, particleType):
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.pos = pos
        self.particleType = particleType

    def __step__(self):
        pass