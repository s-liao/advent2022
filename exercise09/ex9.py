import copy
class State:

    def __init__(self, head_pos, tail_pos):
        self.head_pos = copy.deepcopy(head_pos)
        self.tail_pos = copy.deepcopy(tail_pos)
        self.num_knots = len(tail_pos)

    def copy(self):
        new_head = copy.deepcopy(self.head_pos)
        new_tail = copy.deepcopy(self.tail_pos)

        return State(new_head, new_tail)

class Sim:

    ACTION_NONE = 0
    ACTION_UP = 1
    ACTION_DOWN = 2
    ACTION_LEFT = 3
    ACTION_RIGHT = 4
    ACTION_UPLEFT = 5
    ACTION_UPRIGHT = 6
    ACTION_DOWNLEFT = 7
    ACTION_DOWNRIGHT = 8

    def __init__(self, num_knots):
        tail = []
        for i in range(0, num_knots):
            tail.append([0,0])

        self.current_state = State([0,0], tail)
        self.states = []
        self.action_list = []

    def parse_action_line(self, line):
        tokens = line.split()
        dir = tokens[0]
        quantity = int(tokens[1])

        if dir == 'U':
            action = Sim.ACTION_UP
        elif dir == 'D':
            action = Sim.ACTION_DOWN
        elif dir == 'L':
            action = Sim.ACTION_LEFT
        elif dir == 'R':
            action = Sim.ACTION_RIGHT

        for i in range(0, quantity):
            self.action_list.append(action)

    def save_state(self):
        self.states.append(self.current_state.copy())

    def perform_head_action(self, action):
        if action == Sim.ACTION_UP:
            self.current_state.head_pos[1] += 1
        elif action == Sim.ACTION_DOWN:
            self.current_state.head_pos[1] -= 1
        elif action == Sim.ACTION_LEFT:
            self.current_state.head_pos[0] -= 1
        elif action == Sim.ACTION_RIGHT:
            self.current_state.head_pos[0] += 1

    def perform_tail_action(self, index, action):
        if action == Sim.ACTION_UP:
            self.current_state.tail_pos[index][1] += 1
        elif action == Sim.ACTION_DOWN:
            self.current_state.tail_pos[index][1] -= 1
        elif action == Sim.ACTION_LEFT:
            self.current_state.tail_pos[index][0] -= 1
        elif action == Sim.ACTION_RIGHT:
            self.current_state.tail_pos[index][0] += 1
        elif action == Sim.ACTION_UPLEFT:
            self.current_state.tail_pos[index][1] += 1
            self.current_state.tail_pos[index][0] -= 1
        elif action == Sim.ACTION_UPRIGHT:
            self.current_state.tail_pos[index][1] += 1
            self.current_state.tail_pos[index][0] += 1
        elif action == Sim.ACTION_DOWNLEFT:
            self.current_state.tail_pos[index][1] -= 1
            self.current_state.tail_pos[index][0] -= 1
        elif action == Sim.ACTION_DOWNRIGHT:
            self.current_state.tail_pos[index][1] -= 1
            self.current_state.tail_pos[index][0] += 1
        elif action == Sim.ACTION_NONE:
            pass
        else:
            assert(False)

    def print_state(self, state):
        max_x = max([state.head_pos[0]] + [tail[0] for tail in state.tail_pos])
        max_y = max([state.head_pos[1]] + [tail[1] for tail in state.tail_pos])

        str = ''
        for y in range(max_y, -1, -1):
            for x in range(0, max_x+1):
                if state.head_pos == [x,y]:
                    str += 'H'
                else:
                    tail_found = False
                    for i,tail in reversed(list(enumerate(state.tail_pos))):
                        if tail == [x, y]:
                            char = '%d' % (i+1)
                            tail_found = True

                    if tail_found == False:
                        if x == 0 and y == 0:
                            str += 'S'
                        else:
                            str += '.'
                    else:
                        str += char

            str += '\n'

        print(str)


    def read(self, filename, print_state=False):


        if print_state:
            print('State:---------------')
            self.print_state(self.current_state)
        self.save_state()

        with open(filename) as f:
            self.lines = [line.strip() for line in f.readlines()]

        for line in self.lines:
            self.parse_action_line(line)

        for head_action in self.action_list:
            self.perform_head_action(head_action)

            for i in range(0, self.current_state.num_knots):
                tail_action = self.determine_tail_action(i)
                self.perform_tail_action(i, tail_action)

            if print_state:
                print('State:---------------')
                self.print_state(self.current_state)
            self.save_state()

    def score(self, tail_index):
        #print([state.tail_pos for state in self.states])
        tail_list = set(tuple(state.tail_pos[tail_index]) for state in self.states)
        #print(tail_list)
        return len(tail_list)


    def determine_tail_action(self, tail_index):
        head_pos = self.current_state.head_pos if tail_index == 0 else self.current_state.tail_pos[tail_index-1]
        tail_pos = self.current_state.tail_pos[tail_index]

        dx = head_pos[0] - tail_pos[0]
        dy = head_pos[1] - tail_pos[1]
        if abs(dx) == 2 and abs(dy) == 2:
            if dx == -2 and dy == -2:
                return Sim.ACTION_DOWNLEFT
            elif dx == -2 and dy == 2:
                return Sim.ACTION_UPLEFT
            elif dx == 2 and dy == -2:
                return Sim.ACTION_DOWNRIGHT
            elif dx == 2 and dy == 2:
                return Sim.ACTION_UPRIGHT

        elif abs(dx) <= 1 and abs(dy) <= 1:
            return Sim.ACTION_NONE
        elif abs(dy) > 1:
            if dx == 0:
                return Sim.ACTION_UP if dy > 0 else Sim.ACTION_DOWN
            elif dx == 1:
                return Sim.ACTION_UPRIGHT if dy > 0 else Sim.ACTION_DOWNRIGHT
            elif dx == -1:
                return Sim.ACTION_UPLEFT if dy > 0 else Sim.ACTION_DOWNLEFT

        elif abs(dx) > 1:
            if dy == 0:
                return Sim.ACTION_RIGHT if dx > 0 else Sim.ACTION_LEFT
            elif dy == 1:
                return Sim.ACTION_UPRIGHT if dx > 0 else Sim.ACTION_UPLEFT
            elif dy == -1:
                return Sim.ACTION_DOWNRIGHT if dx > 0 else Sim.ACTION_DOWNLEFT
        else: #abs(dx) > 1 and abs(dy) > 1:
            assert(False)
        assert(False)

def score(filename):
    sim = Sim(1)
    sim.read(filename)
    print(sim.score(0))

def score2(filename):
    sim = Sim(9)
    sim.read(filename)
    print(sim.score(8))

score('sample.txt')
score('input.txt')
score2('sample.txt')
score2('input.txt')
