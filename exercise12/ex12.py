import math
class Graph:

    def __init__(self, filename):
        self.graph = []
        self.filename = filename
        self.read()

    def search2(self):
        ri,ci = self.goal_state
        self.cost_to_come[ri][ci] = 0
        self.queue = []

        ri,ci = self.goal_state
        self.queue.append((ri,ci))

        while len(self.queue) > 0:

            r,c = self.queue[0]
            del self.queue[0]

            for r2,c2 in self.get_actions2(r,c):
                if self.visited[r2][c2] == 0:
                    new_cost = self.cost_to_come[r][c] + 1
                    if new_cost < self.cost_to_come[r2][c2]:
                        self.cost_to_come[r2][c2] = new_cost
                        self.come_through[r2][c2] = (r,c)

                    self.visited[r2][c2] = 1
                    self.queue.append((r2,c2))
                    self.reorder_queue()


    def search(self):
        ri,ci = self.init_state
        self.cost_to_come[ri][ci] = 0
        self.come_through[ri][ci] = (ri,ci)
        self.queue = []

        ri,ci = self.init_state
        self.queue.append((ri,ci))

        while len(self.queue) > 0:

            r,c = self.queue[0]
            del self.queue[0]

            if (r,c) == self.goal_state:
                return

            for r2,c2 in self.get_actions(r,c):
                if self.visited[r2][c2] == 0:
                    new_cost = self.cost_to_come[r][c] + 1
                    if new_cost < self.cost_to_come[r2][c2]:
                        self.come_through[r2][c2] = (r,c)
                        self.cost_to_come[r2][c2] = new_cost

                    self.visited[r2][c2] = 1
                    self.queue.append((r2,c2))
                    self.reorder_queue()

    def reorder_queue(self):
        self.queue.sort(key = lambda state: self.cost_to_come[state[0]][state[1]])

    def read(self):
        with open(self.filename) as f:
            lines = [line.strip() for line in f.readlines()]
        for i,line in enumerate(lines):
            self.graph.append([letter for letter in line])

        self.rows = len(self.graph)
        self.cols = len(self.graph[0])
        self.find_init_state()
        self.find_goal_state()

        self.visited = []
        for r in range(self.rows):
            self.visited.append([0 for c in range(self.cols)])

        self.come_through = []
        for r in range(self.rows):
            self.come_through.append([None for c in range(self.cols)])

        self.cost_to_come = []
        for r in range(self.rows):
            self.cost_to_come.append([math.inf for c in range(self.cols)])


        #print(self.graph)

    def find_char(self, char):
        for (r,row) in enumerate(self.graph):
            for (c, column) in enumerate(row):
                if self.graph[r][c] == char:
                    return (r,c)

    def find_init_state(self):
        self.init_state = self.find_char('S')

    def find_goal_state(self):
        self.goal_state = self.find_char('E')

    def get_adjacent_states(self, r, c):
        possible_states =\
            [
                (r - 1, c), #up
                (r + 1, c), #down
                (r, c - 1), #left
                (r, c + 1), #right
            ]
        adjacent_states = []

        for (r,c) in possible_states:
            if 0 <= r < self.rows and 0 <= c < self.cols:
                adjacent_states.append((r,c))

        return adjacent_states

    def get_elevation(self, r, c):
        letter = self.graph[r][c]
        if letter == 'S':
            letter = 'a'
        elif letter == 'E':
            letter = 'z'

        return ord(letter) - ord('a')

    def get_actions2(self, r, c):
        actions = []
        current_elevation = self.get_elevation(r, c)
        for (r2, c2) in self.get_adjacent_states(r, c):
            elevation = self.get_elevation(r2, c2)
            if current_elevation <= elevation + 1:
                actions.append((r2, c2))

        return actions

    def get_actions(self, r, c):
        actions = []
        current_elevation = self.get_elevation(r, c)
        for (r2, c2) in self.get_adjacent_states(r, c):
            elevation = self.get_elevation(r2, c2)
            if elevation <= current_elevation + 1:
                actions.append((r2, c2))

        return actions

    def print_costs(self):
        str = ''
        for (r,row) in enumerate(self.graph):
            if r != 0:
                str += '\n'
            for (c,col) in enumerate(row):
                if math.isinf(self.cost_to_come[r][c]):
                    str += '[inf]'
                else:
                    str += '[%3d]' % self.cost_to_come[r][c]

        print(str)

    def print_path(self, ri, ci, rg, cg):

        path = []
        r,c = rg, cg
        while (r,c) != (ri,ci):
            path.append((r,c))
            r,c = self.come_through[r][c]

        path.append((ri,ci))
        path.reverse()

        print(path)

    def score2(self):
        lowest_cost = math.inf
        best_r = -1
        best_c = -1
        for r,row in enumerate(self.graph):
            for c,col in enumerate(row):
                if self.graph[r][c] == 'a' and 0 < self.cost_to_come[r][c] < lowest_cost:
                    lowest_cost = self.cost_to_come[r][c]

        print(lowest_cost)





def score(filename):
    graph = Graph(filename)
    graph.search()
    #graph.print_costs()
    ri,ci = graph.init_state
    rg,cg = graph.goal_state
    #graph.print_path(ri,ci, rg, cg)
    r,c = graph.goal_state
    print(graph.cost_to_come[r][c])

def score2(filename):
    graph = Graph(filename)
    graph.search2()
    #graph.print_costs()
    graph.score2()

score('sample.txt')
score('input.txt')
score2('sample.txt')
score2('input.txt')
