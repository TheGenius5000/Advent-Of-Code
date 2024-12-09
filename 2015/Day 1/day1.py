# Very Easy

import time

start_time = time.time()

line = open("input.txt").read()

floor = 0
basement_pos = 0

for i, ch in enumerate(line):
  if ch == '(':
    floor += 1
  elif ch == ')':
    floor -= 1
  if floor == -1 and basement_pos == 0:
    basement_pos = i+1

print(floor)
print(basement_pos)

end_time = time.time()

print(f"{end_time-start_time} seconds")