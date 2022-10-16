from collections import deque

eggs = deque([int(x) for x in input().split(", ")])  # first
papers = deque([int(x) for x in input().split(", ")])  # last
box = 50
filled_boxes = 0


while eggs and papers:
    current_egg = eggs.popleft()
    if current_egg <= 0:
        continue
    if current_egg == 13:
        last_paper = papers.pop()
        first_paper = papers.popleft()
        papers.append(first_paper)
        papers.appendleft(last_paper)
        continue
    current_paper = papers.pop()
    if current_egg + current_paper <= box:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print("Eggs left: ", end="")
    print(", ".join(str(x) for x in eggs))

if papers:
    print("Pieces of paper left: ", end="")
    print(", ".join(str(x) for x in papers))