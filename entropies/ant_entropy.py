from entropies.base_entropy import BaseEntropy

class AntEntropy(BaseEntropy):
    def __init__(self, grid, ants):
        super().__init__(grid, ants)
        pass

    def behavioural_entropy_ratio(self, agent):
        return (1 if agent.particel is None else 2) / 2

    def get_entropy(self):
        pass