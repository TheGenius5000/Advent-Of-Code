import time

start_time = time.time()

lines = [list(x) for x in open("input.txt").read().splitlines()]

not_visited = set([(x,y) for y, line in enumerate(lines) for x, _ in enumerate(line)])
garden_plots = dict()
total = 0
total2 = 0

stack = []
ds = [(0,-1),(1,0), (0,1), (-1,0)]
while not_visited:
  if (new_region := not stack): 
    stack = [not_visited.pop()]
  x, y = stack.pop()
  plant = lines[y][x]
  if new_region:
    if plant not in garden_plots: garden_plots[plant] = [set([(x,y)])]
    else: garden_plots[plant].append(set([(x,y)]))
  for dx, dy in ds:
    new_x, new_y = x+dx, y+dy
    if not(all([0 <= new_x < len(lines[0]), 0 <= new_y < len(lines), (new_x, new_y) in not_visited])): continue
    if lines[new_y][new_x] != plant: continue
    garden_plots[plant][-1].add((coords := (new_x,new_y)))
    stack.append(coords)
    not_visited.remove(coords)

for plots in garden_plots.values():
  for plot in plots:
    perimeter = [1 for x,y in plot for dx,dy in ds if (x+dx, y+dy) not in plot]
    total += len(plot)*len(perimeter)
    #Corners are sides
    corners = [1 for x,y in plot for dir, vec_y in [("N", -1), ("S",1)] for adj_dir, vec_x in [("W", -1), ("E", 1)] if ((border_exists := {dir: (x+dx,y+dy) not in plot for dir, (dx,dy) in zip(["N","E","S","W"], ds)})[adj_dir] and border_exists[dir]) or all([not(border_exists[dir]), not(border_exists[adj_dir]), (x+vec_x, y+vec_y) not in plot])]
    total2 += len(corners)*len(plot)

print(total)
print(total2)

end_time = time.time()

print(f"{end_time-start_time} seconds")