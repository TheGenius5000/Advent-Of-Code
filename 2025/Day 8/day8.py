import time
import math
import copy

## Day 8 - Playground
## Average runtime: ~2.05 seconds

start_time = time.perf_counter()

with open(r"D:\GitHub\Advent-Of-Code\2025\Day 8\input.txt") as f:
  lines = [list(map(int, line.split(","))) for line in f.read().splitlines()]


## Part 1
# Problem: Multiply the sizes of the three circuits together, after making 1000 of the smallest connection with 3d junction boxes.

# Solution: Make connections via keeping track of the sets of each circuit. Find the biggest sets and multiply their lengths.


possible_connections = sorted({(math.dist(coords0, coords1), (tuple(coords0), tuple(coords1))) for (i, coords0) in enumerate(lines) for coords1 in lines[i+1:]}, key= lambda x: x[0])

circuits = [{tuple(x)} for x in lines]

iterations = 0

while len(circuits) > 1:
  iterations += 1
  if iterations == 1000: ans1_circuits = copy.deepcopy(circuits)
  shortest_connection = possible_connections.pop(0)
  dist, (coords0, coords1) = shortest_connection
  current_circuit = circuits.pop(next(i for i, circuit in enumerate(circuits) if coords0 in circuit))
  if coords1 in current_circuit:
    circuits.append(current_circuit)
    continue
  merge_circuit = circuits.pop(next(i for i, circuit in enumerate(circuits) if coords1 in circuit))
  current_circuit |= merge_circuit
  circuits.append(current_circuit)
  


ans1_circuits = sorted(ans1_circuits, key=len, reverse=True)[:3]
ans1 = math.prod(map(len, ans1_circuits[:3]))
ans2 = coords0[0]*coords1[0]

print(f"The product of the sizes of the 3 largest circuits are {ans1}.")
print(f"The product of the final circuit-merging connection is {ans2}.")

## Part 2
# Problem: What is the multiplication of the X coordinates for the first two boxes that connect to form one single circuit for all boxes?

# Solution: Modify the above solution to carry on until the list of circuits is 1. You have the last connection left over from the loop, so times the X coords together.


end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")