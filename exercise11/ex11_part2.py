import copy
import numpy as np
import math

class Value:
    def __init__(self, starting_value, monkeys):
        self.starting_value = starting_value
        self.monkeys = monkeys
        self.operation_list = []
        self.remainder_results = []


    def init_remainder_results(self):
        for i in range(0, len(self.monkeys)):
            self.remainder_results.append(self.starting_value % self.monkeys[i].divisor)

    def add_operation(self, monkey_index):
        monkey = self.monkeys[monkey_index]
        self.operation_list.append(monkey_index)

        for i,val in enumerate(self.remainder_results):

            if monkey.operation_type == Monkey.OPERATION_SQUARE:
                self.remainder_results[i] *= val % self.monkeys[i].divisor
            elif monkey.operation_type == Monkey.OPERATION_PRODUCT:
                self.remainder_results[i] *= monkey.operand % self.monkeys[i].divisor
            elif monkey.operation_type == Monkey.OPERATION_SUM:
                self.remainder_results[i] += monkey.operand % self.monkeys[i].divisor
            self.remainder_results[i] = self.remainder_results[i] % self.monkeys[i].divisor

    def check_remainder2(self, monkey_index):
        return self.remainder_results[monkey_index] == 0

    def check_remainder(self, divisor):

        value = self.starting_value % divisor

        for operation in self.operation_list:
            monkey = self.monkeys[operation]

            if monkey.operation_type == Monkey.OPERATION_SQUARE:
                value *= value % divisor
            elif monkey.operation_type == Monkey.OPERATION_PRODUCT:
                value *= monkey.operand % divisor
            elif monkey.operation_type == Monkey.OPERATION_SUM:
                value += monkey.operand % divisor
                value = value % divisor

        return value % divisor == 0


class Monkey:
    OPERATION_SUM = 1
    OPERATION_PRODUCT = 2
    OPERATION_SQUARE = 3

    def __init__(self, start_items, operation_type, operand, divisor, true_index, false_index):
        self.items = start_items
        self.operation_type = operation_type
        self.operand = operand
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
            items = [Value(starting_value=int(token.strip()), monkeys=self.monkeys) for token in lines[i].split(':')[-1].strip().split(',')]
            i += 1

            # third line: operation Operation: new = old * 19
            operation_text = lines[i].split('=')[-1].strip()
            tokens = operation_text.split()

            if tokens[1] == '+':
                operation_type = Monkey.OPERATION_SUM
                operand = int(tokens[-1])
            else:# tokens[1] == '*':
                if tokens[2] == 'old':
                    operation_type = Monkey.OPERATION_SQUARE
                    operand = 0
                else:
                    operation_type = Monkey.OPERATION_PRODUCT
                    operand = int(tokens[-1])

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
                start_items = items,
                operation_type = operation_type,
                operand = operand,
                divisor = divisor,
                true_index = test1_index,
                false_index = test2_index
            ))

            # 7th line: blank
            i += 1

        for i in range(0, len(self.monkeys)):
            self.inspections.append(0)

        for i in range(0, len(self.monkeys)):
            for value in self.monkeys[i].items:
                value.init_remainder_results()

    def run_rounds(self, num_rounds):
        for i in range(0, num_rounds):
            #print(i)
            self.run_round(i)

        if self.print_output >= 1:
            for i,monkey in enumerate(self.monkeys):
                print('Monkey %d inspected items %d times.' % (i, self.inspections[i]))
        sorted_array = sorted(self.inspections, key=lambda val: -val)
        print(sorted_array[0] * sorted_array[1])


    def run_round(self, round_index):

        for i,monkey in enumerate(self.monkeys):
            if self.print_output >= 2:
                print('Monkey %d:' % i)

            self.inspections[i] += len(monkey.items)
            for value in monkey.items:

                value.add_operation(i)
                #value.operation_list.append(i)

                #if value.check_remainder(monkey.divisor):
                if value.check_remainder2(i):
                        new_monkey_index = monkey.true_index
                else:
                    new_monkey_index = monkey.false_index

                self.monkeys[new_monkey_index].items.append(value)

            monkey.items = []


def score2(filename, print_output = 0):
    sim = Simulation(print_output=print_output)
    #sim.test()
    sim.read(filename)
    sim.run_rounds(10000)

#score('sample.txt', print_output=1)
#score('input.txt')
score2('sample.txt', 1)
score2('input.txt', 1)
