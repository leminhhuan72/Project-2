from random import *


def get_hint_2(self):
    random_num = randint(2, 5)
    random_regions = choices(range(1, self.map.R), k=random_num)
    message = f'{random_regions} that 1 of them has the treasure'
    return (message, random_regions)


def verify_hint_2(self, data):
    random_regions = data
    t_row, t_col = self.treasure_position
    t_region = self.map.map[t_row][t_col].region
    if t_region in random_regions:
        for row in range(self.map.H):
            for col in range(self.map.W):
                if self.map.map[row][col].region not in random_regions:
                    if self.map.map[row][col].is_sea() == False:
                        self.map.map[row][col].make_scan()
        return True

    for row in range(self.map.H):
        for col in range(self.map.W):
            if self.map.map[row][col].region in random_regions:
                if self.map.map[row][col].is_sea() == False:
                    self.map.map[row][col].make_scan()
    return False
