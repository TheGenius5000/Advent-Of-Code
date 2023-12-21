import numpy as np
import time
import functools

lines = open("D:/GitHub/Advent-Of-Code/2023/Day 21/input.txt").read().splitlines()
print(lines)

start = [(x,y) for x in range(len(lines[0])) for y in range(len(lines)) if lines[y][x] == "S"][0]
x_size = len(lines[0])
y_size = len(lines)



def make_steps(full_list):
  empty_list = set()
  while full_list:
    x, y = full_list.pop()
    for dir_x, dir_y in [(0,-1), (0,1), (1,0), (-1,0)]:
      new_x = x+dir_x
      new_y = y+dir_y
      if find_deltas(new_x % x_size, new_y % y_size):
        empty_list.add((new_x, new_y))
  return empty_list

@functools.cache
def find_deltas(x_coord, y_coord):
  try:
    if lines[y_coord][x_coord] == '#':
      return False
  except:
    return False
  return True

for x in range(65, 1000, 131):
  starttime = time.perf_counter()
  steps = set([start])
  print(f"{x},", end=" ")
  for _ in range(x):
    steps = make_steps(steps)
  print(len(set(steps)))
  endtime = time.perf_counter()
  #print(f"Time: {endtime-starttime}")
