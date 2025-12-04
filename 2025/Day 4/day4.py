import time

## Day 4 - Printing Department
## Average runtime: ~0.38 seconds

start_time = time.perf_counter()

with open(r"input.txt") as f:
  lines = [list(line) for line in f.read().splitlines()]

## Part 1
# Problem: Find all the rolls of paper that can be accessed with a forklift (4 accessible positions around it)

# Solution: Iterate through the list, and check every '@' for at least four of '@' around each one. Count how many there are which are strictly under 4.

dirs = set((x,y) for x in [-1,0,1] for y in [-1,0,1])
dirs.remove((0,0))

ans1 = 0 #1st free roll count
ans2 = 0 #All possible free rolls

#Goes through a grid, marks all free rolls with an x, then returns the new grid and the count of how many there are.
def free_roll_counter(lines):
  count = 0
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
        count += 1
  return (lines, count)

#Replaces all free rolls (already marked with 'x') and replaces them with '.'. Returns the new grid and if a change is made.
def free_roll_remover(lines):
  for y, line in enumerate(lines):
    for x, ch in enumerate(line):
      if ch == 'x': 
        lines[y][x] = '.'
  return lines
 
#[print(''.join(x)) for x in lines]
lines, ans1 = free_roll_counter(lines)
#print()
#[print(''.join(x)) for x in lines]



## Part 2
# Problem: When you have found all the roles that can be removed, find the next set of rolls that can be removed. Keep doing this until you have no more rolls left remove. Give the number of rolls that can be removed overall.

# Solution: Continously iterate by removing free rolls, keeping track of the removed count, then 

remove_count = ans1
ans2 = remove_count

while remove_count != 0:
  #print(f"Remove {remove_count} free rolls of paper:")
  lines = free_roll_remover(lines)
  lines, remove_count = free_roll_counter(lines)
  ans2 += remove_count
  #[print(''.join(x)) for x in lines]
  #print()


print(f"The number of free paper rolls intially is {ans1}.")
print(f"The number of free paper rolls overall is {ans2}.")

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")