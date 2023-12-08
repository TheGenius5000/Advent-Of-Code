import time
import math

start = time.perf_counter()
with open("input.txt") as f:
    lines = f.readlines()

directions = lines[0].strip()
lines = lines[2:]

#Key: What the location is
#Value: tuple of locations (left, right)
camel_map = {}

for line in lines:
  locations = ''.join(filter(lambda x: x.isalnum() or x.isspace(), line)).split()
  camel_map.update({locations[0]: (locations[1], locations[2])})

def z_finder(curr_location):
  iterations = 0
  while True:
    for ch in directions:
      if curr_location[2] == "Z": return iterations
      iterations += 1
      options = camel_map.get(curr_location)
      if ch == "L":
        curr_location = options[0]
      elif ch == "R":
        curr_location = options[1]

a_steps = [z_finder(key) for key in camel_map if key[2] == "A"]
print(math.lcm(*a_steps))


end = time.perf_counter()
print(end-start)