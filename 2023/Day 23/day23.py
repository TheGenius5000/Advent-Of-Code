lines = list(map(list, open("D:/GitHub/Advent-Of-Code/2023/Day 23/test.txt").read().splitlines()))

start = (lines[0].index("."),0)
end = (lines[-1].index("."), len(lines)-1)

directions = {
  (-1,0): "W",
  (1,0): "E",
  (0,1): "S",
  (0,-1): "N"
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

highest = 0
crossroads = {start: []}
dead_ends = []


def downTheHillWeGo(start, distance, current_dir, last_crossroads):
  global highest
  x, y = start
  while (x,y) != end:
    old_x = x
    old_y = y
    new_locs = []
    possible_dirs = []
    for (dx, dy), v in directions.items():
      if v == backtracks[current_dir]: continue
      new_x = x+dx
      new_y = y+dy
      if any([new_x < 0, new_x >= len(lines[0]), new_y < 0, new_y >= len(lines)]): continue
      location = lines[new_y][new_x]
      if location not in "."+slopes[v]: continue
      new_locs.append((new_x, new_y))
      possible_dirs.append(v)
    
    if not possible_dirs: 
      dead_ends.append((x,y))
      return 
    if len(possible_dirs) > 1: 
      crossroads[last_crossroads].append(((x,y), distance))
      crossroads[(x,y)] = [(last_crossroads, distance)]
      last_crossroads = (x,y)
      #Comment out this line for part 1 to work and part 2 to break
      distance = 0 
    distance += 1
    current_dir = possible_dirs.pop(0)
    x, y = new_locs.pop(0)
    for i, another_loc in enumerate(new_locs):
      downTheHillWeGo(another_loc, distance, possible_dirs[i], (old_x, old_y))

  if distance > highest: highest = distance

downTheHillWeGo(start, 0, "S", start)
print(highest)
print(crossroads)
print(dead_ends)