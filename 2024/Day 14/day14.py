import time
from math import prod
from operator import *

start_time = time.time()

lines = [[tuple(map(int, [''.join([ch for ch in part if ch.isdigit() or ch == '-']) for part in seg.split(",")])) for seg in line.split(" ")] for line in open("input.txt").read().splitlines()]

Y_SIZE = 103
X_SIZE = 101
mid_x = X_SIZE//2
mid_y = Y_SIZE//2
locs = []
safe_locs = [[],[],[],[]]
#Fml
j = 0
while(True):
  j += 1
  locs = []
  safe_locs = [[],[],[],[]]
  grid = [list('.'*X_SIZE)[:] for _ in range(Y_SIZE)]
  for bleh, ((x,y), (vec_x, vec_y)) in enumerate(lines):
    new_x = (x + vec_x) % X_SIZE
    new_y = (y + vec_y) % Y_SIZE
    locs.append((new_x, new_y))
    if not (any([new_x == mid_x, new_y == mid_y])) and j == 100:
      for i, condition in enumerate([f(new_x, mid_x) and g(new_y, mid_y) for f in [lt, gt] for g in [lt, gt]]):
        if condition: safe_locs[i].append((new_x, new_y))
    lines[bleh][0] = (new_x, new_y)
  for x,y in locs:
    grid[y][x] = '#'
  if j == 100: print(prod([len(x) for x in safe_locs]))
  if any(["##########" in ''.join(x) for x in grid]):
    for x in grid: 
      print(''.join(x))
    print(j)
    break
  
end_time = time.time()

print(f"{end_time-start_time} seconds")