from random import *


def get_hint_8(self):
    row, col = (randrange(0, self.map.H),
                randrange(0, self.map.W))
    choose = choice([0, 1, 2])
    if choose == 0:
        message = f'Row {row} does not contain the treasure'
    if choose == 1:
        message = f'Column {col} does not contain the treasure'
    else:
        message = f'Row {row} and column {col} do not contain the treasure'

    return (message, [choose, (row, col)])


def verify_hint_8(self, data):
    choose = data[0]
    row, col = data[1]

    grids = []
    if choose == 0 or choose == 2:
        for c in range(self.map.W):
            grids.append((row, c))

    if choose == 1 or choose == 2:
        for r in range(self.map.H):
            grids.append((r, col))

    if self.treasure_position in grids:
        for r in range(self.map.H):
            for c in range(self.map.W):
                if (r, c) not in grids:
                    if self.map.map[r][c].is_sea() == False:
                        self.map.map[r][c].make_scan()
        return False

    for grid in grids:
        if self.map.map[grid[0]][grid[1]].is_sea() == False:
            self.map.map[grid[0]][grid[1]].make_scan()
    return True
