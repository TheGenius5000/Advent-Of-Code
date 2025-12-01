import time

## Day 1 - Secret Entrance
## Average runtime: ~0.0025 seconds

start_time = time.perf_counter()

with open(r"input.txt") as f:
  lines = f.read().splitlines()

## Part 1
# Problem: Find out how many times the dial lands at exactly 0 after a series of input turns.

# Solution: Loop through them, keeping track of where the dial is, and increment a counter when the dial is at 0.


dial = 50
zero_counter1 = 0
zero_counter2 = 0
for line in lines:
  direction, clicks = line[0], int(line[1:])
  if direction == "L":
    new_dial = dial - clicks
  elif direction == "R":
    new_dial = dial + clicks
  if (new_dial <= 0) and (dial != 0): zero_counter2 += 1
  zero_counter2 += abs(new_dial)//100
  dial = new_dial % 100
  if dial == 0: 
    zero_counter1 += 1

print(f"zero was landed on {zero_counter1} times.")
print(f"zero appeared {zero_counter2} times.")

## Part 2
# Problem: Find out how many times dial crosses 0, including times when it didn't necessarily land on exactly

# Solution: Modify the above solution to check for lapped hundreds in between dial changes.


end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")