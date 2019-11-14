from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from entropies.abstract_entropies import AbstractEntropies
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

        self.ant_agents = []
        self.particle_agents = []
        
        self.init_agents()
        self.init_particels()

        self.datacollector = DataCollector({
            # "entropy_x_ants": lambda m: BaseEntropy.entropy_x(m.ant_agents, m.grid.width)
            "entropy_x_ants": lambda m: self.emergence_ants_x()
        })
        self.datacollector2 = DataCollector({
            "entropy_y_ants": lambda m: self.emergence_ants_y()
        })
        self.datacollector3 = DataCollector({
            "entropy_special_ants": lambda m: self.emergence_ants_special()
        })

        self.datacollector4 = DataCollector({
            "entropy_x_part": lambda n: self.emergence_particle_x()
        })
        self.datacollector5 = DataCollector({
            "entropy_y_part": lambda n: self.emergence_particle_y()
        })
        self.datacollector6 = DataCollector({
            "entropy_special_part": lambda n: self.emergence_particle_special()
        })

        # Abstract Entropy
        self.datacollector7 = DataCollector({
            # "entropy_x_ants": lambda m: BaseEntropy.entropy_x(m.ant_agents, m.grid.width)
            "entropy_x_ants2": lambda m: self.emergence_ants_x2()
        })
        self.datacollector8 = DataCollector({
            "entropy_y_ants2": lambda m: self.emergence_ants_y2()
        })

        self.datacollector9 = DataCollector({
            "entropy_x_part2": lambda n: self.emergence_particle_x2()
        })
        self.datacollector10 = DataCollector({
            "entropy_y_part2": lambda n: self.emergence_particle_y2()
        })
        self.datacollector11 = DataCollector({
            "entropy_special_part2": lambda n: self.emergence_particle_special2()
        })

        pass

    def compute_entropy(self):
        pass

    def step(self):
        self.datacollector.collect(self)
        self.datacollector2.collect(self)
        self.datacollector3.collect(self)
        self.datacollector4.collect(self)
        self.datacollector5.collect(self)
        self.datacollector6.collect(self)
        self.datacollector7.collect(self)
        self.datacollector8.collect(self)
        self.datacollector9.collect(self)
        self.datacollector10.collect(self)
        self.datacollector11.collect(self)
        self.schedule.step()
        pass

    # returns list of all particels an agent can see
    def particels_in_view(self, agent):
        pass

    def step_in_ran_dir(self, agent):
        pass

    def jump_in_rand_dir(self, agent):
        pass

    def pick_particel(self, agent, particel):
        pass

    def drop_particel(self, agent):
        pass

    def init_particels(self):
        pass

    def init_agents(self):
        pass

    def system_entropy(self):
        pass

    # Ants emergence
    def emergence_ants_x(self):
        return self.entropy_ants_x - BaseEntropy.entropy_x(self.ant_agents, self.grid.width)

    def emergence_ants_y(self):
        return self.entropy_ants_y - BaseEntropy.entropy_y(self.ant_agents, self.grid.height)

    def emergence_ants_special(self):
        return self.entropy_ants_special - BaseEntropy.specific_entropy_ant(self.ant_agents)

    # Particle emergence
    def emergence_particle_x(self):
        return self.entropy_particle_x - BaseEntropy.entropy_x(self.particle_agents, self.grid.width)

    def emergence_particle_y(self):
        return self.entropy_particle_y - BaseEntropy.entropy_y(self.particle_agents, self.grid.height)

    def emergence_particle_special(self):
        return self.entropy_particle_special - BaseEntropy.specific_entropy_particle(self.grid, self.particle_agents)

    # Ants emergence special
    def emergence_ants_x2(self):
        return self.entropy_ants_x2 - AbstractEntropies.entropy_x2(self.ant_agents, self.grid, self.grid.width)

    def emergence_ants_y2(self):
        return self.entropy_ants_y2 - AbstractEntropies.entropy_y2(self.ant_agents, self.grid, self.grid.height)

    # Particle emergence special
    def emergence_particle_x2(self):
        return self.entropy_particle_x2 - AbstractEntropies.entropy_x2(self.particle_agents, self.grid, self.grid.width)

    def emergence_particle_y2(self):
        return self.entropy_particle_y2 - AbstractEntropies.entropy_y2(self.particle_agents, self.grid, self.grid.height)

    def emergence_particle_special2(self):
        return self.entropy_particle_special2 - AbstractEntropies.specific_entropy_particle2(self.grid, self.particle_agents, 2)