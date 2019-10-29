import matplotlib.pyplot as plt
import numpy as np



from agents.particel_agent import ParticelAgent
from agents.ant_agent import AntAgent


class Visulizer :
    def __init__(self, model):
        self.model = model
        self.particel_data = []
        self.agent_data = []
        pass

    def collect_data(self, number_of_interations):
        for i in range(number_of_interations):
            for m in range (10):
                self.model.step()
            step_data_p = np.zeros((self.model.grid.height, self.model.grid.width))
            step_data_a = np.zeros((self.model.grid.height, self.model.grid.width))
            for cell in self.model.grid.coord_iter():
                cell_content, x, y = cell

                for element in cell_content:
                    if type(element) is ParticelAgent:
                        step_data_p[x][y] += 1
                    if type(element) is AntAgent:
                        step_data_a[x][y] += 1

            self.particel_data.append(step_data_p)
            self.agent_data.append(step_data_a)
        pass

    def visulize_data (self, t):
        data = (self.particel_data, self.agent_data)
        fig, ax = plt.subplots(nrows= 1, ncols=2)

        ax[0].imshow(data[0][t],interpolation='nearest')
        ax[1].imshow(data[1][t],interpolation='nearest')
        plt.show()
        pass