import math
from agents.typed_particle_agent import TypedParticelAgent

class BaseEntropy():

    def same_outer_particles(grid, agent):
        siblings = 0
        x = grid.get_neighbors(agent.pos, include_center=False, radius=1, moore=True)
        for i in x:
            if type(i) is TypedParticelAgent and i.particleType == agent.particleType:
                siblings += 1
        return siblings

    def entropy_x(agents, x_margin):
        frequencies = [0] * x_margin
        entropy = 0
        for x in range(len(agents)):
            agent = agents[x]
            frequencies[agent.pos[0]] = frequencies[agent.pos[0]] + 1

        for y in range(range(x_margin)):
            x_ratio = frequencies[y] / x_margin
            entropy += x_ratio * math.log2(x_ratio)

        return -1 * entropy

    def entropy_y(agents, y_margin):
        frequencies = [0] * y_margin
        entropy = 0
        for x in range(len(agents)):
            agent = agents[x]
            frequencies[agent.pos[1]] = frequencies[agent.pos[1]] + 1

        for y in range(range(y_margin)):
            y_ratio = frequencies[y] / y_margin
            entropy += y_ratio * math.log2(y_ratio)

        return -1 * entropy

    def specific_entropy_particle(grid, agents):
        frequencies = [0] * 10
        entropy = 0
        for x in range(len(agents)):
            agent = agents[x]
            siblings = BaseEntropy.same_outer_particles(grid, agent)
            frequencies[siblings] = frequencies[siblings] + 1

        for y in range(11):
            ratio = frequencies[y] / 10
            entropy += ratio * math.log2(ratio)

        return -1 * entropy


    def specific_entropy_ant(agents):
        laden = sum(a.particel is not None for a in agents)
        ratio = laden / len(agents)
        return -1 * ratio * math.log2(ratio)