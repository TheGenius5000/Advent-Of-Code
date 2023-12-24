import time
import decimal
from z3 import *

class CarryOn(Exception):
  pass

start = time.perf_counter()
hailstones = [[tuple([int(nums) for nums in stuff.split(",")]) for stuff in lines.split("@")] for lines in open("D:/GitHub/Advent-Of-Code/2023/Day 24/input.txt").read().splitlines()]
total=0
test_area_lower = 200000000000000
test_area_higher = 400000000000000
lines = []

for i in range(len(hailstones)-1):
  [(pxA, pyA, pzA), (vxA, vyA, vzA)] = hailstones[i]
  line1m = decimal.Decimal(vyA/vxA)
  line1c = decimal.Decimal(pyA - line1m*pxA)
  if i < 3:
    lines.append(hailstones[i])
  for (pxB, pyB, pzB), (vxB, vyB, vzB) in hailstones[i+1:]:
    line2m = decimal.Decimal(vyB/vxB)
    line2c = decimal.Decimal(pyB - line2m*pxB)
    if line2m == line1m: continue
    intersection_x = decimal.Decimal((line1c-line2c)/(line2m-line1m))
    intersection_y = decimal.Decimal(line1m*intersection_x + line1c)
    try:
      for checkvx, checkvy, checkpx, checkpy in [(vxA, vyA, pxA, pyA), (vxB, vyB, pxB, pyB)]: 
        if any([
          checkvx < 0 and intersection_x > checkpx,
          checkvx > 0 and intersection_x < checkpx,
          checkvy < 0 and intersection_y > checkpy,
          checkvy > 0 and intersection_y < checkpy,
        ]): 
          raise CarryOn
    except:
      continue
    if test_area_lower <= intersection_x <= test_area_higher and test_area_lower <= intersection_y <= test_area_higher: total +=1

print(total)
print(lines)
s = Solver()
xr = Int('xr')
yr = Int('yr')
zr = Int('zr')
a = Int('a')
b = Int('b')
c = Int('c')
line = 0

for (px, py, pz), (vx, vy, vz) in lines:
  line += 1
  t = Int(f"t{line}")
  s.add(
    t >= 0,
    xr + a*t == px + vx*t,
    yr + b*t == py + vy*t,
    zr + c*t == pz + vz*t
  )

print(s.check())
m = s.model()
for d in m.decls():
    print ("%s = %s" % (d.name(), m[d]))

print(eval(str(m[xr]+m[yr]+m[zr])))
end = time.perf_counter()
print(end-start)