import time

## Day 5 - Cafeteria
## Average runtime: ~

start_time = time.perf_counter()

with open(r"input.txt") as f:
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

print(f"The sum of fresh IDs listed is {ans1}.")

## Part 2
# Problem: Return the number of all possible fresh ingredient IDs.

# Solution: Try and reduce the ingredient IDs into the fewest possible to remove all the overlap. Then, count the numbers in the ranges.

known_ranges = id_ranges.copy()

ans2 = 0

def attempt_right_merge(start, end, id_start, id_end):
  if (start <= id_start <= end) and (id_end >= end):
    return (start, id_end)
  
def attempt_left_merge(start, end, id_start, id_end):
  if (start <= id_end <= end) and (id_start <= start):
    return (id_start, end)

#One iteration of the list to find and remove overlaps, by merging ranges and deleting ranges. in id ranges. 
def reduce_ranges(id_ranges):
  i = 0
  reduced = False
  while i < len(id_ranges):
    merged = False
    redundant = False
    id_start, id_end = id_ranges.pop(i)
    for j, (start, end) in enumerate(id_ranges):
      if (new_range := attempt_right_merge(start, end, id_start, id_end)):
        id_ranges[j] = new_range
        merged = True
        reduced = True
        break
      elif (new_range := attempt_left_merge(start, end, id_start, id_end)):
        id_ranges[j] = new_range
        merged = True
        reduced = True
        break
      elif (start <= id_start <= end) and (start <= id_end <= end):
        redundant = True 
        reduced = True
        break
    if (not merged) and (not redundant): id_ranges.insert(i, (id_start, id_end))
    i += 1
  return (id_ranges, reduced)

reduced = True
#print(id_ranges)
while reduced:
  id_ranges, reduced = reduce_ranges(id_ranges)
  #print(id_ranges)

for id_start, id_end in id_ranges:
  ans2 += id_end-id_start+1

print(f"The sum of available fresh IDs is {ans2}.")

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")