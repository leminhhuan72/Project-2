from copy import deepcopy
import random
from visualization.constant import DIRECTIONS
from algorithms.astar import astar


class pirate:
    def __init__(self, map, treasure_position, turn_reveal, free_turn):
        self.map = map
        self.initial_loc = self.get_random_prison()
        self.current_loc = self.initial_loc
        self.treasure_position = treasure_position
        self.turn_reveal = turn_reveal
        self.free_turn = free_turn
        self.path_instruction = astar(
            self.initial_loc, self.treasure_position, self.map, [1, 2])  # A*
        self.found_treasure = False
        self.current_direct = None

    def run(self, CUR_TURN):
        if CUR_TURN < self.turn_reveal:
            return ''
        if CUR_TURN == self.turn_reveal:
            return 'Pirate is in prison ' + str(self.initial_loc)
        if CUR_TURN < self.free_turn:
            return ''
        message = ''
        if CUR_TURN == self.free_turn:
            message += 'Pirate is free/'

        dest = self.path_instruction.pop()
        cor_x = dest[0] - self.current_loc[0]
        cor_y = dest[1] - self.current_loc[1]
        step = abs(cor_x) + abs(cor_y)
        if cor_x % 2 == 0:
            cor_x //= 2
        if cor_y % 2 == 0:
            cor_y //= 2

        self.current_direct = DIRECTIONS[(cor_x, cor_y)]
        self.current_loc = deepcopy(dest)
        message += f'Pirate moves {step} steps to the {self.current_direct}'
        if not len(self.path_instruction):
            self.found_treasure = True
            message += 'The Pirate has found the treasure\nPIRATE WON!'

        return message

    def get_current_direct(self):
        return self.current_direct

    def get_random_prison(self):
        prisons = []
        for row in self.map.map:
            for grid in row:
                if grid.entity == 'P':
                    prisons.append((grid.row, grid.col))
        # print(prisons)
        return random.choice(prisons)

    def draw(self, win, cur_turn):
        if cur_turn < self.free_turn:
            return
        PIRATE = (215, 227, 86)
        x = (self.current_loc[1] + 3/2) * self.map.grid_w
        y = (self.current_loc[0] + 3/2) * self.map.grid_h
        text = self.map.THEME.render('Pi', True, PIRATE)
        center_rect = (x - text.get_rect().width/2,
                       y - text.get_rect().height/2)
        win.blit(text, center_rect)
