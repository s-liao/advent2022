def decode_num1(char):
    return ord(char) - ord('A')

def decode_num2(char):
    return ord(char) - ord('X')

def score1(char):
    return decode_num2(char) + 1

def score2(char1, char2):
    if (decode_num1(char1) + 1) % 3 == decode_num2(char2):
        return 6 #win
    elif (decode_num2(char2) + 1) % 3 == decode_num1(char1):
        return 0 #loss
    else:
        return 3

def get_score(filename):
    with open(filename) as f:
        lines = f.readlines()

    score = 0
    for line in lines:
        char1, char2 = line.split()
        score += score1(char2) + score2(char1, char2)

    print(score)

def encode_num2(num2):
    return chr(ord('X') + num2)

def get_char2(char1, strategy):
    num1 = decode_num1(char1)
    if strategy == 'X': # lose
        num2 = (num1 + 2) % 3
    elif strategy == 'Y': #draw
        num2 = num1
    else: #win
        num2 = (num1 + 1) % 3

    return encode_num2(num2)

def get_score2(filename):
    with open(filename) as f:
        lines = f.readlines()

    score = 0
    for line in lines:
        char1, strategy = line.split()
        char2 = get_char2(char1, strategy)
        score += score1(char2) + score2(char1, char2)

    print(score)

if __name__ == '__main__':
    get_score('sample.txt')
    get_score('input.txt')
    get_score2('sample.txt')
    get_score2('input.txt')

