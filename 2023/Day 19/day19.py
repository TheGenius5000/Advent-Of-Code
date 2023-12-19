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

