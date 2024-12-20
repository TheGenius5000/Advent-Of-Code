import time
import heapq

## Day 20: Race Condition
## Difficulty: Hard
## Need-to-know skills: Dijkstra, Flood-fill

## Problem:  A race on a 2d grid where you are given one cheat to ignore boundaries for 2 squares.
##           Part 1: Count the number of cheats that save at least 100 distance.
##           Part 2: You can use the one cheat to ignore boundaries for up to 20 squares.
##                   Count the number of cheats that save at least 100 distance.

## Solution: Part 1: First, Dijkstra's algorithm to get all the distances for the reachable squares ('.' or 'S' or 'E') from start ('S'). 
##           Then, Flood-fill from the start of the cheat position towards any reachable end 2 squares away, ignoring boundaries.
##           Part 2: This again but for squares up to 20 squares away.

## Average runtime: ~5.7 seconds


start_time = time.perf_counter()

grid = list(map(list, open(r"input.txt").read().splitlines()))

ans1 = 0
ans2 = 0

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

start_x, start_y = (find_the_char := lambda match: [(x,y) for y, line in enumerate(grid) for x, ch in enumerate(line) if ch in match][0])('S')

adj_matrix = [[float('inf') for _ in line] for line in grid]
adj_matrix[start_y][start_x] = 0

cheats = dict()

## Reverse dijkstra
queue = [(0, (start_x, start_y))]
while queue:
  distance, (x,y) = heapq.heappop(queue)
  for dx, dy in dirs:
    new_x, new_y = x+dx, y+dy
    new_distance = distance + 1
    if any([grid[new_y][new_x] == '#', new_distance >= adj_matrix[new_y][new_x]]): continue
    adj_matrix[new_y][new_x] = new_distance
    heapq.heappush(queue, (new_distance, (new_x, new_y)))

## Flood-fill
for y, (line, adjacancy_line) in enumerate(zip(grid, adj_matrix)):
  for x, (location, distance) in enumerate(zip(line, adjacancy_line)):
    if location == '#': continue
    start = (x,y)
    for delta_x in range(-20,21):
      for delta_y in range(-20,21):
        if (delta_distance := abs(delta_x) + abs(delta_y)) > 20: continue
        new_x, new_y = x+delta_x, y+delta_y
        if not all([0 <= new_x < len(line), 0 <= new_y < len(grid)]): continue
        if grid[new_y][new_x] == '#': continue
        new_distance = distance + delta_distance
        if not(new_distance < adj_matrix[new_y][new_x]) or adj_matrix[new_y][new_x] == float('inf'): continue
        distance_saved = adj_matrix[new_y][new_x] - new_distance
        cheats[(start, (new_x, new_y))] = distance_saved

for ((from_x, from_y), (to_x, to_y)), time_saved in cheats.items():
  if time_saved < 100: continue
  ans2 += 1
  if abs(from_x - to_x) + abs(from_y - to_y) == 2: ans1 += 1

print(ans1)
print(ans2)

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")