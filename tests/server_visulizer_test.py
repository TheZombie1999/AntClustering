from models.simpel_clustering_model import SimpleClusteringModel
from visualization.server_visulizer import ServerVizuliser

numAnts = 50
densityOfParticels = 50
stepSize = 3
jumpingDistance = 8
middel = False

model = SimpleClusteringModel(middel, numAnts, densityOfParticels, stepSize, jumpingDistance)

server = ServerVizuliser(model)