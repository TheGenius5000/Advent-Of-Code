import re
import functools
import time

lines = [(((x[0]+'?')*5)[:-1], [int(y) for y in x[1].split(",")]*5) for x in [x.strip().split() for x in open("D:/GitHub/Advent-Of-Code/2023/Day 12/input.txt")]]
#lines = [(''.join(list(filter(None, re.split('(\.)',''.join(re.sub('\.\.+', '.', x[0])).strip('.'))))), [int(y) for y in x[1].split(",")]) for x in [x.strip().split() for x in open("D:/GitHub/Advent-Of-Code/2023/Day 12/input.txt")]]


totals = []

@functools.cache
def permutate(conditions, target_str):
  if target_str.count('#') < conditions.count('#'):
    return 0

  if target_str == '':
    return 1

  total = 0

  try:
    while conditions[0] == ".":
      conditions = conditions[1:]
  except:
    return total
  
  if len(target_str) > len(conditions):
    return total

  if conditions[0] == '?':
    total += permutate(conditions[1:], target_str)
  
  curr_group = target_str.split('.')[0]
  if '.' in target_str: curr_group += '.'

  try:
    for i, x in enumerate(curr_group):
      if (x == '#' and conditions[i] not in '?#') or (x == '.' and conditions[i] not in '?.'):
        raise Exception
  except:
    return total

  total += permutate(conditions[len(curr_group):], target_str[len(curr_group):])

  return total

start = time.perf_counter()
for i, (conditions, groups) in enumerate(lines):
  targets = ['#'*x+'.' for x in groups]
  targets[-1] = targets[-1].replace('.', '')
  stack = []

  if len(''.join(targets)) == len(conditions):
    totals.append(1)
    continue
  
  this_go = permutate(conditions, ''.join(targets))
  totals.append(this_go)


print(sum(totals))
end = time.perf_counter()
print(end-start)