import time
import numpy as np

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
    if char in "F7JL": #Vertices
      x_coords.append(x)
      y_coords.append(y)
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

start = time.perf_counter()

with open("input.txt") as f:
  lines = [x.strip() for x in f.readlines()]

start_location = [(i, x.index("S")) for i, x in enumerate(lines) if "S" in x][0]

width = len(lines[0])
space = [list(''.ljust(width)) for x in lines]
x_coords = []
y_coords = []

#You're gonna have to give me the direction of the pipe for start here...
length = path_finder(start_location, "W")


#Shoelace formula
A = 0.5*np.abs(np.dot(x_coords, np.roll(y_coords, 1)) - np.dot(y_coords, np.roll(x_coords, 1)))
#Pick's theorem
i = A+1-length/2

print(length//2)
print(i)

end = time.perf_counter()
print(end-start)