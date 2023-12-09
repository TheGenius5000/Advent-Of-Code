import time

def diff(nums):
  difference = []
  last_diff = 0
  for i, n in enumerate(nums[:-1]):
    diff = n - nums[i+1]
    difference.append(diff)
    last_diff = diff
  return difference

start = time.perf_counter()
extrapolations = []

with open("input.txt") as f:
  for line in f:
    nums = list(map(int, line.strip().split()[::-1]))
    differences = diff(nums)
    difference_next = [differences[0]]
    while (any(differences)):
      differences = diff(differences)
      difference_next.append(differences[0])
    extrapolations.append(nums[0] + sum(difference_next))

print(sum(extrapolations))

end = time.perf_counter()
print(end-start)