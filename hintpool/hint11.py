from random import *

from visualization.constant import REGIONS, DIRECTIONS


def get_hint_11(self):
    distance = randint(2, 3)
    message = f'The treasure is somewhere in an area bounded by {distance} tiles from sea'
    return (message, distance)


def verify_hint_11(self, data):
    distance = data
    grids = []
    for row in range(self.map.H):
        for col in range(self.map.W):
            if self.map.map[row][col].is_sea():
                for direct in DIRECTIONS:
                    for i in range(1, distance+1):
                        nb_grid = (row + i*direct[0], col + i*direct[1])
                        if nb_grid[0] in range(self.map.H) and nb_grid[1] in range(self.map.W) and not self.map.map[nb_grid[0]][nb_grid[1]].is_sea():
                            grids.append(nb_grid)

    if self.treasure_position not in grids:
        for grid in grids:
            if self.map.map[grid[0]][grid[1]].is_sea() == False:
                self.map.map[grid[0]][grid[1]].make_scan()
        return False

    for row in range(self.map.H):
        for col in range(self.map.W):
            if (row, col) not in grids:
                if self.map.map[row][col].is_sea() == False:
                    self.map.map[row][col].make_scan()
    return True
