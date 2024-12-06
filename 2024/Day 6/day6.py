lines = open("input.txt").read().splitlines()

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

guard_visited_places = [(guard_x, guard_y)]

orientation = 0

while (0 <= guard_y < len(lines)) and (0 <= guard_x < len(lines[0])):
  guard_x, guard_y = move(guard_x, guard_y, 1, orientation)
  if not ((0 <= guard_y < len(lines)) and (0 <= guard_x < len(lines[0]))): break
  if lines[guard_y][guard_x] == '#':
    guard_x, guard_y = move(guard_x, guard_y, -1, orientation)
    orientation = (orientation + 90) % 360
  guard_visited_places.append((guard_x, guard_y))

print(len(set(guard_visited_places)))

pass