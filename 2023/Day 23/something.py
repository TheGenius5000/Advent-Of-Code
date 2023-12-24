import heapq
import functools
import time

starttime = time.perf_counter()
lines = list(map(list, open("D:/GitHub/Advent-Of-Code/2023/Day 23/input.txt").read().splitlines()))

directions = {
  "W": (-1, 0),
  "E": (1, 0),
  "S": (0, 1),
  "N": (0, -1)
}

directions_index = {
  "W": 0,
  "E": 1,
  "S": 2,
  "N": 3,
}

backtracks = {
  "W": "E",
  "E": "W",
  "S": "N",
  "N": "S"
}

slopes = {
  "E": ">",
  "W": "<",
  "S": "v",
  "N": ""
}

end = (lines[-1].index("."), len(lines)-1)
start = (lines[0].index("."),0)

highest = 0
crossroads = {start: []}

def downTheHillWeGo(start, distance, current_dir, last_crossroads):
  global highest
  x, y = start
  while (x,y) != end:
    old_x = x
    old_y = y
    new_locs = []
    possible_dirs = []
    for k, (dx, dy) in directions.items():
      if k == backtracks[current_dir]: continue
      new_x = x+dx
      new_y = y+dy
      if any([new_x < 0, new_x >= len(lines[0]), new_y < 0, new_y >= len(lines)]): continue
      location = lines[new_y][new_x]
      if location not in ".<>v": continue
      new_locs.append((new_x, new_y))
      possible_dirs.append(k)
    
    if len(possible_dirs) > 1: 
      crossroads[last_crossroads].append(((x,y), distance))
      if (x,y) in crossroads: return
      crossroads[(x,y)] = [(last_crossroads, distance)]
      last_crossroads = (x,y)      
      distance = 0   
    distance += 1
    current_dir = possible_dirs.pop(0)
    x, y = new_locs.pop(0)
    for i, another_loc in enumerate(new_locs):
      downTheHillWeGo(another_loc, distance, possible_dirs[i], (old_x, old_y))

  crossroads[last_crossroads].append(((x,y), distance))
  if distance > highest: highest = distance

downTheHillWeGo(start, 0, "S", start)
print(highest)
print(crossroads)

highest = 0
paths = {start: []}

def find_highest(point, history, total):
  global highest
  if point == end:
    if total > highest: highest = total
    return
  for next_point, distance in crossroads[point]:
    if next_point in history: continue
    find_highest(next_point, tuple([x for x in history]+[next_point]), total+distance)

find_highest(start, (), 0)
print(highest)
end = time.perf_counter()
print(end-starttime)