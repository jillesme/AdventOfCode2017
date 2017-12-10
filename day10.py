from functools import reduce


def part_one():
    number_range = list(range(0, 256))
    current_position = 0
    skip_size = 0

    steps = [int(char) for char in '212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164'.split(',')]

    for step in steps:

        chunk = []
        for i in range(current_position, current_position + step):
            chunk.append(number_range[i % len(number_range)])

        for i, num in enumerate(reversed(chunk)):
            number_range[(current_position + i) % len(number_range)] = num

        current_position += step + skip_size
        skip_size += 1

    return number_range[0] * number_range[1]


def part_two():
    number_range = list(range(0, 256))
    current_position = 0
    skip_size = 0

    code_input = '212,254,178,237,2,0,1,54,167,92,117,125,255,61,159,164'
    steps = [ord(char) for char in code_input]
    steps += [17, 31, 73, 47, 23]

    for run in range(0, 64):
        for step in steps:

            chunk = []
            for i in range(current_position, current_position + step):
                chunk.append(number_range[i % len(number_range)])

            for i, num in enumerate(reversed(chunk)):
                number_range[(current_position + i) % len(number_range)] = num

            current_position += step + skip_size
            skip_size += 1

    sparse_hash = []
    for i in range(0, 16):
        n = i * 16
        sparse_hash.append(number_range[n:n+16])

    dense_hash = []
    for group in sparse_hash:
        x = 0
        for num in group:
            x ^= num
        dense_hash.append(x)

    knot = ''.join([hex(int(d))[2:].zfill(2) for d in dense_hash])

    return knot
