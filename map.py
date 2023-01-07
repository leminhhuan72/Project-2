from visualization.constant import MAP_H, MAP_W
from visualization.layout import layout
import pygame
pygame.init()


class map:
    def __init__(self, Width: int, Height: int, detailed_map, Region_number: int):
        self.grid_w = MAP_W // Width
        self.grid_h = MAP_H // Height
        self.W = Width
        self.H = Height
        self.R = Region_number
        self.map = self.make_map(Width, Height, detailed_map)
        self.THEME = pygame.font.Font(
            './font/opensans.ttf', round(self.grid_h/1.5))
        self.prisons = self.get_all_prisons()

    def get_all_prisons(self):
        prisons = []
        for row in self.map:
            for grid in row:
                if grid.entity == 'P':
                    prisons.append((grid.row, grid.col))
        return prisons

    def make_map(self, W, H, detailed_map):
        grids = []
        for i in range(H):
            grids.append([])
            for j in range(W):
                grids[i].append(
                    layout(i, j, self.grid_w, self.grid_h, detailed_map[i][j]))

        return grids

    def reset_map(self):
        for row in range(self.H):
            for col in range(self.W):
                if self.map[row][col].is_scan:
                    self.map[row][col].is_scan = False

    def draw_map(self, WIN):
        WIN.fill((255, 255, 255))

        for row in self.map:
            for grid in row:
                grid.draw(WIN, self.THEME)

        gap_row = self.grid_w
        gap_col = self.grid_h

        # number list
        for i in range(self.W):
            text = self.THEME.render(str(i), True, (0, 0, 0))
            center_rect = (gap_col*(i+1) + gap_col//2 -
                           text.get_rect().width//2, 0)
            WIN.blit(text, center_rect)

        for i in range(self.H):
            text = self.THEME.render(str(i), True, (0, 0, 0))
            center_rect = (0, gap_row*(i+1) + gap_row //
                           2 - text.get_rect().height//2)
            WIN.blit(text, center_rect)

        # Draw line
        for i in range(self.H+2):
            pygame.draw.line(WIN, (0, 0, 0), (0, i * gap_row),
                             (self.grid_w*(self.W+1), i * gap_row))
            for j in range(self.W+2):
                pygame.draw.line(WIN, (0, 0, 0), (j * gap_col, 0),
                                 (j * gap_col, self.grid_h*(self.H+1)))
