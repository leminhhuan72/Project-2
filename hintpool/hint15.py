from random import *


def get_hint_15(self):
    message = 'The treasure is in a region that has mountain'
    return [message, None]


def verify_hint_15(self, data):
    regions = [False for i in range(self.map.R)]
    for row in range(0, self.map.H):
        for col in range(0, self.map.W):
            if self.map.map[row][col].is_mountain():
                regions[self.map.map[row][col].region-1] = True

    t_region = self.map.map[self.treasure_position[0]
                            ][self.treasure_position[1]].region
    if regions[t_region-1]:
        for row in range(0, self.map.H):
            for col in range(0, self.map.W):
                if not self.map.map[row][col].is_sea() and not regions[self.map.map[row][col].region-1]:
                    if self.map.map[row][col].is_sea() == False:
                        self.map.map[row][col].make_scan()
        return True

    for row in range(0, self.map.H):
        for col in range(0, self.map.W):
            if not self.map.map[row][col].is_sea() and regions[self.map.map[row][col].region-1]:
                if self.map.map[row][col].is_sea() == False:
                    self.map.map[row][col].make_scan()
    return False
