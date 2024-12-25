import time

## Day 25: Code Chronicle
## Difficulty: Easy
## Need-to-know skills: 

## Problem: 

## Solution: 

## Average runtime: ~

start_time = time.perf_counter()

with open(r"D:\GitHub\Advent-Of-Code\2024\Day 25\input.txt") as f:
  inf = f.read().split("\n\n")

keys = []
locks = []
ans1 = 0

for schematic in inf:
  schematic = schematic.splitlines()
  key, lock = [ch not in schematic[0] for ch in '#.']
  schematic_T = list(map(list, zip(*schematic)))
  heights = []
  for line in schematic_T:
    heights.append(line.count('#')-1)
  if key: keys.append(heights)
  if lock: locks.append(heights)

del inf

for key_heights in keys:
  for lock_heights in locks:
    #print(key_heights, lock_heights, end=" ")
    if all(x+y < 6 for x,y in zip(key_heights, lock_heights)): ans1 += 1

def get_heights(schematic):
  return [line.count('#')-1 for line in [*zip(*schematic)]]

def heights_creator(inf, delim):
  return [get_heights(schematic.splitlines()) for schematic in inf if delim not in schematic[0]]

def get_ans1(key_heights, lock_heights):
  return sum(all(x+y < 6 for x,y in zip(key_heights, lock_heights)) for key_heights in keys for lock_heights in locks)

key_heights = heights_creator((inf := open(r"D:\GitHub\Advent-Of-Code\2024\Day 25\input.txt").read().split("\n\n")), '#')
lock_heights = heights_creator(inf, '.')
del key_heights
del lock_heights

print(ans1)
print((lambda key_heights, lock_heights: sum(all(x+y < 6 for x,y in zip(key_heights, lock_heights)) for key_heights in keys for lock_heights in locks))((heights_creator := lambda inf, delim: [(lambda schematic: [line.count('#')-1 for line in [*zip(*schematic)]])(schematic.splitlines()) for schematic in inf if delim not in schematic[0]])((inf := open(r"input.txt").read().split("\n\n")), '#'), heights_creator(inf, '.')))

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")