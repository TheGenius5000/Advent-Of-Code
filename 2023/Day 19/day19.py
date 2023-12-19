import copy
import time

def combination_search(location, ranges):
  while location not in "AR":
    for k, v in workflows[location].items():
      if not v: 
        location = k
        continue
      category, operation, val = k[0], k[1], int(k[2:])
      if operation == ">":
        new_ranges = copy.deepcopy(ranges)
        new_ranges[category][0] = val+1
        combination_search(v, new_ranges)
        ranges[category][1] = val
      elif operation == "<":
        new_ranges = copy.deepcopy(ranges)
        new_ranges[category][1] = val-1
        combination_search(v, new_ranges)
        ranges[category][0] = val
  if location == "A":
    acceptible_parts.append(ranges)


start = time.perf_counter()
workflows_input, parts_input = open("input.txt").read().split("\n\n")

parts = [dict([(split_kvs := kvs.split("="))[0], int(split_kvs[1])] for kvs in part[1:-1].split(",")) for part in parts_input.splitlines()]
workflows = dict([((split_x := x.split("{"))[0], dict(y.split(":") if ":" in y else [y, None] for y in split_x[1][:-1].split(",") )) for x in workflows_input.splitlines()])

accepted = []

for part in parts:
  location = "in"
  x = part['x']
  m = part['m']
  a = part['a']
  s = part['s']
  while location not in "AR":
    for k, v in workflows[location].items():
      if not v: location = k
      elif eval(k):
        location = v
        break
  if location == "A": accepted.append(part) 

print(sum([sum(d.values()) for d in accepted]))

acceptible_parts = []

combination_search("in", {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]})
total = 0
for d in acceptible_parts:
  temp_total = 1
  for range in d.values():
    temp_total *= range[1]-range[0]+1
  total += temp_total

print(total)
end = time.perf_counter()
print(end-start)