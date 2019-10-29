from models.simpel_clustering_model import SimpleClusteringModel
from visualization.server_visulizer import ServerVizuliser

numAnts = 10
densityOfParticels = 1
stepSize = 1
jumpingDistance = 5

model = SimpleClusteringModel(numAnts, densityOfParticels, stepSize, jumpingDistance)

server = ServerVizuliser(model)