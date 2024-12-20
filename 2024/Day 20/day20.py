import time
import heapq

start_time = time.perf_counter()

grid = list(map(list, open(r"D:\GitHub\Advent-Of-Code\2024\Day 20\input.txt").read().splitlines()))

ans1 = 0

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

start_x, start_y = (find_the_char := lambda match: [(x,y) for y, line in enumerate(grid) for x, ch in enumerate(line) if ch in match][0])('S')
end_x, end_y = find_the_char('E')

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


## Find all skips
for y, (line, adjacancy_line) in enumerate(zip(grid, adj_matrix)):
  for x, (location, distance) in enumerate(zip(line, adjacancy_line)):
    if distance == float('inf'): continue
    for dx, dy in dirs:
      new_distance = distance
      new_x, new_y = x+dx, y+dy
      if grid[new_y][new_x] in '.SE': continue
      new_x, new_y = new_x+dx, new_y+dy
      if not all([0 <= new_x < len(line), 0 <= new_y < len(grid)]): continue
      if grid[new_y][new_x] == '#': continue
      new_distance += 2
      if not(new_distance < adj_matrix[new_y][new_x]) or adj_matrix[new_y][new_x] == float('inf'): continue
      distance_saved = adj_matrix[new_y][new_x] - new_distance
      cheats[((x,y),(new_x,new_y))] = distance_saved
      # if distance_saved not in cheats: cheats[distance_saved] = set([((x,y),(new_x, new_y))])
      # else: cheats[distance_saved].add(((x,y),(new_x, new_y)))

for cheat_skip, time_saved in cheats.items():
  if time_saved < 100: continue
  ans1 += 1

# for time_saved, cheat_skips in cheats.items():
#   if len(cheat_skips) < 100: continue
#   ans1 += len(cheat_skips)

print(ans1)

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")