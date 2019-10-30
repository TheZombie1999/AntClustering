from mesa import *
import numpy as np


class AntAgent(Agent):

    def __init__(self, id, model, startpos, site):
        super().__init__(id, model)

        self.model = model
        self.grid = model.grid

        self.unique_id = id
        self.particel = None # place holder for a particel
        self.site = site
        self.pos = np.array(startpos)
        pass

    def step(self):
        # comment tests
        model = self.model
        inView = model.particels_in_view(self)


        if  inView and not self.particel:

            # pickUp(object)
            model.pick_particel(self, inView)
            # jump j steps in random direction
            model.jump_in_rand_dir(self)

        elif self.particel and inView:

            # drop oi at empty place
            model.drop_particel(self)
            # jump j steps in random direction
            model.jump_in_rand_dir(self)

        else:

            # step in random dir with with s
            model.step_in_ran_dir(self)
            pass



