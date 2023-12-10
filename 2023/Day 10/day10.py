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

with open("input.txt") as f:
  lines = [x.strip() for x in f.readlines()]

start_location = [(i, x.index("S")) for i, x in enumerate(lines) if "S" in x][0]

width = len(lines[0])
space = [list(''.ljust(width)) for x in lines]

#You're gonna have to give the direction of the pipe for start here...
length = path_finder(start_location, "W")

for i, xs in enumerate(space):
  for j, x in enumerate(xs):
    space[i][j] = better_pipes.get(space[i][j])

#Might need MS Paint for this one...
[print(''.join(z)) for z in space]

print(length//2)
end = time.perf_counter()
print(end-start)