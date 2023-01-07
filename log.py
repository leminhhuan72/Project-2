from visualization.textrect import render_textrect
from visualization.constant import WINDOW_WIDTH, WINDOW_HEIGHT, MAP_H, MAP_W
import pygame
pygame.init()

LOG_W = WINDOW_WIDTH / 2
LOG_H = 700
LOG_LINES = 10
LOG_COLOR = (255, 255, 255)


class logger:
    def __init__(self, fout_path):
        self.messages = []
        self.area = pygame.Rect(
            MAP_W + (WINDOW_WIDTH - MAP_W - LOG_W)//2, (WINDOW_HEIGHT - LOG_H)//3, LOG_W, LOG_H)
        self.font = pygame.font.Font('./font/opensans.ttf', 22)
        self.fout_path = fout_path

    def export_log(self):
        f = open(self.fout_path, "w")
        for turn_log in self.messages:
            f.write(turn_log)
        print('Save logs successfully')
        f.close()

    def receive_message(self, messages, this_turn):
        if not messages:
            return
        while this_turn > len(self.messages)-1:
            self.messages.append('')
        proccessed_messages = messages.split('\n')
        proccessed_messages = [s for s in proccessed_messages if s != '']
        if '' in proccessed_messages:
            proccessed_messages = proccessed_messages.remove('')

        for message in proccessed_messages:
            #print(this_turn, len(self.messages)-1)
            self.messages[this_turn] += '\n> ' + message

    def draw(self, this_turn, win):
        rendered_text = render_textrect(
            self.messages[this_turn], self.font, self.area, (0, 0, 0), LOG_COLOR)
        win.blit(rendered_text, self.area.topleft)
