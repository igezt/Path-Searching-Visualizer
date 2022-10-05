import time

from pygame.locals import *
import sys
from BFS import *
from DFS import *
from IDS import *
from Board import *

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

global SCREEN, CLOCK



def main():
    window_height = 1000
    window_width = 700
    block_size = 20

    pygame.init()

    grid_height = int(window_height / block_size)
    grid_width = int(window_width / block_size)

    board = Board(grid_height, grid_width, block_size)
    board.populate_neighbors()

    start_button = board.node(0, 0).start_button()
    wall_button = board.node(2, 0).wall_button()
    reset_button = board.node(1, 0).reset_button()
    source = board.node(3, 3).make_source()
    goal = board.node(grid_height - 1, grid_width - 1).make_goal()

    dict_of_nodes = board.dict_of_nodes
    grid = board.grid

    bfs = BFS(grid, source, dict_of_nodes)
    dfs = DFS(grid, source, dict_of_nodes)
    ids = IDS(grid, source, dict_of_nodes, 5)
    algo = ids

    run = False
    wall_mouse = True
    first_run = True

    while True:

        board.drawGrid(grid, first_run)
        pygame.display.update()

        if run:
            algo.run()
            # time.sleep(0.1)
            if first_run:
                first_run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x = mouse_pos[0] // block_size
                y = mouse_pos[1] // block_size
                if grid[x][y] == start_button:
                    run = not run
                if grid[x][y] == wall_button:
                    wall_mouse = not wall_mouse
                if grid[x][y] == reset_button:
                    for r in grid:
                        for n in r:
                            n.reset()
                    algo.reset()
                    run = False
                    first_run = True
                if first_run:
                    if x == 3 and y == 0:
                        algo = bfs
                        algo.reset()
                    if x == 4 and y == 0:
                        algo = dfs
                        algo.reset()
                    if x == 5 and y == 0:
                        algo = ids
                        algo.reset()

            if pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                x = mouse_pos[0] // block_size
                y = mouse_pos[1] // block_size
                if x >= grid_height and y >= grid_width:
                    continue
                if wall_mouse and not (5 >= x >= 2 and y == 0):
                    grid[x][y].wall()
                else:
                    grid[x][y].unwall()


if __name__ == "__main__":
    main()
