import time
import heapq

start_time = time.perf_counter()

X_SIZE, Y_SIZE = 71,71
HAS_FALLEN_ALREADY = 1024

corrupted_coords = [tuple(map(int, (x.split(",")))) for x in open(r"input.txt").read().splitlines()]

directions = [(0,1), (0,-1), (-1,0), (1,0)]

grid = [['.' for _ in range(X_SIZE)] for _ in range(Y_SIZE)]

for x,y in corrupted_coords[:HAS_FALLEN_ALREADY]:
  grid[y][x] = '#'

adj_matrix = [[999 for _ in range(X_SIZE)] for _ in range(Y_SIZE)]

start = (0,0)
x,y = start
adj_matrix[y][x] = 0
exit = (X_SIZE-1, Y_SIZE-1)

queue = [(0, start)]

while queue:
  dist, (x,y) = heapq.heappop(queue)
  dist += 1
  for dx, dy in directions:
    new_x, new_y = x+dx, y+dy
    if not all([0 <= new_x < X_SIZE, 0 <= new_y < Y_SIZE]): continue
    if not all([dist < adj_matrix[new_y][new_x], grid[new_y][new_x] != '#']): continue
    adj_matrix[new_y][new_x] = dist
    heapq.heappush(queue, (dist, (new_x,new_y)))

print(adj_matrix[exit[1]][exit[0]])

is_now_falling = HAS_FALLEN_ALREADY
prev_visited = set()

while True:
  corrupted_x, corrupted_y = corrupted_coords[is_now_falling]
  grid[corrupted_y][corrupted_x] = '#'
  is_now_falling += 1
  x,y = start
  queue = set([start])
  visited = set()
  while queue:
    x,y = queue.pop()
    for dx, dy in directions:
      new_x, new_y = x+dx, y+dy
      if not all([0 <= new_x < X_SIZE, 0 <= new_y < Y_SIZE]): continue
      if any([(new_x, new_y) in visited, grid[new_y][new_x] == '#']): continue
      visited.add((new_x, new_y))
      queue.add((new_x,new_y))
  if exit not in visited: 
    break
  prev_visited = visited.copy()

print(f"{corrupted_x},{corrupted_y}")

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")