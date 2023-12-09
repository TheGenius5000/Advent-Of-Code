import time

start = time.perf_counter()
with open("input.txt") as f:
    lines = f.readlines()

directions = lines[0].strip()
lines = lines[2:]

#Key: What the location is
#Value: tuple of locations (left, right)
camel_map = {}

for line in lines:
  locations = ''.join(filter(lambda x: x.isalpha() or x.isspace(), line)).split()
  camel_map.update({locations[0]: (locations[1], locations[2])})

def zzz_finder():
  curr_location = "AAA"
  iterations = 0
  while True:
    for ch in directions:
      if curr_location == "ZZZ": return iterations
      iterations += 1
      options = camel_map.get(curr_location)
      if ch == "L":
        curr_location = options[0]
      elif ch == "R":
        curr_location = options[1]

print(zzz_finder())

end = time.perf_counter()
print(end-start)