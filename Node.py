

class Node:

    def __init__(self, parent, name, state, visited: bool = False, g_n: float = 0.0, h_n: float = 0.0):
        self.parent = parent
        self.name = name
        self.state = state
        self.g_n = g_n
        self.h_n = h_n
        self.neighbors = {}
        self.visited = visited
        self.is_goal = False
        self.is_source = False
        self.is_wall = False
        self.fixed = False
        self.pushed = False

    def f_n(self):
        return self.g_n + self.h_n

    def state(self):
        return self.state

    def act(self):
        return self.act

    def parent(self):
        return self.parent

    def populate_neighbor(self, ls_of_node):
        self.neighbors = ls_of_node
        return

    def make_goal(self):
        self.state = "GREEN"
        self.is_goal = True
        self.fixed = True
        return self

    def make_source(self):
        self.state = "BLUE"
        self.is_source = True
        self.fixed = True
        return self
    
    def visit(self):
        self.visited = True
        if not self.fixed:
            self.state = "BEIGE"
        return

    def push(self, parent: "Node"):
        if not self.fixed:
            self.state = "GREY"
            self.pushed = True
            self.parent = parent
            self.g_n = parent.g_n + 1
        if self.is_goal:
            self.parent = parent
            self.pushed = True
            self.g_n = parent.g_n + 1
        return

    def path(self):
        if not self.fixed:
            self.state = "LIME"
        return

    def wall(self):
        if not self.fixed:
            if not self.is_wall:
                self.state = "RED"
                self.is_wall = True
        return
    
    def unwall(self):
        if not self.fixed:
            if self.is_wall:
                self.state = "WHITE"
                self.is_wall = False
        return

    def normal(self):
        self.state = "WHITE"
        self.is_wall = False
        self.is_source = False
        self.fixed = False
        self.is_goal = False
        self.pushed = False
        return

    def start_button(self):
        self.state = "GREY"
        self.fixed = True
        return self

    def wall_button(self):
        self.state = "RED"
        self.fixed = True
        return self
    
    def reset(self):
        if not self.fixed:
            self.state = "WHITE"
            self.is_wall = False
            self.parent = None
            self.visited = False
            self.pushed = False
        if self.is_goal:
            self.is_wall = False
            self.parent = None
            self.visited = False
            self.pushed = False
        return

    def reset_button(self):
        self.fixed = True
        self.state = "BLACK"
        return self


