import random
from models.base_model import BaseAntModel
from agents.ant_agent import AntAgent
from agents.particel_agent import ParticelAgent
from util.util import Util


class SimpleClusteringModel(BaseAntModel):

    def __init__(self, mid, num_ants=10, density_of_particels=1, step_size=10, jumping_distance=10):
        self.middel = mid
        super().__init__(num_ants, density_of_particels, step_size, jumping_distance)
        pass


    # returns list of all particels an agent can see
    def particels_in_view(self, agent):
        view = []

        x = self.grid.get_neighbors(agent.pos, include_center=True, radius=agent.site, moore=True)

        for i in x:
            if type(i) is ParticelAgent:
                view.append(i)
        return view

    def step_in_ran_dir(self, agent):

        newPos = random.choice(self.grid.get_neighborhood(agent.pos,moore=True,include_center=False,radius=self.step_size))
        self.grid.move_agent(agent,newPos)
        agent.pos = newPos
        pass

    def jump_in_rand_dir(self, agent):
        newPos = random.choice(self.grid.get_neighborhood(agent.pos,moore=True,include_center=False,radius=self.jumping_distance))
        self.grid.move_agent(agent,newPos)
        agent.pos = newPos
        pass

    def pick_particel(self, agent, view):
        p = random.choice(view)
        agent.particel = p
        self.grid.remove_agent(p)
        pass

    def drop_particel(self, agent):

        x = self.grid.get_neighborhood(agent.pos, True, False, 1)
        loc = random.choice(x)
        self.grid.place_agent(agent.particel, loc)
        agent.particel = None
        pass

    def init_particels(self):
        for x in range(self.grid_size):
            for y in range(self.grid_size):

                if random.randrange(0, 100, step = 1) < self.density_of_particels:
                    p = ParticelAgent(model= self, unique_id= x,pos =(x, y))
                    self.grid.place_agent(p, (x, y))
        pass

    def init_agents(self):
        if self.middel:
            for i in range(self.num_ants):
                pos = (round(self.grid.width/2), round(self.grid.height/2))
                a = AntAgent(i,self,startpos=pos,site=1)
                self.schedule.add(a)
                self.grid.place_agent(a,pos)
        else:
            for i in range(self.num_ants):
                x = self.random.randrange(0,self.grid.width)
                y = self.random.randrange(0,self.grid.height)
                a = AntAgent(i, self, startpos=(x,y), site= 1)
                self.schedule.add(a)
                self.grid.place_agent(a,(x,y))

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
    pass