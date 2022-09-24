import math
from collections import deque

sequence = deque(list(input().split()))
segment = deque(list())
sign = ""
current_sub_sum = 0

while len(sequence) >= 1:
    current_iteration = sequence.popleft()

    if current_iteration != '+' and current_iteration != '-' and current_iteration != '*' and current_iteration != '/':
        segment.append(int(current_iteration))

    else:
        sign = current_iteration

        if sign == "+":
            while len(segment) > 1:
                first_num = segment.popleft()
                second_num = segment.popleft()
                segment.appendleft(first_num + second_num)
            current_sub_sum = segment[0]
            sequence.appendleft(current_sub_sum)

        elif sign == "-":
            while len(segment) > 1:
                first_num = segment.popleft()
                second_num = segment.popleft()
                segment.appendleft(first_num - second_num)
            current_sub_sum = segment[0]
            sequence.appendleft(current_sub_sum)

        elif sign == "*":
            while len(segment) > 1:
                first_num = segment.popleft()
                second_num = segment.popleft()
                segment.appendleft(first_num * second_num)
            current_sub_sum = segment[0]
            sequence.appendleft(current_sub_sum)

        elif sign == "/":
            while len(segment) > 1:
                first_num = segment.popleft()
                second_num = segment.popleft()
                segment.appendleft(math.floor(first_num / second_num))
            current_sub_sum = segment[0]
            sequence.appendleft(current_sub_sum)

        segment.clear()
        current_sub_sum = 0
        if len(sequence) == 1:
            break
print(sequence[0])
