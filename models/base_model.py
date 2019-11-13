from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from entropies.base_entropy import BaseEntropy

class BaseAntModel(Model):
    def __init__(self, num_ants, density_of_particels, step_size, jumping_distance):
        self.step_size = step_size
        self.jumping_distance = jumping_distance
        self.num_ants = num_ants
        self.schedule = RandomActivation(self)
        self.grid_size = 50
        self.density_of_particels = density_of_particels
        self.grid = MultiGrid(self.grid_size, self.grid_size, True)
        self.running = True

        self.ant_entropy = None
        self.particle_entropy = None

        self.init_agents()
        self.init_particels()

        self.ant_agents = []
        self.particle_agents = []

        self.data_collection = DataCollector(model_reporters={"agent_count":
                                    lambda m: m.schedule.get_agent_count()})

        self.datacollector = DataCollector({
            "emergence": lambda m: BaseEntropy.entropy_x(m.ant_agents, m.grid.width)
        })

        pass

    def compute_entropy(self):
        pass

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

        pass

    # returns list of all particels an agent can see
    def particels_in_view (self, agent):
        pass

    def step_in_ran_dir (self, agent):
        pass

    def jump_in_rand_dir (self, agent):
        pass

    def pick_particel (self, agent, particel):
        pass

    def drop_particel (self, agent):
        pass

    def init_particels (self):
        pass

    def init_agents (self):
        pass

    def system_entropy(self):
        pass