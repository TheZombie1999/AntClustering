from visualization.Visulizer import Visulizer
from models.simpel_clustering_model import SimpleClusteringModel

numAnts = 10
densityOfParticels = 3
stepSize = 1
jumpingDistance = 5

num_steps = 1000
model = SimpleClusteringModel(numAnts, densityOfParticels, stepSize, jumpingDistance)

v = Visulizer(model=model)
v.collect_data(num_steps)
for i in range(num_steps):
    v.visulize_data(i)

