import time
start = time.perf_counter()
universe = [x.strip() for x in open("input.txt").readlines()]
empty_columns = [j for j in range(len(universe[0])) if '#' not in [linecheck[j] for linecheck in universe]]
empty_rows = [i for i, line in enumerate(universe) if '#' not in line]

galaxy_coords = sum([[(i, j) for j, x in enumerate(line) if x == '#'] for (i, line) in enumerate(universe)], [])
end = time.perf_counter()
print(end-start)
total = 0

for i, (a, b) in enumerate(galaxy_coords):
  for j, (c, d) in enumerate(galaxy_coords[i+1:]):
    dy = abs(d-b)
    dx = abs(c-a)
    for x in empty_columns:
      if x in range(min(d,b), max(d,b)):
        dy += (1000000-1)
    for x in empty_rows:
      if x in range(min(c,a), max(c,a)):
        dx += (1000000-1)
    dist = dy+dx
    total += dist
  
print(total)
total = 0
total = sum([sum([sum([abs(d-b), abs(c-a)]+[1000000-1 for x in empty_columns if x in range(min(d,b), max(d,b))]+[1000000-1 for x in empty_rows if x in range(min(c,a), max(c,a))]) for c, d in galaxy_coords[i+1:]]) for i, (a, b) in enumerate(galaxy_coords)])

#for i, (a, b) in enumerate(galaxy_coords):
  #total += 
  #for j, (c, d) in enumerate(galaxy_coords[i+1:]):
    
    # dy = abs(d-b)
    # dx = abs(c-a)
    # for x in empty_columns:
    #   if x in range(min(d,b), max(d,b)):
    #     dy += (1000000-1)
    # for x in empty_rows:
    #   if x in range(min(c,a), max(c,a)):
    #     dx += (1000000-1)
    # dist = dy+dx


print(total)

""" print(sum([
  sum([
    sum(
      [1000000-1 for x in 
        [i for i, line in enumerate(
          [x.strip() for x in open("input.txt").readlines()]) 
        if '#' not in line] 
      if x in range(min(c,a), max(c,a))]
      +[1000000-1 for y in 
        [j for j in range(10) if '#' not in 
         [linecheck[j] for linecheck in [x.strip() for x in open("input.txt").readlines()]]] 
         if y in range(min(d,b), max(d,b))]+[abs(d-b), abs(c-a)]) for c, d in galaxy_coords[i+1:]]) for i, (a, b) in enumerate(galaxy_coords)])) """
