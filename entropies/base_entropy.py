import math
from agents.typed_particle_agent import TypedParticelAgent

class BaseEntropy():
    def single_ant_entropy(agent):
        return (1 if agent.particel is None else 2) / 2


    def same_outer_particles(self, agent):
        siblings = 0
        x = self.grid.get_neighbors(agent.pos, include_center=False, radius=1, moore=True)
        for i in x:
            if type(i) is TypedParticelAgent and i.particleType == agent.particleType:
                siblings += 1
        return siblings

    def single_particle_entropy(grid, agent):
        return BaseEntropy.same_outer_particles(agent) / 9


    def get_ant_entropy(model):
        agents = model.ant_agents
        grid_size = model.grid.width
        Hx = 0
        Hy = 0
        Hbehaviour = 0

        x_frequencies = [0] * grid_size
        y_frequencies = [0] * grid_size

        for x in range(grid_size):
            agent = agents[x]
            x_frequencies[agent.pos[0]] = x_frequencies[agent.pos[0]] + 1
            y_frequencies[agent.pos[1]] = y_frequencies[agent.pos[1]] + 1

            ratio = BaseEntropy.single_ant_entropy(agent)
            Hbehaviour += ratio * math.log2(ratio)

        for x in range(grid_size):
            x_ratio = x_frequencies[x] / grid_size
            y_ratio = y_frequencies[x] / grid_size

            Hx += x_ratio * math.log2(x_ratio)
            Hy += y_ratio * math.log2(y_ratio)

        return (-1 * Hx) + (-1 * Hy) + (-1 * Hbehaviour)

    def get_particle_entropy(model):
        agents = model.particle_agents
        grid_size = model.grid.width
        Hx = 0
        Hy = 0
        Hbehaviour = 0

        x_frequencies = [0] * grid_size
        y_frequencies = [0] * grid_size

        for x in range(grid_size):
            agent = agents[x]
            x_frequencies[agent.pos[0]] = x_frequencies[agent.pos[0]] + 1
            y_frequencies[agent.pos[1]] = y_frequencies[agent.pos[1]] + 1

            ratio = BaseEntropy.single_particle_entropy(model.grid, agent)
            Hbehaviour += ratio * math.log2(ratio)

        for x in range(grid_size):
            x_ratio = x_frequencies[x] / grid_size
            y_ratio = y_frequencies[x] / grid_size

            Hx += x_ratio * math.log2(x_ratio)
            Hy += y_ratio * math.log2(y_ratio)

        return (-1 * Hx) + (-1 * Hy) + (-1 * Hbehaviour)

    def get_system_entropy(model):
        return BaseEntropy.get_ant_entropy(model) + BaseEntropy.get_particle_entropy(model)