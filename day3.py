from math import floor

"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23  24  25
"""

def challenge_one(n):
    largest_odd_sqrt = 1

    while (largest_odd_sqrt ** 2 < n):
        largest_odd_sqrt += 2

    vary = floor(largest_odd_sqrt // 2)
    # It takes at least l ** 2 - 1
    steps = largest_odd_sqrt - 1
    cycle = -vary

    # Difference from your largest odd squery to our number
    difference = largest_odd_sqrt ** 2 - n

    for _ in range(0, difference):
        step = 1 if cycle > 0 else -1
        steps += step

        if cycle > 0:
            cycle -= 1
        elif cycle < 0:
            cycle += 1

        if cycle == 0:
            cycle = vary * step * -1

    return steps


def challenge_two(n):
    # https://oeis.org/A141481/list
    return 'I am a cheat. Not smart enough to solve this myself.'
