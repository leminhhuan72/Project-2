from random import *


def get_hint_13(self):
    direct = choice(['W', 'E', 'N', 'S', 'SE', 'SW', 'NE', 'NW'])

    message = 'From the prison ' + \
        str(self.pirate.initial_loc) + \
        ', the direction that has the treasure is ' + direct
    return (message, direct)


def verify_hint_13(self, data):
    direct = data
    if direct in ['SE', 'SW', 'NE', 'NW']:
        row_range = range(0, 0)
        col_range = range(0, 0)
        if direct == 'SE':
            row_range = range(0, self.pirate.initial_loc[0] + 1)
            col_range = range(self.pirate.initial_loc[1], self.map.W)
        elif direct == 'SW':
            row_range = range(0, self.pirate.initial_loc[0] + 1)
            col_range = range(0, self.pirate.initial_loc[1] + 1)
        elif direct == 'NE':
            row_range = range(self.pirate.initial_loc[0], self.map.H)
            col_range = range(self.pirate.initial_loc[1], self.map.W)
        elif direct == 'NW':
            row_range = range(self.pirate.initial_loc[0], self.map.H)
            col_range = range(0, self.pirate.initial_loc[1] + 1)

        if self.treasure_position[0] not in row_range or self.treasure_position[1] not in col_range:
            for row in row_range:
                for col in col_range:
                    if self.map.map[row][col].is_sea() == False:
                        self.map.map[row][col].make_scan()
            return False

        for row in range(self.map.H):
            for col in range(self.map.W):
                if row not in row_range or col not in col_range:
                    if self.map.map[row][col].is_sea() == False:
                        self.map.map[row][col].make_scan()
        return True

    elif direct in ['W', 'E', 'N', 'S']:
        f1 = None
        f2 = None
        if direct == 'E':
            f1 = 1
            f2 = 1
        elif direct == 'W':
            f1 = -1
            f2 = -1
        elif direct == 'N':
            f1 = 1
            f2 = -1
        elif direct == 'S':
            f1 = -1
            f2 = 1

        def func(cor, f1, f2, x, y):
            l1 = (y - cor[1]) - (x - cor[0])
            l2 = (y - cor[1]) + (x - cor[0])
            if l1*f1 >= 0 and l2*f2 >= 0:
                return True
            return False

        if not func(self.pirate.initial_loc, f1, f2, self.treasure_position[0], self.treasure_position[1]):
            for r in range(self.map.H):
                for c in range(self.map.W):
                    if func(self.pirate.initial_loc, f1, f2, r, c):
                        if self.map.map[r][c].is_sea() == False:
                            self.map.map[r][c].make_scan()
            return False

        for r in range(self.map.H):
            for c in range(self.map.W):
                if not func(self.pirate.initial_loc, f1, f2, r, c):
                    if self.map.map[r][c].is_sea() == False:
                        self.map.map[r][c].make_scan()
        return True
