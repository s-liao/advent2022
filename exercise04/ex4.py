from parse import parse

def check_contains(tuple1, tuple2):
    if tuple1[0] <= tuple2[0] and tuple1[1] >= tuple2[1]:
        return True
    else:
        return False

def check_contains2(tuple1, tuple2):
    return not(tuple1[0] > tuple2[1] or tuple1[1] < tuple2[0])

def score(filename):

    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        l1, l2, l3, l4 = map(int, parse('{}-{},{}-{}', line))
        if check_contains((l1, l2), (l3, l4)):
            #print('%d-%d contains %d-%d' % (l1,l2,l3,l4))
            sum += 1
        elif check_contains((l3, l4), (l1, l2)):
            #print('%d-%d contains %d-%d' % (l3,l4,l1,l2))
            sum += 1

    print(sum)

def score2(filename):

    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        l1, l2, l3, l4 = map(int, parse('{}-{},{}-{}', line))
        if check_contains((l1, l2), (l3, l4)):
            #print('%d-%d contains %d-%d' % (l1,l2,l3,l4))
            sum += 1
        elif check_contains((l3, l4), (l1, l2)):
            #print('%d-%d contains %d-%d' % (l3,l4,l1,l2))
            sum += 1
        elif check_contains2((l1, l2), (l3, l4)):
            sum += 1

    print(sum)

score('sample.txt')
score('input.txt')
score2('sample.txt')
score2('input.txt')
