import time

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


end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")