import time

## Day 
## Average runtime: ~

start_time = time.perf_counter()

with open(r"input.txt") as f:
  lines = f.read().splitlines()

## Part 1
# Problem: Find out how many times the dial lands at exactly 0 after a series of input turns.

# Solution: Loop through them, keeping track of where the dial is, and increment a counter when the dial is at 0.

dial = 50
zero_counter = 0
for line in lines:
  direction, clicks = line[0], int(line[1:])
  if direction == "L":
    dial = (dial - clicks) % 100
  elif direction == "R":
    dial = (dial + clicks) % 100
  if dial == 0: zero_counter += 1

print(f"zero appeared {zero_counter} times.")

## Part 2
# Problem: 

# Solution: 


end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")