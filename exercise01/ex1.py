
def main():
    max_cal = -1
    current = 0

    with open('input.txt') as f:
        lines = f.readlines()



    for i, line in enumerate(lines):
        if line.strip() == '':
            if current > max_cal:
                max_cal = current
            current = 0
        else:
            current += int(line)

        if current > max_cal:
            max_cal = current

    print(max_cal)

def main_part2():

    with open('input.txt') as f:
        lines = f.readlines()

    cal_counts = []

    current = 0
    for i, line in enumerate(lines):
        if line.strip() == '':
            cal_counts.append(current)
            current = 0
        else:
            current += int(line)
    if current > 0:
        cal_counts.append(current)

    cal_counts.sort(reverse=True)
    print(sum(cal_counts[0:3]))

if __name__ == '__main__':
    main_part2()