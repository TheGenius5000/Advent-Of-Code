import time

# def fall_amount(key):
#   what_falls = 0
#   for v in supporting[key]
  
def addTuple(tup1, tup2):
  return tuple(sum(x) for x in zip(tup1,tup2))

start = time.perf_counter()
lines = [[tuple(map(int, coords.split(","))) for coords in line.split("~")] for line in open("input.txt").read().splitlines()]
#viz(lines)
space = [[[None for _ in range(10)] for _ in range(10)] for _ in range(10)]
bricks = sorted(lines, key=lambda x: x[0][2])
supporting = {}
brick_remove_options = set()


for i, (brick_start, brick_end) in enumerate(bricks):
  diff = tuple(b-a for a, b in zip(brick_start, brick_end))
  if any([x < 0 for x in diff]):
    bricks[i][0] = brick_end
    bricks[i][1] = brick_start

for i, ((xstart, ystart, zstart), (xend, yend, zend)) in enumerate(bricks):
  if zend == 1 or zstart == 1: continue
  #delta = tuple(giveDelta(b, a) for a, b in zip(bricks[i][0], bricks[i][1]))
  possible_lowest = 1
  for j, ((x0, y0, z0), (x1, y1, z1)) in enumerate(bricks[:i]):
    if len(range(max(x0, xstart), min(x1, xend)+1)) > 0:
      if len(range(max(y0, ystart), min(y1, yend)+1)) > 0:
        if z1+1 > possible_lowest: possible_lowest = z1+1
  bricks[i][0] = (xstart, ystart, possible_lowest)
  bricks[i][1] = (xend, yend, possible_lowest + (zend-zstart))


for i, ((xstart, ystart, zstart), (xend, yend, zend)) in enumerate(bricks):
  supporting[(xstart, ystart, zstart), (xend, yend, zend)] = []
  for another_brick in bricks[i+1:]:
    (x0, y0, z0), (x1, y1, z1) = another_brick
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

print(len(brick_remove_options))
end = time.perf_counter()
print(end-start)


#for brick_start, brick_end in lines: