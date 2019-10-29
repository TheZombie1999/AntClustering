from agents.particel_agent import ParticelAgent
from models.simpel_clustering_model import SimpleClusteringModel
import numpy as np
import matplotlib.pyplot as plt



"""
# two classes
    model and agent
    
scheduler controlls the order in which agents are activated

step fuction of model advances the intier model by one step
step fuction of agent advances the agent by one step
"""

numAnts = 10
densityOfParticels = 1
stepSize = 1
jumpingDistance = 5

model = SimpleClusteringModel(numAnts, densityOfParticels, stepSize, jumpingDistance)
data = []
for i in range(0,100):
    model.step()
    agent_counts = np.zeros((model.grid.width, model.grid.height))

    for cell in model.grid.coord_iter():
        cell_content, x, y = cell
        for i in cell_content:
            if type(i) is ParticelAgent:
                agent_counts[x][y] += 1
    data.append(agent_counts)

for i in data:
    plt.imshow(i, interpolation='nearest')
    plt.colorbar()
    plt.show()


