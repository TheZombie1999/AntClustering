import math

class Util:
    def get_outer_circel_cords(x, radius, pos, grid_size):
        try:
            return round(math.sqrt(math.pow(radius, 2)-(x - math.pow((x-pos[0]),2)))+ pos[1]) % grid_size
        except:
            return x % grid_size