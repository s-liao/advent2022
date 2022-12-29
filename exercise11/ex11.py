import copy
import numpy as np
class Monkey:
    def __init__(self, start_items, operation_text, divisor, true_index, false_index):
        self.items = start_items
        self.operation_text = operation_text
        self.divisor = divisor
        self.true_index = true_index
        self.false_index = false_index

class Simulation:

    def __init__(self, print_output = 0):
        self.print_output = print_output
        self.monkeys = []
        self.inspections = []

    def read(self, filename):
        with open(filename) as f:
            lines = [line.strip() for line in f.readlines()]

        i = 0
        while i < len(lines):

            # first line: monkey (skip)
            i += 1

            # second line: items
            items = [int(token.strip()) for token in lines[i].split(':')[-1].strip().split(',')]
            i += 1

            # third line: operation Operation: new = old * 19
            operation_text = lines[i].split('=')[-1].strip()
            i += 1

            # fourth line: Test
            divisor = int(lines[i].split()[-1])
            i += 1

            # fifth line: true condition
            test1_index = int(lines[i].split()[-1])
            i += 1

            # sixth line: false condition
            test2_index = int(lines[i].split()[-1])
            i += 1

            self.monkeys.append(Monkey(
                items,
                operation_text,
                divisor,
                test1_index,
                test2_index
            ))

            # 7th line: blank
            i += 1

        for i in range(0, len(self.monkeys)):
            self.inspections.append(0)

    def run_rounds(self, num_rounds):
        for i in range(0, num_rounds):
            self.run_round()

        if self.print_output >= 1:
            for i,monkey in enumerate(self.monkeys):
                print('Monkey %d inspected items %d times.' % (i, self.inspections[i]))

        print(np.prod(sorted(self.inspections, key=lambda val:-val)[0:2]))


    def run_round(self, divide = True):
        new_items = {}
        for i,monkey in enumerate(self.monkeys):
            new_items[i] = []

        for i,monkey in enumerate(self.monkeys):
            if self.print_output >= 2:
                print('Monkey %d:' % i)

            self.inspections[i] += len(monkey.items)
            for item in monkey.items:

                new_level = int(eval(monkey.operation_text, {}, {'old':item}) / (3 if divide else 1))

                if new_level % monkey.divisor == 0:
                    new_monkey_index = monkey.true_index
                else:
                    new_monkey_index = monkey.false_index

                self.monkeys[new_monkey_index].items.append(new_level)
                #new_items[new_monkey_index].append(new_level)

                if self.print_output >= 2:
                    print('  Monkey inpects an item with a worry level of %d.' % (item))
                    print('    Worry level is changed to %d.' % eval(monkey.operation_text, {}, {'old':item}))
                    print('    Monkey gets bored with item. Worry level is %d.' % (new_level))
                    print('    Item with worry level %d is thrown to monkey %d' % (new_level, new_monkey_index))
            monkey.items = []

        #for i,monkey in enumerate(self.monkeys):
            #monkey.items = new_items[i]

        if self.print_output >= 1:
            for i, monkey in enumerate(self.monkeys):
                print('Monkey %d: %s' % (i, ', '.join(['%s' % num for num in monkey.items])))


def score(filename, print_output = 0):
    sim = Simulation(print_output=print_output)
    #sim.test()
    sim.read(filename)
    sim.run_rounds(20)

def score2(filename, print_output = 0):
    sim = Simulation(print_output=print_output)
    #sim.test()
    sim.read(filename)
    sim.run_rounds(10000)

score('sample.txt', print_output=2)
#score('input.txt')
#score2('sample.txt', print_output = 1)
