import time

start_time = time.time()

lines = [list(map(int, x)) for x in open("D:\\GitHub\\Advent-Of-Code\\2024\\Day 10\\input_easy2.txt").read().splitlines()]

dirs = {"U": [0,-1], "D": [0,1], "L": [-1,0], "R":[1,0]}
visited = set()
stack = []
#State = ((x,y), dir)
score = 0

[stack.append((x,y)) for y, line in enumerate(lines) for x, ch in enumerate(line) if ch == 0]

while stack:
  x, y = stack.pop()
  visited.add((x,y))
  if lines[y][x] == 9:
    score += 1
    continue
  for dx, dy in dirs.values():
    new_x, new_y = x+dx, y+dy
    if not(all([0 <= new_x < len(lines[0]), 0 <= new_y < len(lines)])): continue
    if lines[new_y][new_x] != lines[y][x] + 1: continue
    stack.append((new_x,new_y))

print(score)

end_time = time.time()

print(f"{end_time-start_time} seconds")