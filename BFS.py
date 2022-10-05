class BFS:

    def __init__(self, grid, source, dict_of_nodes: dict, reached: bool = False):
        self.goal = None
        self.grid = grid
        self.source = source
        self.queue = []
        self.reached = reached
        self.dict = dict_of_nodes
        self.queue.append(source)

    def run(self):

        if self.reached:
            self.finished()
            return

        curr = self.queue.pop(0)
        curr.visit()
        if self.dict[curr.name] == 0:
            self.dict[curr.name] += 1

        if curr.is_goal:
            self.goal = curr
            self.reached = True
            return

        for n in curr.neighbors:
            if self.dict[n.name] == 0 and not n.is_wall:
                self.queue.append(n)
                n.push(curr)
                self.dict[n.name] += 1

    def finished(self):
        goal = self.goal
        while goal.parent is not None:
            goal.path()
            goal = goal.parent

    def reset(self):
        self.queue.clear()
        self.queue.append(self.source)
        self.reached = False
        for k in self.dict:
            self.dict[k] = 0
