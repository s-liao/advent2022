def score(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    for line in lines:
        for i in range(0, len(line)-3):
            substr = line[i:i+4]
            if len(set(substr)) == len(substr): # all unique
                print(i+4)
                break;

def score2(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    for line in lines:
        for i in range(0, len(line)-13):
            substr = line[i:i+14]
            if len(set(substr)) == len(substr): # all unique
                print(i+14)
                break;

score('sample.txt')
print('---')
score('input.txt')
print('===')
score2('sample.txt')
print('---')
score2('input.txt')
