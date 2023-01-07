from random import *
from visualization.constant import REGIONS, DIRECTIONS


def get_nb_regions(self):
    nb_regions = [[] for i in range(self.map.R-1)]
    for row in range(self.map.H):
        for col in range(self.map.W):
            cur_grid = self.map.map[row][col]
            if not cur_grid.is_sea():
                for direct in DIRECTIONS:
                    nb_row = row + direct[0]
                    nb_col = col + direct[1]
                    if nb_row in range(self.map.H) and nb_col in range(self.map.W):
                        nb_region = self.map.map[nb_row][nb_col].region
                        cur_region = cur_grid.region
                        if nb_region != cur_region and nb_region != 0 and nb_region not in nb_regions[cur_region-1]:
                            nb_regions[cur_region-1].append(nb_region)

    return nb_regions


def get_boundaries(self, region, nb_region):
    boundaries_loc = []
    for row in range(self.map.H):
        for col in range(self.map.W):
            grid = self.map.map[row][col]
            if grid.region == REGIONS[region]:
                for direct in DIRECTIONS:
                    nb_row = row + direct[0]
                    nb_col = col + direct[1]
                    if nb_row in range(self.map.H) and nb_col in range(self.map.W) and self.map.map[nb_row][nb_col].region is REGIONS[nb_region]:
                        if (row, col) not in boundaries_loc:
                            boundaries_loc.append((row, col))
                        if (nb_row, nb_col) not in boundaries_loc:
                            boundaries_loc.append((nb_row, nb_col))

    return boundaries_loc


def get_hint_9(self):
    nb_regions = get_nb_regions(self)
    region = randrange(1, self.map.R)
    nb_region = choice(nb_regions[region-1])
    message = "The treasure is somewhere in the boundary of region " + \
        str(region) + ' and ' + str(nb_region)
    return [message, (region, nb_region)]


def verify_hint_9(self, data):
    region, nb_region = data
    boundaries_loc = get_boundaries(self, region, nb_region)

    if self.treasure_position not in boundaries_loc:
        for loc in boundaries_loc:
            if self.map.map[loc[0]][loc[1]].is_sea() == False:
                self.map.map[loc[0]][loc[1]].make_scan()
        return False

    for row in range(self.map.H):
        for col in range(self.map.W):
            if (row, col) not in boundaries_loc:
                if self.map.map[row][col].is_sea() == False:
                    self.map.map[row][col].make_scan()
    return False
