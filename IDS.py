class IDS:

    def __init__(self, grid, source, dict_of_nodes: dict, depth: int = 1, reached: bool = False):
        self.grid = grid
        self.source = source
        self.stack1 = []
        self.stack2 = []
        self.reached = reached
        self.dict = dict_of_nodes
        self.goal = None
        self.depth = depth
        self.count = 0
        self.stack1.append(source)
        self.flip = True
        self.limit = depth
        self.pause = 10

    def run(self):
        if self.reached:
            self.finished()
            return

        if self.flip and len(self.stack1) == 0:
            if self.pause > 0:
                self.pause -= 1
                return
            else:
                self.flip = not self.flip
                self.limit += self.depth
                self.pause = 10
                return
        elif not self.flip and len(self.stack2) == 0:
            if self.pause > 0:
                self.pause -= 1
                return
            else:
                self.flip = not self.flip
                self.limit += self.depth
                self.pause = 10
                return

        if self.flip:
            stk1 = self.stack1
            stk2 = self.stack2
        else:
            stk1 = self.stack2
            stk2 = self.stack1

        curr = stk1.pop()

        if not curr.visited:
            curr.visit()

        if curr.is_goal:
            self.goal = curr
            self.reached = True
            return

        for n in curr.neighbors:
            if not n.is_wall and not n.visited:
                if curr.g_n >= self.limit:
                    stk2.append(n)
                else:
                    stk1.append(n)
                self.dict[n.name] += 1
                n.push(curr)

    def finished(self):
        goal = self.goal
        while goal.parent is not None:
            goal.path()
            goal = goal.parent

    def queue_print(self):
        prtr = "("
        for n in self.stack1:
            prtr += str(n.name) + ", "
        print(prtr + ")")
        prtr = "("
        for n in self.stack2:
            prtr += str(n.name) + ", "
        print(prtr + ")")

    def reset(self):
        for n in self.dict:
            self.dict[n] = 0
        self.stack1.clear()
        self.stack2.clear()
        self.flip = True
        self.stack1.append(self.source)
        self.limit = self.depth
        self.reached = False
