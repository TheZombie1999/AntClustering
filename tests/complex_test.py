from models.complex_clustering_model import ComplexClusteringModel
from visualization.server_complex_server_visulizer import ServerComplexVisulizer

numAnts = 65
densityOfParticels = 18
stepSize = 3
jumpingDistance = 8
middel = False

model = ComplexClusteringModel(middel, numAnts, densityOfParticels, stepSize, jumpingDistance, particleThreshhold=3, perceptionRadius=1, kPlus=0.1, kMinus= 0.3)

server = ServerComplexVisulizer(model)