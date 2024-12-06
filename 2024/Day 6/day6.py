lines = [list(x) for x in open("D:\\GitHub\\Advent-Of-Code\\2024\\Day 6\\input.txt").read().splitlines()]

def move(x, y, amount, orientation):
  if orientation == 0:
    y -= amount
  elif orientation == 90:
    x += amount
  elif orientation == 180:
    y += amount
  elif orientation == 270:
    x -= amount
  return (x, y)


guard_y = lines.index([x for x in lines if '^' in x][0])
guard_x = lines[guard_y].index('^')
orientation = 0
visited = set([(guard_x, guard_y)])
ignore_rotations = 0

guard_visited_places = [((guard_x, guard_y), orientation)]

turning_points = {k: [] for k in [0,90,180,270]}

while (0 <= guard_y < len(lines)) and (0 <= guard_x < len(lines[0])):
  guard_x, guard_y = move(guard_x, guard_y, 1, orientation)
  if not ((0 <= guard_y < len(lines)) and (0 <= guard_x < len(lines[0]))): 
    guard_x, guard_y = move(guard_x, guard_y, -1, orientation)
    break
  if lines[guard_y][guard_x] == '#':
    guard_x, guard_y = move(guard_x, guard_y, -1, orientation)
    lines[guard_y][guard_x] = '+'
    orientation = (orientation + 90) % 360
    turning_points[orientation].append((guard_x, guard_y))
    guard_visited_places.append(((guard_x, guard_y), orientation))
    ignore_rotations += 1
    continue
  guard_visited_places.append(((guard_x, guard_y), orientation))
  visited.add((guard_x, guard_y))

# for x, y, orientation in ignore:
#   guard_visited_places[(x,y)].pop(guard_visited_places[(x,y)].index(orientation))

obstacles_to_add = []
total = 0

for i, ((x,y), orientation) in enumerate(guard_visited_places):
  obs_x, obs_y = move(x,y,1,orientation)
  if not(all([0 <= obs_y < len(lines), 0 <= obs_x < len(lines[0])])): continue
  if (obs_x, obs_y) in obstacles_to_add: continue
  if lines[obs_y][obs_x] in '#^': continue
  if any([(obs_x, obs_y) == visited_place[0] for visited_place in guard_visited_places[:i]]): continue
  orientation = (orientation+90) % 360
  traversed_coords = [(x,y,orientation)]
  while True:
    x,y = move(x,y,1,orientation)
    if not((0 <= y < len(lines)) and (0 <= x < len(lines[0]))): break
    if lines[y][x] == '#' or (x,y) == (obs_x,obs_y): 
      x,y = move(x,y,-1,orientation)
      orientation = (orientation+90) % 360
    if (x,y,orientation) in traversed_coords:
      lines[obs_y][obs_x] = 'O'
      obstacles_to_add.append((obs_x, obs_y))
      break
    traversed_coords.append((x,y,orientation))

print(len(visited))
print(len(set(obstacles_to_add)))
pass