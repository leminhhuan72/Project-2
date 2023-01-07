from visualization.constant import WINDOW_HEIGHT, WINDOW_WIDTH
from log import logger
from hint import hint_pool
from pirate import pirate
from agent import agent
from map import map
import sys
import pygame
pygame.init()

WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


class game:
    def __init__(self, in_path, out_path):
        global THEME
        self.import_data(in_path)
        self.map = map(self.Width, self.Height,
                       self.detailed_map, self.Regions_number)
        self.pirate = pirate(
            self.map, self.treasure_position, self.reveal_turn, self.free_turn)
        self.agent = agent(self.map, self.pirate)
        self.hint_manager = hint_pool(
            self.agent, self.pirate, self.treasure_position, self.map)
        self.logger = logger(out_path)
        self.is_gameover = False
        self.run = True
        self.TURN = 0

    def import_data(self, in_path):
        f = open(in_path, "r")
        size = f.readline().split()
        self.Width = int(size[0])
        self.Height = int(size[1])
        self.reveal_turn = int(f.readline())
        self.free_turn = int(f.readline())
        self.Regions_number = int(f.readline())
        treasure_loc = f.readline().split()
        self.treasure_position = (int(treasure_loc[0]), int(treasure_loc[1]))

        self.detailed_map = []
        for line in f:
            lst_c = line.split(';')
            final = [c.strip() for c in lst_c]
            self.detailed_map.append(final)

        f.close()

    def check_state(self, run):
        if not self.is_gameover:
            self.logger.receive_message(run(self.TURN), self.TURN)
            if self.agent.found_treasure or self.pirate.found_treasure:
                self.is_gameover = True

    def run_game(self):
        print('GAME START')
        self.logger.receive_message(
            f'Game start\nThe pirate’s prison is going to reveal the at the beginning of the turn {self.pirate.turn_reveal}\n>The pirate is free at the beginning of the turn {self.pirate.free_turn}', self.TURN)
        next_turn = False
        check = -1
        while self.run:
            if check != self.TURN:
                print('Turn: ', self.TURN)
                check = self.TURN
            if not self.is_gameover:
                self.map.map[self.treasure_position[0]
                             ][self.treasure_position[1]].entity = 'T'

                if next_turn:
                    self.logger.receive_message(
                        f'START TURN {self.TURN}', self.TURN)
                    hint = self.hint_manager.get_random_hint(self.TURN)
                    self.logger.receive_message(
                        hint.get_hint_message(), self.TURN)
                    self.logger.receive_message(
                        self.agent.add_to_hintlist(hint), self.TURN)
                    self.check_state(self.pirate.run)
                    self.check_state(self.agent.run)
                    self.logger.receive_message(
                        f'END TURN {self.TURN}', self.TURN)
                    next_turn = False

            self.map.draw_map(WIN)
            self.pirate.draw(WIN, self.TURN)
            self.agent.draw(WIN)
            self.logger.draw(self.TURN, WIN)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    self.logger.export_log()

                if event.type == pygame.KEYDOWN and not self.is_gameover:
                    self.TURN += 1
                    next_turn = True
        pygame.quit()
