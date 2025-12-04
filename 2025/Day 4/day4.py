import time

## Day 4 - Printing Department
## Average runtime: ~

start_time = time.perf_counter()

with open(r"input.txt") as f:
  lines = [list(line) for line in f.read().splitlines()]

## Part 1
# Problem: Find all the rolls of paper that can be accessed with a forklift (4 accessible positions around it)

# Solution: Iterate through the list, and check every '@' for at least four of '@' around each one. Count how many there are which are strictly under 4.

dirs = set((x,y) for x in [-1,0,1] for y in [-1,0,1])
dirs.remove((0,0))

for x in lines:
  print(''.join(x))

ans1 = 0

for y, line in enumerate(lines):
  for x, ch in enumerate(line):
    if ch == '.': continue
    adj_rolls = 0
    for d_x, d_y in dirs:
      new_x, new_y = x+d_x, y+d_y
      if any([new_x<0, new_y<0, new_x>=len(line), new_y>=len(lines)]): continue
      elif lines[new_y][new_x] in '@x':
        adj_rolls += 1
      if adj_rolls >= 4: break
    if adj_rolls < 4:
      lines[y][x] = 'x'
      ans1 += 1
 
for x in lines:
  print(''.join(x))
print(f"The number of free paper rolls is {ans1}.")

## Part 2
# Problem: 

# Solution: 


end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")