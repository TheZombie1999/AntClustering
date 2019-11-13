import math

from agents.typed_particle_agent import TypedParticelAgent
from entropies.base_entropy import BaseEntropy


class AbstractEntropies:
    def same_outer_particles(grid, agent, radius):
        siblings = 0
        x = grid.get_neighbors(agent.pos, include_center=False, radius=radius, moore=True)
        for i in x:
            if type(i) is TypedParticelAgent and i.particleType == agent.particleType:
                siblings += 1
        return siblings

    def entropy_x2(agents,grid, x_margin):
        frequencies = [0] * x_margin
        entropy = 0
        for agent in agents:
            pos = AbstractEntropies.translate(agent.pos[0],0,grid.size, 0, x_margin)
            pos = round(pos)
            frequencies[pos] += 1

        for y in range(x_margin):
            x_ratio = frequencies[y] / x_margin
            try:
                entropy += x_ratio * math.log2(x_ratio)
            except:
                pass
        return -1 * entropy

    def entropy_y2(agents, grid, y_margin):
        frequencies = [0] * y_margin
        entropy = 0
        for agent in agents:
            pos = AbstractEntropies.translate(agent.pos[0],0,grid.size, 0, y_margin)
            pos = round(pos)
            frequencies[agent.pos[1]] += 1

        for y in range(y_margin):
            y_ratio = frequencies[y] / y_margin
            try:
                entropy += y_ratio * math.log2(y_ratio)
            except ValueError:
                pass
        return -1 * entropy

    def specific_entropy_particle(grid, agents, radius):
        num_of_neighbours = math.pow(2* radius +1, 2) - 1
        frequencies = [0] * num_of_neighbours
        entropy = 0
        for x in range(len(agents)):
            agent = agents[x]
            siblings = BaseEntropy.same_outer_particles(grid, agent, radius)
            frequencies[siblings] = frequencies[siblings] + 1

        for y in range(num_of_neighbours + 1):
            ratio = frequencies[y] / num_of_neighbours
            entropy += ratio * math.log2(ratio)

        return -1 * entropy


    def specific_entropy_ant(agents):
        laden = sum(a.particel is not None for a in agents)
        ratio = laden / len(agents)
        return -1 * ratio * math.log2(ratio)

    def translate(value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)