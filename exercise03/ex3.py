def find_common(sack1, sack2):
    for letter in sack1:
        if letter in sack2:
            return letter

def priority(letter):
    val = ord(letter)
    if ord('A') <= val <= ord('Z'):
        return val - ord('A') + 27
    else:
        return val - ord('a') + 1
def score(filename):
    sum = 0
    with open(filename) as f:
        for text in f:
            line = text.strip()
            half_len = int(len(line)/2)
            sack1 = line[:half_len]
            sack2 = line[half_len:]
            sum += priority(find_common(sack1, sack2))

    print(sum)

def find_common3(line1, line2, line3):

    for letter in line1:
        if letter in line2 and letter in line3:
            return letter

def score2(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

        sum = 0
        for i in range(0, len(lines), 3):
            letter = find_common3(lines[i], lines[i+1], lines[i+2])
            sum += priority(letter)

        print(sum)

score('sample.txt')
score('input.txt')

score2('sample.txt')
score2('input.txt')
