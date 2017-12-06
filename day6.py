input = '5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6'

def challenge_one(input):
    memory = [int(n) for n in input.split('\t')]
    track = []
    steps = 0
    while (memory not in track):
        steps += 1
        track.append(memory[:])

        highest_index = memory.index(max(memory))
        highest_memory = memory[highest_index]

        # Set highest to 0
        memory[highest_index] -= highest_memory

        # Loop over the rest
        for n in range(1, highest_memory + 1):
            memory[(highest_index + n) % len(memory)] += 1

    return steps


def challenge_two(input):
    memory = [int(n) for n in input.split('\t')]
    track = []
    steps = 0
    while (memory not in track):
        steps += 1
        track.append(memory[:])

        highest_index = memory.index(max(memory))
        highest_memory = memory[highest_index]

        # Set highest to 0
        memory[highest_index] -= highest_memory

        # Loop over the rest
        for n in range(1, highest_memory + 1):
            memory[(highest_index + n) % len(memory)] += 1

    # Return difference between two
    return len(track) - track.index(memory)
