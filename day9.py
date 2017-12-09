with open('day9.txt') as file:
    input = file.readline()

total = 0
garbage_total = 0
depth = 0
ignore_next = False
is_garbage = False
for character in list(input):

    if ignore_next:
        ignore_next = False
        continue

    if not is_garbage:

        if character == '{':
            depth += 1
            continue

        if character == '}':
            total += depth
            depth -= 1
            continue

        if character == '<':
            is_garbage = True
            continue

    else:
        if character == '!':
            ignore_next = True
            continue

        if character == '>':
            is_garbage = False
            continue

        garbage_total += 1

print(total, garbage_total)

