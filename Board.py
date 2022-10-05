from Node import *
import pygame as pygame

COLORS = {"BLACK": (0, 0, 0),
          "WHITE": (255, 255, 255),
          "GREY": (127, 127, 127),
          "GREEN": (0, 255, 0),
          "RED": (255, 0, 0),
          "BLUE": (0, 0, 255),
          "YELLOW": (255, 185, 15),
          "BEIGE": (255, 250, 205),
          "LIME": (124, 252, 0)
          }


def color(c):
    return COLORS[c]


WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 700


def drawRect(x, y, border_color, fill_color, screen):
    rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
    screen.fill(fill_color, rect)
    pygame.draw.rect(screen, border_color, rect, 1)
    return rect


class Board:

    def __init__(self, grid_height, grid_width, block_size):
        grid = []

        for i in range(grid_height):
            grid.append([])
            for j in range(grid_width):
                name = (i, j)
                grid[i].append(Node(None, name, "WHITE"))
        self.grid = grid
        self.height = grid_height
        self.width = grid_width
        self.dict_of_nodes = None
        self.screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
        self.block_size = block_size

    def populate_neighbors(self):
        dict_of_nodes = {}
        h = self.height
        w = self.width
        for i in range(h):
            for j in range(w):

                ls_of_nbr = []

                if i != 0:
                    ls_of_nbr.append(self.grid[i - 1][j])

                if j != 0:
                    ls_of_nbr.append(self.grid[i][j - 1])

                if i != h - 1:
                    ls_of_nbr.append(self.grid[i + 1][j])

                if j != w - 1:
                    ls_of_nbr.append(self.grid[i][j + 1])

                dict_of_nodes[(i, j)] = 0
                self.grid[i][j].populate_neighbor(ls_of_nbr)
        self.dict_of_nodes = dict_of_nodes

    def node(self, h, w):
        return self.grid[h][w]

    def drawGrid(self, grid, first_run):
        pygame.font.init()
        bfs_text = pygame.font.SysFont('calibri', 10).render("BFS", True, COLORS["BLACK"])
        dfs_text = pygame.font.SysFont('calibri', 10).render("DFS", True, COLORS["BLACK"])
        ids_text = pygame.font.SysFont('calibri', 10).render("IDS", True, COLORS["BLACK"])
        for h in range(len(grid)):
            for w in range(len(grid[0])):
                entry = grid[h][w].state
                rect = drawRect(h, w, color("BLACK"), color(entry), self.screen)
                if first_run:
                    if h == 3 and w == 0:
                        text_rect = bfs_text.get_rect(center=rect.center)
                        self.screen.blit(bfs_text, text_rect)
                    if h == 4 and w == 0:
                        text_rect = dfs_text.get_rect(center=rect.center)
                        self.screen.blit(dfs_text, text_rect)
                    if h == 5 and w == 0:
                        text_rect = ids_text.get_rect(center=rect.center)
                        self.screen.blit(ids_text, text_rect)
