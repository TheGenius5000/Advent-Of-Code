import time
import functools

start_time = time.perf_counter()



colours = ["w","g","r","b","u"]

lines = open("input.txt").read().split("\n\n")
designs = lines[1].splitlines()
towels_by_size = dict()
towels_by_colour = {colour: [] for colour in colours}
for towel in lines[0].split(", "):
  towel = towel.strip()
  if len(towel) not in towels_by_size:
    towels_by_size[len(towel)] = set([towel])
  else:
    towels_by_size[len(towel)].add(towel)
  for c in towels_by_colour:
    if c in towel:
      towels_by_colour[c].append(towel)

for v in towels_by_colour.values():
  v.sort(key=len)

absent_single_colours = {colour for colour in colours if colour not in towels_by_size[1]}
accepted_designs = set()
ans2 = 0

@functools.cache
def is_there_design(design):
  global towels_by_size, towels_by_colour, absent_single_colours
  if not((colours_needed := set(design) & absent_single_colours)): return True
  if len(design) == 1: return False
  for abs_colour in colours_needed:
    for towel in towels_by_colour[abs_colour]:
      if towel not in design: continue
      design_edit = design.replace(towel,'.')
      if all(is_there_design(sub_design) for sub_design in design_edit.split(".")): return True

@functools.cache
def all_designs(design):
  global towels_by_size, towels_by_colour, absent_single_colours
  if design in absent_single_colours: return 0
  elif not design: return 1
  total_designs = 0
  this_colour = design[0]
  for towel in towels_by_colour[this_colour]:
    if towel not in design[:len(towel)]: continue
    total_designs += all_designs(design[len(towel):])
  return total_designs

for design in designs:
  if is_there_design(design): accepted_designs.add(design)  
  ans2 += all_designs(design)

print(len(accepted_designs))
print(ans2)

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")