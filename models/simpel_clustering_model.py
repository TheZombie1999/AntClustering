import random
from models.base_model import BaseAntModel
from agents.AntAgent import AntAgent
from agents.ParticelAgent import ParticelAgent


class SimpleClusteringModel(BaseAntModel):

    def __init__(self, num_ants=10, density_of_particels=10, step_size=10, jumping_distance=10):
        super().__init__(num_ants, density_of_particels, step_size, jumping_distance)
        self.grid = super().grid

    # returns list of all particels an agent can see
    def particels_in_view(self, agent):
        view = []
        x = super().grid.get_neighbors(agent.pos, include_center=True, radius=agent.site)
        for i in x:
            if type(x) is ParticelAgent:
                view.append(i)
        return view

    def step_in_ran_dir(self, agent):
        pass

    def jump_in_rand_dir(self, agent):
        pass

    def pick_particel(self, agent, particel):
        pass

    def drop_particel(self, agent):
        pass

    def init_particels(self):
        for x in range(super().grid_size):
            for y in range(super().grid_size):

                if random.randrange(100) < super().density_of_particels:
                    p = ParticelAgent(model= super(), unique_id= x)
                    super().grid.place_agent(p, (x, y))
        pass

    def init_agents(self):
        for i in range(super().num_ants):

            super().schedule.add(a)

            x = super().random.randrange(super().grid.width)
            y = super().random.randrange(super().grid.height)
            a = AntAgent(i, super(), startpos=(x,y))
            super().grid.place_agent(a,(x,y))

