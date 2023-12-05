import time

seeds = []
maps = []
destinations1 = []
destinations2 = []
map_names = ["seed-to-soil map:\n","soil-to-fertilizer map:\n","fertilizer-to-water map:\n","water-to-light map:\n","light-to-temperature map:\n","temperature-to-humidity map:\n","humidity-to-location map:\n"]
index = 2
lowest = 999999999999999999999999

def parse_map():
  global index
  index += 1
  a_map = []
  while (True):
    try:
      line = lines[index]
    except IndexError:
      break
    index += 1
    #Thank you python for not having a 'do' block. >:(
    if (line == "\n"): break
    a_map.append(list(map(int, line.strip().split())))
  return a_map

def mapper(location, maps):
  for map in maps:
    for line in map:
      if location >= line[1] and location < line[1]+line[2]:
        location = line[0] + (location - line[1])
        break
  return location

start = time.perf_counter()
with open("D:/GitHub/Advent-Of-Code/2023/Day 05/test.txt") as f:
  lines = f.readlines()

seeds = list(map(int, lines[0].strip().split(":")[1].split())) 

for map_name in map_names:
  maps.append(parse_map())

for seed in seeds:
  location = mapper(seed, maps)
  destinations1.append(location)

print(min(destinations1))
print(min(destinations2))
end = time.perf_counter()
print(end-start)