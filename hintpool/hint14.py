from random import *


def get_hint_14(self):
    top_large, left_large, size_large = None, None, None
    SIZE_MIN = self.map.H // 4
    while True:
        top_large = randrange(0, self.map.H)
        left_large = randrange(0, self.map.W)
        size_large = randrange(SIZE_MIN, self.map.W)
        if top_large + size_large < self.map.H and left_large + size_large < self.map.W:
            break

    top_small, left_small, size_small = None, None, None
    while True:
        top_small = randrange(top_large+1, top_large + size_large)
        left_small = randrange(
            left_large+1, left_large + size_large)
        size_small = randrange(1, size_large)
        if top_small + size_small < top_large + size_large and left_small + size_small < left_large + size_large:
            break

    cor_large = [top_large, left_large, top_large +
                 size_large, left_large + size_large]
    cor_small = [top_small, left_small, top_small +
                 size_small, left_small + size_small]
    message = 'The treasure is somewhere inside the gap between 2 squares (top, left, bottom, right) ' + str(
        cor_large) + ' and ' + str(cor_small)
    return (message, (cor_large, cor_small))


def verify_hint_14(self, data):
    cor_large, cor_small = data
    t_row, t_col = self.treasure_position
    if t_row in range(cor_large[0], cor_large[2] + 1) and t_col in range(cor_large[1], cor_large[3]+1) and not (t_row in range(cor_small[0], cor_small[2] + 1) and t_col in range(cor_small[1], cor_small[3]+1)):
        for row in range(0, self.map.H):
            for col in range(0, self.map.W):
                if row in range(cor_large[0], cor_large[2] + 1) and col in range(cor_large[1], cor_large[3]+1) and not (row in range(cor_small[0], cor_small[2] + 1) and col in range(cor_small[1], cor_small[3]+1)):
                    continue
                if self.map.map[row][col].is_sea() == False:
                    self.map.map[row][col].make_scan()
        return True

    for row in range(0, self.map.H):
        for col in range(0, self.map.W):
            if row in range(cor_large[0], cor_large[2] + 1) and col in range(cor_large[1], cor_large[3]+1) and not (row in range(cor_small[0], cor_small[2] + 1) and col in range(cor_small[1], cor_small[3]+1)):
                if self.map.map[row][col].is_sea() == False:
                    self.map.map[row][col].make_scan()
    return False
