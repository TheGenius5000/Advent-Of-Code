import time
import math

## Day 8 - Playground
## Average runtime: ~

start_time = time.perf_counter()

with open(r"D:\GitHub\Advent-Of-Code\2025\Day 8\input.txt") as f:
  lines = [list(map(int, line.split(","))) for line in f.read().splitlines()]


## Part 1
# Problem: Multiply the sizes of the three circuits together, after making 1000 of the smallest connection with 3d junction boxes.

# Solution: Make connections via keeping track of the sets of each circuit. Find the biggest sets and multiply their lengths.


possible_connections = sorted({(math.dist(coords0, coords1), (tuple(coords0), tuple(coords1))) for (i, coords0) in enumerate(lines) for coords1 in lines[i+1:]}, key= lambda x: x[0])

circuits = [{tuple(x)} for x in lines]

for _ in range(1000):
  shortest_connection = possible_connections.pop(0)
  dist, (coords0, coords1) = shortest_connection
  for i, circuit in enumerate(circuits):
    if coords0 in circuit:
      current_circuit = circuits.pop(i)
      break
  for i, circuit in enumerate(circuits):
    if coords1 in circuit:
      merge_circuit = circuits.pop(i)
      break
  else:
    merge_circuit = set()
  current_circuit |= merge_circuit
  circuits.append(current_circuit)

circuits = sorted(circuits, key=len)
circuits.reverse()

for circuit in circuits:
  print(circuit)

ans1 = math.prod(map(len, circuits[:3]))

print(f"The product of the sizes of the 3 largest circuits are {ans1}.")

## Part 2
# Problem: 

# Solution: 


end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")