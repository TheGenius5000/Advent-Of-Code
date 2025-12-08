import time

## Day 7 - Laboratories
## Average runtime: ~

start_time = time.perf_counter()

with open(r"D:\GitHub\Advent-Of-Code\2025\Day 7\input_test.txt") as f:
  lines = f.read().splitlines()

## Part 1
# Problem: Figure out how many times the beam will be split based on the tachyon manifold. That is, you start at the top, going down, and every time you find a splitter, you restart the beam twice to the immediate left and the immediate right.

# Solution: Iterate down the lines and perform the beam split. Count how many unique beams you have.

beams = {lines[0].index("S")}
splits = 0


for line in lines[1:]:
  for i, ch in enumerate(line):
    if i not in beams: continue
    if ch != "^": continue
    beams.remove(i)
    beams.update({i-1, i+1})
    splits += 1

print(f"The number of tachyon beam splits is {splits}.")

## Part 2
# Problem: Figure out many paths the beam could've took, and give the total of that.

# Solution: Do the splits again, but keep track of how many paths it took to reach a certain splitter.

# beams = {(lines[0].index("S"), 1)}

# for line in lines[1:]:
#   for i, ch in enumerate(line):


end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")