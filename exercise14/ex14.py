import functools
class System:

    M = 1000
    N = 1000

    def __init__(self, filename):
        self.filename = filename

        self.grid = []
        for r in range(self.M):
            row = ['.' for c in range(self.N)]
            self.grid.append(row)


    def read(self):
        with open(self.filename) as f:
            lines = [line.strip() for line in f.readlines()]

        for i,line in enumerate(lines):
            tokens = line.split(' -> ')

            for token in tokens:
                col,row = map(int, token.split(','))



    def score(self):
        sum = 0
        return sum

def score(filename):
    sys = System(filename)
    sys.read()
    print(sys.score())

score('sample.txt')
#score('input.txt')
