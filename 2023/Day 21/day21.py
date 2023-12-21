import numpy as np

lines = open("D:/GitHub/Advent-Of-Code/2023/Day 21/input.txt").read().splitlines()
print(lines)
start = [(x,y) for x in range(len(lines[0])) for y in range(len(lines)) if lines[y][x] == "S"][0]

even_steps = set([(start,0)])
odd_steps = set([])

def make_steps(full_list, empty_list):
  while full_list:
    step_start, step_count = full_list.pop()
    x, y = step_start
    for dir_x, dir_y in [(0,-1), (0,1), (1,0), (-1,0)]:
      new_x = x+dir_x
      new_y = y+dir_y
      try:
        if lines[new_y][new_x] == '#':
          continue
      except:
        continue
      empty_list.add(((new_x, new_y), step_count+1))

for x in range(32):
  make_steps(even_steps, odd_steps)
  make_steps(odd_steps, even_steps)


print(len(set(even_steps)))