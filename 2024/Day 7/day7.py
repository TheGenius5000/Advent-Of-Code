import itertools
import time
import functools
from operator import mul, add

start_time = time.time()

lines = {int((split_x := x.split(": "))[0]): list(map(int, split_x[1].split())) for x in open("input.txt").read().splitlines()}
success = []
targets = []
total, total2 = 0,0

n = 1

def concat(a, b):
  return int(str(a)+str(b))

print(concat(62, 4))

@functools.cache
def combinations(length, operations):
  if length == 1:
    return set([(operation,) for operation in operations])
  new_set = set()
  for operation in operations:
    for subset in combinations(length-1, operations):
      new_set.add((operation,)+subset)
  return new_set

print(combinations(2, (mul, add)))

for target, nums in lines.items():
  targets.append(target)
  for operations in combinations(len(nums)-1,(mul,add)):
    evaluation = nums[0]
    for i, f in enumerate(operations):
      evaluation = f(evaluation, nums[i+1])
    if evaluation == target:
      total += target
      success.append(target)
      break

print(total)
failed = list(set(targets) - set(success))

for target in failed:
  nums = lines[target]
  for operations in combinations(len(nums)-1,(mul,add,concat)):
    evaluation = nums[0]
    for i, f in enumerate(operations):
      evaluation = f(evaluation, nums[i+1])
    if evaluation == target:
      total2 += target
      success.append(target)
      break

print(total2+total)

end_time = time.time()


print(f"{end_time-start_time} seconds")