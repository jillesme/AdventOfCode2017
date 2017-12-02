from collections import deque

def challenge_one(input):
    que = deque([int(i) for i in str(input)])

    sum = 0
    for i in range(len(que)):
        current = que[0]
        next = que[1]
        if current == next:
            sum += current
        que.rotate(-1)

    return sum


def challenge_two(input):
    que = deque([int(i) for i in str(input)])

    sum = 0
    for i in range(len(que)):
        current = que[0]
        que.rotate(len(que) // 2)
        next = que[0]
        if current == next:
            sum += current
        que.rotate(-1 * (len(que) // 2 - 1))

    return sum

