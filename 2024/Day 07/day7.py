import time
import functools
from operator import mul, add

start_time = time.time()

lines = {int((split_x := x.split(": "))[0]): list(map(int, split_x[1].split())) for x in open("input.txt").read().splitlines()}
total = [0,0]

def concat(a, b):
  return int(str(a)+str(b))

@functools.cache
def combinations(length, operations):
  if length == 1:
    return set([(operation,) for operation in operations])
  return set([(operation,)+subset for subset in combinations(length-1, operations) for operation in operations])

for target, nums in lines.items():
  for total_part, operations_part in [(0, (mul,add)), (1, (mul,add,concat))]:
    for operations in combinations(len(nums)-1,operations_part):
      evaluation = nums[0]
      for i, f in enumerate(operations):
        evaluation = f(evaluation, nums[i+1])
      if evaluation == target:
        total[total_part] += target
        break
    else: continue
    break

print(total[0])
print(total[1]+total[0])

end_time = time.time()
print(f"{end_time-start_time} seconds")