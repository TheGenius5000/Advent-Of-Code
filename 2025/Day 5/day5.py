import time

## Day 5 - Cafeteria
## Average runtime: ~

start_time = time.perf_counter()

with open(r"D:\GitHub\Advent-Of-Code\2025\Day 5\input.txt") as f:
  id_ranges, ids = [x.splitlines() for x in f.read().split("\n\n")]

## Part 1
# Problem: Count how many ingredient IDs are fresh. They are fresh if they fall into the ranges specified of fresh IDs.

# Solution: Brute-force - check all IDs in the available ranges.

ids = list(map(int, ids))
id_ranges = [(int((id_split := line.split("-"))[0]), int(id_split[1])) for line in id_ranges]

ans1 = 0

for id in ids:
  for id_start, id_end in id_ranges:
    if id_start <= id <= id_end:
      ans1 += 1
      break

print(f"The sum of fresh IDs is {ans1}.")

## Part 2
# Problem: 

# Solution: 


end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")