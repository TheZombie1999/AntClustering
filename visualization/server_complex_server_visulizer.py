from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import CanvasGrid, ChartModule
from agents.ant_agent import AntAgent
from agents.typed_particle_agent import TypedParticelAgent
from models.complex_clustering_model import ComplexClusteringModel


class ComplexClusteringMode(object):
    pass


class ServerComplexVisulizer:

    def __init__(self, model):
        # super().__init__(model=model)
        self.model = model
        grid = CanvasGrid(self.agent_portrayal, 50, 50, 500, 500)

        model_params = {
            "mid": UserSettableParameter('checkbox', 'Start mid', False),
            "num_ants": UserSettableParameter('slider', 'Number of ants', 50, 1, 100),
            "density_of_particels": UserSettableParameter('slider', 'Density of particles', 25, 1, 100),
            "step_size": UserSettableParameter('slider', 'Step size', 3, 1, 10),
            "jumping_distance": UserSettableParameter('slider', 'Step size', 8, 5, 20),
            "perceptionRadius": model.perceptionRadius,
            "particleThreshhold": model.particleThreshhold,
            "kPlus": model.kPlus,
            "kMinus": model.kMinus
        }

        chart = ChartModule([{"Label": "entropy_x_ants", "Color": "Black"}], data_collector_name='datacollector')
        chart2 = ChartModule([{"Label": "entropy_y_ants", "Color": "Black"}], data_collector_name='datacollector2')
        chart3 = ChartModule([{"Label": "entropy_special_ants", "Color": "Black"}],
                             data_collector_name='datacollector3')

        chart4 = ChartModule([{"Label": "entropy_x_part", "Color": "Black"}], data_collector_name='datacollector4')
        chart5 = ChartModule([{"Label": "entropy_y_part", "Color": "Black"}], data_collector_name='datacollector5')
        chart6 = ChartModule([{"Label": "entropy_special_part", "Color": "Black"}],
                             data_collector_name='datacollector6')

        server = ModularServer(ComplexClusteringModel,
                               visualization_elements=[grid, chart, chart2, chart3, chart4, chart5, chart6],
                               name="Ant Model",
                               model_params=model_params)
        server.port = 8525  # The default
        server.launch()
        pass

    def agent_portrayal(self, agent):
        self.model.particleThreshhold
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