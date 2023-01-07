from random import *


def get_hint_12(self):
    half_side = randint(0, 1)
    message = "Right" if half_side else "Left"
    message += " half does not contain the treasure"
    return (message, half_side)


def verify_hint_12(self, data):
    if data == 0:
        if self.treasure_position[1] > (self.map.W // 2):
            for c in range(0, self.map.W // 2 + 1):
                for r in range(0, self.map.H):
                    if self.map.map[r][c].is_sea() == False:
                        self.map.map[r][c].make_scan()
            return True
        else:
            for c in range(self.map.W // 2 + 1, self.map.W):
                for r in range(0, self.map.H):
                    if self.map.map[r][c].is_sea() == False:
                        self.map.map[r][c].make_scan()

    if data == 1:
        if self.treasure_position[1] <= (self.map.W // 2):
            for c in range(self.map.W // 2 + 1, self.map.W):
                for r in range(0, self.map.H):
                    if self.map.map[r][c].is_sea() == False:
                        self.map.map[r][c].make_scan()
            return True
        else:
            for c in range(0, self.map.W // 2 + 1):
                for r in range(0, self.map.H):
                    if self.map.map[r][c].is_sea() == False:
                        self.map.map[r][c].make_scan()

    return False
