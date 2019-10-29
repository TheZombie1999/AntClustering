from agents.ant_agent import AntAgent
from agents.particel_agent import ParticelAgent
from visualization.visulizer import Visulizer
from models.simpel_clustering_model import SimpleClusteringModel
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

class ServerVizuliser:

    def __init__(self, model):
        #super().__init__(model=model)
        grid = CanvasGrid(self.agent_portrayal, 50, 50, 500, 500)
        server = ModularServer(SimpleClusteringModel,
                               [grid],
                               "Ant Model",
                               { "num_ants":50, "density_of_particels":10, "step_size":5, "jumping_distance":10})
        server.port = 8525  # The default
        server.launch()
        pass

    def agent_portrayal(self, agent):
        protrayal = None
        if type(agent) is AntAgent:
            portrayal = {"Shape": "circle",
                        "Color": "red",
                        "Filled": "true",
                        "Layer": 0,
                        "r": 0.5}

        if type(agent) is ParticelAgent:
            portrayal = {"Shape": "circle",
                         "Color": "blue",
                         "Filled": "true",
                         "Layer": 0,
                         "r": 0.2}
        return portrayal

