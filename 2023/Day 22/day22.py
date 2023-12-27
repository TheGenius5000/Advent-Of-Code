import time

start = time.perf_counter()

bricks = sorted([[tuple(map(int, coords.split(","))) for coords in line.split("~")] for line in open("input.txt").read().splitlines()], key=lambda x: x[0][2])
supporting = {}
brick_remove_options = set()
cascade_total = 0

for i, ((xstart, ystart, zstart), (xend, yend, zend)) in enumerate(bricks):
  if zend == 1 or zstart == 1: continue
  possible_lowest = 1
  for (x0, y0, z0), (x1, y1, z1) in bricks[:i]:
    if len(range(max(x0, xstart), min(x1, xend)+1)) > 0:
      if len(range(max(y0, ystart), min(y1, yend)+1)) > 0:
        if z1+1 > possible_lowest: possible_lowest = z1+1
  bricks[i][0] = (xstart, ystart, possible_lowest)
  bricks[i][1] = (xend, yend, possible_lowest + (zend-zstart))

for i, ((xstart, ystart, zstart), (xend, yend, zend)) in enumerate(bricks):
  supporting[(xstart, ystart, zstart), (xend, yend, zend)] = []
  for (x0, y0, z0), (x1, y1, z1) in bricks[i+1:]:
    if z0 == zend+1:
      if len(range(max(x0, xstart), min(x1, xend)+1)) > 0:
        if len(range(max(y0, ystart), min(y1, yend)+1)) > 0:
          supporting[(xstart, ystart, zstart), (xend, yend, zend)].append(((x0, y0, z0), (x1, y1, z1)))

supported_by = dict.fromkeys(supporting)
for k, v in supporting.items():
  for tup in v:
    try:
      supported_by[tup].append(k)
    except:
      supported_by[tup] = [k]

for k, v in supporting.items():
  if not v:
    brick_remove_options.add(k)
    continue
  for brick in v:
    if len(supported_by[brick]) == 1: break
  else:
    brick_remove_options.add(tuple(k))

for k, v in supporting.items():
  if k in brick_remove_options: continue
  stack = [k]
  falling_history = set()
  while stack:
    current_brick = stack.pop()
    falling_history.add(current_brick)
    for brick in supporting[current_brick]:
      if set(supported_by[brick]).issubset(falling_history):
        stack.append(brick)
  cascade_total += len(falling_history)-1

print(cascade_total)
print(len(brick_remove_options))

end = time.perf_counter()
print(end-start)
