class DFS:

    def __init__(self, grid, source, dict_of_nodes, reached: bool = False):
        self.grid = grid
        self.source = source
        self.stack = []
        self.reached = reached
        self.dict = dict_of_nodes
        self.stack.append(source)
        self.goal = None

    def run(self):

        if self.reached:
            self.finished()
            return

        curr = self.stack.pop(len(self.stack) - 1)
        curr.visit()
        if self.dict[curr.name] == 0:
            self.dict[curr.name] += 1
        if not curr.visited:
            curr.visit()
        
        if curr.is_goal:
            self.goal = curr
            self.reached = True
            return

        for n in curr.neighbors: 
            if not n.is_wall and not n.visited:
                self.dict[n.name] += 1
                self.stack.append(n)
                n.push(curr)
                self.dict[n.name] += 1

    def finished(self):
        goal = self.goal
        while goal.parent is not None:
            goal.path()
            goal = goal.parent
    
    def reset(self):
        for n in self.dict:
            self.dict[n] = 0
        self.stack.clear()
        self.stack.append(self.source)
        self.reached = False
        return

