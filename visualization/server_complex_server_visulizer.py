from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
import random
from agents.ant_agent import AntAgent
from agents.typed_particle_agent import TypedParticelAgent
from models.complex_clustering_model import ComplexClusteringModel


class ComplexClusteringMode(object):
    pass


class ServerComplexVisulizer:

    def __init__(self, model):
        #super().__init__(model=model)
        self.model = model
        grid = CanvasGrid(self.agent_portrayal, 50, 50, 500, 500)

        chart = ChartModule([{"Label": "emergence",
                              "Color": "Black"}],
                            data_collector_name='datacollector')

        server = ModularServer(ComplexClusteringModel,
                               visualization_elements= [grid,chart],
                               name ="Ant Model",
                               model_params={"mid":model.middel, "num_ants":model.num_ants, "density_of_particels":model.density_of_particels, "step_size":model.step_size, "jumping_distance":model.jumping_distance,"perceptionRadius":model.perceptionRadius,"particleThreshhold": model.particleThreshhold,"kPlus": model.kPlus,"kMinus": model.kMinus})
        server.port = 8525  # The default
        server.launch()
        pass

    def agent_portrayal(self, agent):
        self.model.particleThreshhold
        #color = ["#7FFF00", "#00FF00", "#9ACD32", "#ADFF2F", "yellow", "khaki", "peachpuff", "moccasin", "gold", "orange", "darkorange", "coral", "tomato", "orangered", "indianred", "crimson", "red", "darkred", "firebrick", "indianred"]#
        color = ["blue", "green", "orange"]
        protrayal = None
        if type(agent) is AntAgent:
            portrayal = {"Shape": "circle",
                        "Color": "red",
                        "Filled": "true",
                        "Layer": 0,
                        "r": 0.5}
            if agent.particel:
                portrayal["Color"] = "black"


        if type(agent) is TypedParticelAgent:
            portrayal = {"Shape": "circle",
                         "Color": "blue",
                         "Filled": "true",
                         "Layer": 0,
                         "r": 0.2}
            portrayal["Color"] = color[agent.particleType]
        return portrayal

