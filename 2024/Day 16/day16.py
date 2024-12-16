import time
import heapq
from copy import deepcopy

start_time = time.time()

def moveAround(queue, matrix, end_goal):
  global grid
  while queue:
    score, (x,y,facing_dir) = heapq.heappop(queue)
    if grid[y][x] == end_goal: continue
    for dir_change in [0, 90, -90]:
      next_dir = (facing_dir+dir_change)%360
      vec_x, vec_y = directions_dict[next_dir]
      new_x, new_y = x+vec_x, y+vec_y
      if grid[new_y][new_x] == '#': continue
      new_score = score+1001 if next_dir != facing_dir else score+1
      if new_score < matrix[new_y][new_x][next_dir]:
        matrix[new_y][new_x][next_dir] = new_score
        heapq.heappush(queue, (new_score, (new_x, new_y, next_dir)))

grid = [list(x) for x in open("input.txt").read().splitlines()]

adj_matrix = [[{angle: 99999 for angle in [0,90,180,270]} for ch in line] for line in grid]
adj_matrix_end = deepcopy(adj_matrix)
seats = set()

directions_dict = {k: v for k, v in zip([270, 90, 0, 180], [(-1,0), (1,0), (0,-1), (0,1)])}

start = [(i,j,90) for j, line in enumerate(grid) for i, ch in enumerate(line) if ch == 'S'][0]
end_x, end_y = [(i,j) for j, line in enumerate(grid) for i, ch in enumerate(line) if ch == 'E'][0]
start_x,start_y,_ = start

for angle in range(0, 360, 90):
  adj_matrix[start_y][start_x][angle] = 0
  adj_matrix_end[end_y][end_x][angle] = 0

queue = [(0, start)]

moveAround(queue, adj_matrix, 'E')

ans1 = min(adj_matrix[end_y][end_x].values())
print(ans1)

queue = [(0, (end_x, end_y,angle)) for angle in directions_dict.keys()]
moveAround(queue, adj_matrix_end, 'S')

for (y, ys) in enumerate(adj_matrix):
  for (x, dirs) in enumerate(ys):
    for from_angle, from_score in dirs.items():
      for to_angle, to_score in adj_matrix_end[y][x].items():
        if (to_angle == (from_angle+180)%360 and from_score+to_score <= ans1) or (any([to_angle == (from_angle+turn)%360 for turn in (90,-90)]) and from_score+to_score <= ans1-1000):
          seats.add((x,y))

for x,y in seats:
  grid[y][x] = 'O'

print(len(seats))

end_time = time.time()

print(f"{end_time-start_time} seconds")