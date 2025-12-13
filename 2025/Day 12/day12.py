import time
import math

## Day 12 - 
## Average runtime: ~0.0029 seconds

start_time = time.perf_counter()

with open(r"input.txt") as f:
  lines = [x.splitlines() for x in f.read().split("\n\n")]

## Part 1
# Problem: Find the number of regions that can fit all the right combination of presents into its region.

# Solution: The problem is simpler than it sounds - check if the area of the presents is less than the area of the region given. Give the number of such occurences.

areas = [sum(x.count("#") for x in line) for line in lines[:-1]]
ans1 = 0

for line in lines[-1]:
  linep0, linep1 = line.split(":")
  region_area = math.prod(map(int, linep0.split("x")))
  if sum(present_area*present_count for present_area, present_count in zip(areas, map(int, linep1.strip().split()))) < region_area: ans1 += 1

print(f"The number of fitting regions is {ans1}.")

## Part 2
# Problem: 

# Solution: 


end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")