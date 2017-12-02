def challenge_one(input):
    items = input.split('\n')[1:-1]

    sum = 0
    for row in items:
        row = [int(digit) for digit in row.split(' ') if digit is not '']
        sum += max(row) - min(row)

    return sum

def challenge_two(input):
    items = input.split('\n')[1:-1]

    sum = 0
    for row in items:
        row = [int(digit) for digit in row.split(' ') if digit is not '']
        for i in range(0, len(row)):
            for j in range(0, len(row)):
                if i is not j and row[i] % row[j] == 0:
                    sum += row[i] // row[j]

    return sum
