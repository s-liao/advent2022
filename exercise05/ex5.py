from parse import parse
def get_nums(lines):

    num_cols = 0;
    num_rows = 0

    # get number of columns
    for line in lines:
        if '[' not in line:
            num_cols = int(line.split()[-1])

            break;
        else:
            num_rows += 1
    return num_rows, num_cols;


def score(filename):

    with open(filename) as f:
        lines = [line.strip('\n') for line in f.readlines()]

    num_rows, num_cols = get_nums(lines)

    lines = ['%-{}s'.format(4*num_cols) % line for line in lines]

    stacks = []
    for i in range(num_cols):
        stacks.append([])

    for i in range(num_rows-1, -1, -1):
        line = lines[i]
        #print('.%s.' % line)
        for j in range(0, num_cols):
            col = line[4*j:4*(j+1)]
            #print(col)
            if col[1] != ' ':
                stacks[j].append(col[1])

    #print(stacks)

    for line in lines[num_rows + 2:]:
        tokens = line.split()

        quantity, frm, to = int(tokens[1]), int(tokens[3]), int(tokens[5])
        #print(quantity, frm, to)
        for i in range(0, quantity):
            stacks[to-1].append(stacks[frm-1].pop())

    message = ''
    for stack in stacks:
        message += stack.pop()

    print(message)


def score2(filename):

    with open(filename) as f:
        lines = [line.strip('\n') for line in f.readlines()]

    num_rows, num_cols = get_nums(lines)

    lines = ['%-{}s'.format(4*num_cols) % line for line in lines]

    stacks = []
    for i in range(num_cols):
        stacks.append([])

    for i in range(num_rows-1, -1, -1):
        line = lines[i]
        #print('.%s.' % line)
        for j in range(0, num_cols):
            col = line[4*j:4*(j+1)]
            #print(col)
            if col[1] != ' ':
                stacks[j].append(col[1])

    #print(stacks)

    for line in lines[num_rows + 2:]:
        tokens = line.split()

        quantity, frm, to = int(tokens[1]), int(tokens[3]), int(tokens[5])
        #print(quantity, frm, to)
        removed = []
        for i in range(0, quantity):
            removed.insert(0, stacks[frm-1].pop())

        for i in range(0, quantity):
            stacks[to-1].append(removed[i])

    message = ''
    for stack in stacks:
        message += stack.pop()

    print(message)

score('sample.txt')
score('input.txt')
score2('sample.txt')
score2('input.txt')
