import time
import functools

## Day 11 - Reactor
## Average runtime: ~

start_time = time.perf_counter()

with open(r"input.txt") as f:
  lines = f.read().splitlines()

## Part 1
# Problem: 

# Solution: 

cables = dict()
for line in lines:
  key, values = line.split(":")
  cables[key] = values.strip().split()
  
ans1 = 0  
stack = ["you"]
while len(stack) > 0:
  cable = stack.pop()
  if cable == "out":
    ans1 += 1
    continue
  for v in cables[cable]:
    stack.append(v)

print(f"The number of routes to 'out' is {ans1}.")

## Part 2
# Problem: 

# Solution: 

ans2 = 0
stack = [("svr", False, False, 0)]
good_routes = set()
bad_routes = set()
route_history = {0: []}

@functools.cache
def connection_travel(cable, fft_visit, dac_visit):
  if (cable == "out") and all([fft_visit, dac_visit]): return 1
  elif cable == "out": return 0
  if cable == "fft": fft_visit = True
  if cable == "dac": dac_visit = True

  total = 0
  for sub_cable in cables[cable]:
    total += connection_travel(sub_cable, fft_visit, dac_visit)
  return total

ans2 = connection_travel("svr", False, False)

print(f"The number of routes visiting 'fft' and 'dac' is {ans2}.")


end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")