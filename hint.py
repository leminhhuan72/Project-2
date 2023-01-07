import random
import numpy
import math
from visualization.constant import REGIONS, DIRECTIONS
from hintpool import *


class hint:
    def __init__(self, ID, get_hint, verify_hint, hintpool):
        self.ID = None
        self.name = None
        self.message = None
        self.data = None
        self.verify_hint = verify_hint
        self.get_hint = get_hint
        self.hintpool = hintpool

    def read_hint(self,  cur_turn):
        res = self.get_hint(self.hintpool)
        self.name = f'hint {cur_turn}'
        self.message = res[0]
        self.data = res[1]

    def is_verified(self):
        return self.verify_hint(self.hintpool, self.data)

    def get_hint_message(self):
        return self.name + ': ' + self.message


class hint_pool:
    def __init__(self, agent, pirate, treasure_position, map):
        self.agent = agent
        self.pirate = pirate
        self.treasure_position = treasure_position
        self.map = map  # self.map.map = 2D list of Grids
        self.map.Hints = [hint(1,  hint1.get_hint_1, hint1.verify_hint_1, self),
                          hint(2, hint2.get_hint_2, hint2.verify_hint_2, self),
                          hint(3,  hint3.get_hint_3, hint3.verify_hint_3, self),
                          hint(4,  hint4.get_hint_4, hint4.verify_hint_4, self),
                          hint(5, hint5.get_hint_5, hint5.verify_hint_5, self),
                          hint(6, hint6.get_hint_6, hint6.verify_hint_6, self),
                          hint(7, hint7.get_hint_7, hint7.verify_hint_7, self),
                          hint(8,  hint8.get_hint_8, hint8.verify_hint_8, self),
                          hint(9,  hint9.get_hint_9, hint9.verify_hint_9, self),
                          hint(10, hint10.get_hint_10,
                               hint10.verify_hint_10, self),
                          hint(11, hint11.get_hint_11,
                               hint11.verify_hint_11, self),
                          hint(12, hint12.get_hint_12,
                               hint12.verify_hint_12, self),
                          hint(13, hint13.get_hint_13,
                               hint13.verify_hint_13, self),
                          hint(14, hint14.get_hint_14,
                               hint14.verify_hint_14, self),
                          hint(15, hint15.get_hint_15, hint15.verify_hint_15, self)]

    def get_random_hint(self, cur_turn):
        hint = None
        res = None
        p_rare = 0.02
        num_of_rare = 2
        p_other = (1 - num_of_rare*p_rare) / (15 - num_of_rare)
        p_lst = [p_other, p_other, p_other, p_other, p_other, p_other, p_rare,
                 p_other, p_other, p_other, p_other, p_rare, p_other, p_rare, p_other]
        hint = random.choices(self.map.Hints, weights=p_lst, k=1)[0]
        hint.read_hint(cur_turn)
        if cur_turn == 1:
            res = hint.is_verified()
            while not res:
                hint = random.choice(self.map.Hints)
                hint.read_hint(cur_turn)
                res = hint.is_verified()
            self.map.reset_map()
        return hint
