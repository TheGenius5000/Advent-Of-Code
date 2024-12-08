import time

start_time = time.time()

lines = [list(x) for x in open("input.txt").read().splitlines()]

antennas = dict()
anti_coords = [[], []]

for j, line in enumerate(lines):
  for i, ch in enumerate(line):
    if ch != '.':
      if ch in antennas: antennas[ch].append((i,j))
      else: antennas[ch]= [(i,j)]

for frequency, xys in antennas.items():
  for coords in [xys, list(reversed(xys))]:
    for i, (x,y) in enumerate(coords):
      for a,b in coords[i+1:]:
        anti_x = x + x-a
        anti_y = y + y-b
        anti_coords[1].append((x,y))
        anti_coords[1].append((a,b))
        if (0 <= anti_x < len(lines[0])) and (0 <= anti_y < len(lines)): 
          anti_coords[0].append((anti_x, anti_y))
        else: continue
        while True:
          if not((0 <= anti_x < len(lines[0])) and (0 <= anti_y < len(lines))): break
          anti_coords[1].append((anti_x, anti_y))
          if lines[anti_y][anti_x] == '.': lines[anti_y][anti_x] = '#'
          anti_x += x-a
          anti_y += y-b

print(len(set(anti_coords[0])))
print(len(set(anti_coords[1])))

end_time = time.time()
print(f"{end_time-start_time} seconds")