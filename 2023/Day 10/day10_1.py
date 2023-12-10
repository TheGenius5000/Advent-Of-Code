import time
start = time.perf_counter()

better_pipes = {
  "L": "└",
  "F": "┌",
  "J": "┘",
  "7": "┐",
  " ": "%",
  "-": "─",
  "|": "│",
  "S": "S"
}


def define_direction(co_ord):
  try:
    direction = lines[co_ord[0]][co_ord[1]]
  except:
    direction = None
  return direction


def path_finder(place, orientation):
  length = 0
  x, y = place
  char = lines[x][y]
  space[x][y] = char
  while True:
    #if char == "S": break
    match orientation:
      case "S":
        place = (x+1, y)
      case "N":
        place = (x-1, y)
      case "W":
        place = (x, y-1)
      case "E":
        place = (x, y+1)
    x, y = place
    char = lines[x][y]
    space[x][y] = char
    length += 1
    match char:
      case "S":
        break
      case "L":
        orientation = "N" if orientation == "W" else "E"
      case "F":
        orientation = "S" if orientation == "W" else "E"
      case "J":
        orientation = "N" if orientation == "E" else "W"
      case "7":
        orientation = "S" if orientation == "E" else "W"
  return length

with open("D:/GitHub/Advent-Of-Code/2023/Day 10/input.txt") as f:
  lines = [x.strip() for x in f.readlines()]

start_location = [(i, x.index("S")) for i, x in enumerate(lines) if "S" in x][0]

width = len(lines[0])
space = [list(''.ljust(width)) for x in lines]

#You're gonna have to give the direction of the pipe for start here...
length = path_finder(start_location, "W")



for i, xs in enumerate(space):
  for j, x in enumerate(xs):
    if x.isspace(): space[i][j] = "."
    else: break

space = [x+["."] for x in space]

changed = False
for z in range(100):
  changed = False
  for i, xs in enumerate(space):
    for j, x in enumerate(xs):
      if x.isspace() and any([space[i-1][j] == ".", space[i+1][j] == ".", space[i][j-1] == ".", space[i][j+1] == "."]):
        changed = True
        space[i][j] = "."

for i, xs in enumerate(space):
  for j, x in enumerate(xs):
    space[i][j] = better_pipes.get(space[i][j])

[print(''.join(z)) for z in space]
print(length//2)
end = time.perf_counter()
print(end-start)