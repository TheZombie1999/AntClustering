import math

from agents.typed_particle_agent import TypedParticelAgent


class BaseEntropy:
    def same_outer_particles(grid, agent):
        siblings = 0
        if agent.pos is None:
            return 0
        x = grid.get_neighbors(agent.pos, include_center=False, radius=1, moore=True)
        for i in x:
            if type(i) is TypedParticelAgent and i.particleType == agent.particleType:
                siblings += 1
        return siblings

    def entropy_x(agents, x_margin):
        frequencies = [0] * x_margin
        entropy = 0
        for agent in agents:
            if agent.pos is None:
                continue
            frequencies[agent.pos[0]] += 1

        for y in range(x_margin):
            x_ratio = frequencies[y] / x_margin
            try:
                entropy += x_ratio * math.log2(x_ratio)
            except ValueError:
                pass

        return -1 * entropy

    def entropy_y(agents, y_margin):
        frequencies = [0] * y_margin
        entropy = 0
        for agent in agents:
            if agent.pos is None:
                continue
            frequencies[agent.pos[1]] += 1

        for y in range(y_margin):
            y_ratio = frequencies[y] / y_margin
            try:
                entropy += y_ratio * math.log2(y_ratio)
            except ValueError:
                pass

        return -1 * entropy

    def specific_entropy_particle(grid, agents):
        frequencies = [0] * 10
        entropy = 0
        for agent in agents:
            siblings = BaseEntropy.same_outer_particles(grid, agent)
            frequencies[siblings] = frequencies[siblings] + 1

        for y in range(9):
            ratio = frequencies[y] / 9
            try:
                entropy += ratio * math.log2(ratio)
            except ValueError:
                pass
        return -1 * entropy

    def specific_entropy_ant(agents):
        laden = 0
        for a in agents:
            if a.particel is not None:
                laden += 1
        # laden = sum(a.particel is not None for a in agents)
        # print(laden)
        ratio = laden / len(agents)
        try:
            ret = -1 * ratio * math.log2(ratio)
        except ValueError:
            ret = 0
        return ret
