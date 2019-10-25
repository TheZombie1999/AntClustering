import random
from models.base_model import BaseAntModel
from agents.AntAgent import AntAgent
from agents.ParticelAgent import ParticelAgent


class SimpleClusteringModel(BaseAntModel):

    def __init__(self, num_ants=10, density_of_particels=10, step_size=10, jumping_distance=10):
        super().__init__(num_ants, density_of_particels, step_size, jumping_distance)


    # returns list of all particels an agent can see
    def particels_in_view(self, agent):
        view = []
        x = self.grid.get_neighbors(agent.pos, include_center=True, radius=agent.site, moore=True)
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
        for x in range(self.grid_size):
            for y in range(self.grid_size):

                if random.randrange(100) < self.density_of_particels:
                    p = ParticelAgent(model= self, unique_id= x)
                    self.grid.place_agent(p, (x, y))
        pass

    def init_agents(self):

        for i in range(self.num_ants):
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            a = AntAgent(i, self, startpos=(x,y), site= 10)
            self.schedule.add(a)
            self.grid.place_agent(a,(x,y))

