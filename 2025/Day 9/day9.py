import time
from itertools import combinations

## Day 9 - Movie Theater
## Average runtime: ~

start_time = time.perf_counter()

with open(r"input.txt") as f:
  coords = [tuple(map(int, x.split(","))) for x in f.read().splitlines()]

## Part 1
# Problem: Out of the 2d co-ordinates given that indicate red squares, which two together give the largest area?

# Solution: Permeate all the co-ordinates and keep track of the one with the largest area.

ans1 = 0
rectangles = []

for (x0, y0), (x1, y1) in combinations(coords, 2):
    current_area = (abs(x0-x1)+1)*(abs(y0-y1)+1)
    rectangles.append((current_area, ((x0, y0), (x1, y1))))

rectangles.sort(key=lambda x: x[0], reverse=True)
ans1 = rectangles[0][0]

print(f"The max square that can be made out of the red tiles is {ans1}.")

## Part 2
# Problem: Find the area of the largest rectangle you can make but with the extra restriction of it being within the bounding polygon of red tiles.

# Solution: A similar solution to above, but also with the restriction of all the corners of the rectangle existing within said polygon. You can do this by raycasting with the edges of the polygon.
#           The vertices have been pruned into edges, so that edges can be checked directly.


def bad_rectangle():
  y, (x_start, x_end) = top_line
  for i, next_edge in enumerate(vertical_edge_lookup):
    if next_edge > x_start: break
  for y_line_start, y_line_end in vertical_edges[next_edge]:
    if y_line_start <= y < y_line_end: return True 
  y, (x_start, x_end) = bottom_line
  for x in range(x_start+1, x_end):
    if x not in vertical_edges: continue
    for y_line_start, y_line_end in vertical_edges[x]:
      if y_line_start < y <= y_line_end: return True
  x, (y_start, y_end) = left_line
  for y in range(y_start+1, y_end):
    if y not in horizontal_edges: continue
    for x_line_start, x_line_end in horizontal_edges[y]:
      if x_line_start <= x < x_line_end: return True
  x, (y_start, y_end) = right_line
  for y in range(y_start+1, y_end):
    if y not in horizontal_edges: continue
    for x_line_start, x_line_end in horizontal_edges[y]:
      if x_line_start < x <= x_line_end: return True
  return False


ans2 = 0
sorted_tuple = lambda x, y: tuple(sorted((x,y)))

vertical_edges = dict()
horizontal_edges = dict()


for i, (x0, y0) in enumerate(coords):
  if x0 not in vertical_edges: vertical_edges[x0] = []
  if y0 not in horizontal_edges: horizontal_edges[y0] = []
  x1, y1 = coords[(i+1)%len(coords)]
  if x0 == x1: vertical_edges[x0].append(sorted_tuple(y0, y1))
  if y0 == y1: horizontal_edges[y0].append(sorted_tuple(x0, x1))

vertical_edge_lookup = sorted(vertical_edges.keys())
horizontal_edge_lookup = sorted(horizontal_edges.keys())

for k in vertical_edges:
  vertical_edges[k].sort(key=lambda x: x[0])
for k in horizontal_edges:
  horizontal_edges[k].sort(key=lambda x: x[0])

# vertical_edges.sort(key=lambda x: x[0])
# horizontal_edges.sort(key=lambda x: x[0])
# for i, (x, _) in enumerate(vertical_edges):
#   if x not in vertical_edge_index: 
#     vertical_edge_index[x] = i
#     break
# for i, (y, _) in enumerate(horizontal_edges):
#   if y not in horizontal_edge_index: 
#     horizontal_edge_index[y] = i
#     break

for area, ((x0, y0), (x1, y1)) in rectangles:
  #print(f"Rectangle of ({x0}, {y0}) to ({x1}, {y1}):")
  x0, x1 = sorted((x0, x1))
  y0, y1 = sorted((y0, y1))
  top_line = (y0, sorted_tuple(x0, x1))
  bottom_line = (y1, sorted_tuple(x0, x1))
  left_line = (x0, sorted_tuple(y0, y1))
  right_line = (x1, sorted_tuple(y0, y1))
  vertical_lines = [(x0, sorted_tuple(y0, y1)), (x1, sorted_tuple(y0, y1))]
  bad = bad_rectangle()
  if not bad:
    ans2 = area
    #print(f"Accepted! area: {area}")
    break
  #else: print(f"Rejected! area: {area}")

print(f"The largest area of the rectangle that fits is {ans2}.")

#Visualisation stuff
# grid = [["." for _ in range(43)] for _ in range(43)]
# for x, (y_start, y_end) in vertical_edges:
#   for y in range(y_start, y_end+1): grid[y][x] = "X"
# for y, (x_start, x_end) in horizontal_edges:
#   for x in range(x_start, x_end+1): grid[y][x] = "X"
# for (x,y) in coords:
#   grid[y][x] = "#"
# [print(''.join(line)) for line in grid]

#print(sorted_coords)

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")