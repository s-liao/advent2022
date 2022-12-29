import functools
class System:

    def __init__(self, filename):
        self.filename = filename
        self.left_list = []
        self.right_list = []

    def read(self):
        with open(self.filename) as f:
            lines = [line.strip() for line in f.readlines()]

        i = 0
        while i < len(lines):
            left_line = eval(lines[i])
            right_line = eval(lines[i+1])

            self.left_list.append(left_line)
            self.right_list.append(right_line)
            i += 3




    def score(self):
        sum = 0
        for i,(left,right) in enumerate(zip(self.left_list, self.right_list)):
            index = i+1
            val = self.check(left, right, 0, 0)

            if val < 0:
                sum += index
        return sum

    def score2(self):
        divider_packet1 = [[2]]
        divider_packet2 = [[6]]
        packet_list = self.left_list + self.right_list + [divider_packet1, divider_packet2]

        def compare(l, r):
            return self.check(l, r, 0, 0)

        packet_list.sort(key=functools.cmp_to_key(compare))

        index1 = packet_list.index(divider_packet1) + 1
        index2 = packet_list.index(divider_packet2) + 1

        #print('\n'.join(['%s' % v for v in packet_list]))

        return index1 * index2

    def check(self, left, right, left_index, right_index):

        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return -1
            elif left > right:
                return +1
            else:
                return 0
        elif isinstance(left, int) and isinstance(right, list):
            return self.check([left], right, left_index = 0, right_index=right_index)
        elif isinstance(left, list) and isinstance(right, int):
            return self.check(left, [right], left_index = left_index, right_index = 0)
        elif isinstance(left, list) and isinstance(right, list):
            if left_index < len(left) and right_index < len(right):
                pass
            elif left_index < len(left) and right_index >= len(right):
                return +1
            elif left_index >= len(left) and right_index < len(right):
                return -1
            elif left_index >= len(left) and right_index >= len(right):
                return 0


            val = self.check(left[left_index], right[right_index], 0, 0)

            if val == 0:
                return self.check(left, right, left_index + 1, right_index + 1)
            else:
                return val



def score(filename):
    sys = System(filename)
    sys.read()
    print(sys.score())

def score2(filename):
    sys = System(filename)
    sys.read()
    print(sys.score2())
score('sample.txt')
score('input.txt')
score2('sample.txt')
score2('input.txt')
