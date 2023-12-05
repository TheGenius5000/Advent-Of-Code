import time

seeds = []
maps = []
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

def mapper(location_min, location_max, maps):
  locations = []
  diff = location_max - location_min
  for i, map in enumerate(maps):
    for line in map:
      start = line[1]
      end = line[1]+line[2]
      if location_min >= start and location_min < end:
        if location_max < end:
          location_max = line[0] + (location_max - start)
          location_min = line[0] + (location_min - start)
          break
        else:
          locations += mapper(end, location_max, maps[i+1:])
          location_max = end-1
          location_max = line[0] + (location_max - start)
          location_min = line[0] + (location_min - start)
      else:
        if location_max >= start and location_max < end:
          locations += mapper(start,location_max, maps[i:])
          location_max = start-1
  locations.append(location_min)
  locations.append(location_max)
  return locations

start = time.perf_counter()
with open("input.txt") as f:
  lines = f.readlines()

seeds = list(map(int, lines[0].strip().split(":")[1].split())) 

for map_name in map_names:
  maps.append(parse_map())


for seed_start, seed_range in zip(*[iter(seeds)]*2):
  destinations2 += mapper(seed_start, seed_range+seed_start-1, maps)

print(min(destinations2))
end = time.perf_counter()
print(end-start)