from mesa import Agent


class ParticelAgent (Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        pass

    def __step__(self):
        pass