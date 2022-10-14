from collections import deque

eggs = deque(map(int, input().split(', ')))
paper = deque(map(int, input().split(', ')))
box_count = 0

while True:
    egg = eggs.popleft()
    piece_of_paper = paper.pop()
    if egg == 13:
        move_to_back = paper.popleft()
        paper.appendleft(piece_of_paper)
        paper.append(move_to_back)
    elif egg <= 0:
        paper.append(piece_of_paper)
    else:
        summary = egg + piece_of_paper
        if summary <= 50:
            box_count += 1
    if len(eggs) <= 0 or len(paper) <= 0:
        break

if box_count > 0:
    print(f"Great! You filled {box_count} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if len(eggs) > 0:
    print(f"Eggs left: {', '.join(map(str, eggs))}")
if len(paper) > 0:
    print(f"Pieces of paper left: {', '.join(map(str, paper))}")
