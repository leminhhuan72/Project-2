from random import *


def get_hint_5(self):
    size = self.map.H // 8
    random_loc = (randint(0, self.map.H-size-1),
                  randint(0, self.map.W-size-1))
    message = f'A small rectangle area {random_loc[0], random_loc[1], random_loc[0] + size, random_loc[1] + size} that doesn not have the treasure'
    return (message, (random_loc[0], random_loc[1], random_loc[0] + size, random_loc[1] + size))


def verify_hint_5(self, data):
    top, left, bot, right = data
    if self.treasure_position[0] in range(top, bot+1) and self.treasure_position[1] in range(left, right+1):
        for row in range(self.map.H):
            for col in range(self.map.W):
                if row not in range(top, bot+1) or col not in range(left, right+1):
                    if self.map.map[row][col].is_sea() == False:
                        self.map.map[row][col].make_scan()
        return False

    for row in range(top, bot+1):
        for col in range(left, right+1):
            if self.map.map[row][col].is_sea() == False:
                self.map.map[row][col].make_scan()
    return True
