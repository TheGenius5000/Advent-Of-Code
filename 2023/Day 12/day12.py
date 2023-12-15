import re

#lines = [(''.join(list(filter(None, re.split('(\.)',''.join(re.sub('\.\.+', '.', x[0])).strip('.'))))), [int(y) for y in x[1].split(",")]) for x in [x.strip().split() for x in open("D:/GitHub/Advent-Of-Code/2023/Day 12/input.txt")]]
lines = [(((''.join(list(filter(None, re.split('(\.)',''.join(re.sub('\.\.+', '.', x[0])).strip('.')))))+'?')*5)[:-1], [int(y) for y in x[1].split(",")]*5) for x in [x.strip().split() for x in open("D:/GitHub/Advent-Of-Code/2023/Day 12/test.txt")]]

totals = []

def permutate(conditions, targets):
  target_str = ''.join(targets)
  if target_str.count('#') < conditions.count('#'):
    return 0

  try:
    while conditions[0] == ".":
      conditions = conditions[1:]
  except:
    if targets:
      return 0
  
  if targets == []:
    return 1

  if conditions[0] == '?':
    return permutate(conditions[1:], targets)
  
  try:
    for i, x in enumerate(targets[0]):
      if (x == '#' and conditions[i] not in '?#') or (x == '.' and conditions[i] not in '?.'):
        raise Exception
  except:
    return 0

  return(conditions[len(targets[0]):], targets[1:])

for i, (conditions, groups) in enumerate(lines):
  targets = ['#'*x+'.' for x in groups]
  targets[-1] = targets[-1].replace('.', '')
  stack = []
  total = 0

  """ if len(''.join(targets)) == len(conditions):
    totals.append(1)
    continue """

  stack.append((conditions, targets.copy()))
  while stack != []:

    conditions, targets = stack.pop()

    target_str = ''.join(targets)
    if target_str.count('#') < conditions.count('#'):
      continue

    try:
      while conditions[0] == ".":
        conditions = conditions[1:]
    except:
      if targets:
        continue
    
    if targets == []:
      total += 1
      continue

    if conditions[0] == '?':
      stack.append((conditions[1:], targets))
    
    try:
      for i, x in enumerate(targets[0]):
        if (x == '#' and conditions[i] not in '?#') or (x == '.' and conditions[i] not in '?.'):
          raise Exception
    except:
      continue

    stack.append((conditions[len(targets[0]):], targets[1:]))
  
  totals.append(total)

print(totals)
print(sum(totals))