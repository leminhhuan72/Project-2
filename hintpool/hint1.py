
from random import *


def get_hint_1(self):
    random_quantity = randrange(1, 13)
    tiles = []
    while len(tiles) < random_quantity:
        tile = (randrange(0, self.map.H),
                randrange(0, self.map.W))
        if tile not in tiles:
            tiles.append(tile)
    message = str(tiles) + " doesn't contain the treasure"
    return (message, tiles)


def verify_hint_1(self, data):
    if self.treasure_position in data:
        for row in range(self.map.H):
            for col in range(self.map.W):
                if (row, col) not in data:
                    if self.map.map[row][col].is_sea() == False:
                        self.map.map[row][col].make_scan()

        return False

    for loc in data:
        if self.map.map[loc[0]][loc[1]] == False:
            self.map.map[loc[0]][loc[1]].make_scan()
    return True
