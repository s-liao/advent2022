import math
class CPU:

    def __init__(self):
        self.register = {'X':1}
        self.cycles = 0

        self.cpu_record = []

    def addx(self, V):
        self.cycles += 2
        self.register['X'] += V

    def noop(self):
        self.cycles += 1

    def add_record(self):
        self.cpu_record.append({'X':self.register['X'], 'cycles':self.cycles})

    def read(self, filename):
        with open(filename) as f:
            lines = [line.strip() for line in f.readlines()]

        self.add_record()

        for line in lines:
            tokens = line.split()

            if tokens[0] == 'noop':
                self.noop()
            elif tokens[0] == 'addx':
                self.addx(int(tokens[1]))
            self.add_record()


    def signal_strength(self, cycle_num):

        # during nth cycle is the register value after n-1 cycles completed
        register_value = 0
        for record in self.cpu_record:
            if record['cycles'] < cycle_num:
                register_value = record['X']
            else:
                break;

        return cycle_num * register_value

    def score(self):
        n = math.floor((max([self.cycles, 220]) - 20) / 40)

        total = 0
        for i in range(0, n+1):
            cycle_num = 20 + 40*i
            val = self.signal_strength(cycle_num)
            total += val

        #total = sum([self.signal_strength(20 + 40*i) for i in range(0, n+1)])
        print(total)

    def get_sprite_position(self, cycle_num):
        # during nth cycle is the register value after n-1 cycles completed
        register_value = 0
        for record in self.cpu_record:
            if record['cycles'] < cycle_num:
                register_value = record['X']
            else:
                break;

        return register_value

    def render(self):
        str = ''
        for cycle_num in range(1, 241):
            sprite_pos = self.get_sprite_position(cycle_num)
            i = cycle_num - 1
            r = int(math.floor(i / 40.0))
            c = i % 40

            if abs(c - sprite_pos) <= 1:
                str += '#'
            else:
                str += '.'

            if c == 39:
                str += '\n'

        print(str);


def score(filename):
    cpu = CPU()
    cpu.read(filename)
    cpu.score()

def score2(filename):
    cpu = CPU()
    cpu.read(filename)
    cpu.render()

score('sample.txt')
score('input.txt')
score2('sample.txt')
score2('input.txt')
