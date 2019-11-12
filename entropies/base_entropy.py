import math

class BaseEntropy():
    def __init__(self, grid, agents):
        self.agents = agents
        self.grid_size = 50
        self.grid = grid

        self.initialEntropy = self.get_entropy()
        pass

    def behavioural_entropy_ratio(self, agent):
        pass

    def get_entropy(self):
        Hx = 0
        Hy = 0
        Hbehaviour = 0

        x_frequencies = [0] * self.grid_size
        y_frequencies = [0] * self.grid_size

        for x in range(self.grid_size):
            agent = self.agents[x]
            x_frequencies[agent.pos[0]] = x_frequencies[agent.pos] + 1
            y_frequencies[agent.pos[1]] = y_frequencies[agent.pos] + 1

            ratio = self.behavioural_entropy_ratio(agent)
            Hbehaviour += ratio * math.log2(ratio)

        for x in range(self.grid_size):
            x_ratio = x_frequencies[x] / self.grid_size
            y_ratio = y_frequencies[x] / self.grid_size

            Hx += x_ratio * math.log2(x_ratio)
            Hy += y_ratio * math.log2(y_ratio)

        return (-1 * Hx) + (-1 * Hy) + (-1 * Hbehaviour)