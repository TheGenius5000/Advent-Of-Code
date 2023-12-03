import time
import re

symbols = "!@#$%^&*_-+=/"

#Looks around the line on the grid to find the associative numbers and returns them in a list
def peekForNums(line, symbol):
  amount = []
  length = 0
  nums = list(filter(None, re.split('([.])', line.replace(symbol, "."))))
  for n in nums:
    if length >= 5:
        break
    length += len(n)
    if n.isdigit():
      if length < 3:
        continue
      amount.append(int(n))
  return amount

start = time.perf_counter()
with open("input.txt", "r") as f:
  lines = f.readlines()

gear_vals = []
total = 0

#Loop on every gear symbol on input
for i0, line in enumerate(lines):
  if i0 != 0 and i0 != (len(lines)-1):
    for i1, ch in enumerate(line):
      if ch == "*":
        symbol_total = []
        schematic_space = [lines[i0-1][i1-3:i1+4], lines[i0][i1-3:i1+4], lines[i0+1][i1-3:i1+4]]
        for schematic in schematic_space:
          if any(x.isdigit() for x in schematic[2:5]):
            symbol_total += peekForNums(schematic, ch)
        gear_vals.append(symbol_total)

#Get product of every gear symbol if possible
for xs in gear_vals:
  if len(xs) == 2:
    total += xs[0]*xs[1]

print(total)
end = time.perf_counter()
print(end-start)