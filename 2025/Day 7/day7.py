import time

## Day 7 - Laboratories
## Average runtime: ~0.0035 seconds

start_time = time.perf_counter()

with open(r"input.txt") as f:
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

# Solution: Do the splits again, but keep track of how many paths it took to reach a certain splitter. This is done via a hashmap.

beams = {lines[0].index("S"): 1}

j = 1
while j < len(lines):
  new_beams = {k: v for k, v in beams.items()}
  for beam, beam_count in sorted(beams.items(), key=lambda x: x[0]):
    if lines[j][beam] != "^": continue
    if beam-1 in new_beams:  new_beams[beam-1] += beam_count
    else: new_beams[beam-1] = beam_count
    if beam+1 in new_beams:  new_beams[beam+1] += beam_count
    else: new_beams[beam+1] = beam_count
    del new_beams[beam]
  j += 1
  beams = new_beams

ans2 = sum(beams.values())

print(f"The number of possible timelines is {ans2}.")

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")