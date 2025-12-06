import time
import math

## Day 6 - Trash Compactor
## Average runtime: ~

start_time = time.perf_counter()

with open(r"input.txt") as f:
  lines = [line.split() for line in f.read().splitlines()]



## Part 1
# Problem: Solve the math homework - each column represents numbers that should be added or mutliplied together, based on the symbol at the bottom of the column.

# Solution: Parse each line of the string, taking the 3/4 numbers and the symbol. Calculate and add to a running total.

homework = []
ans1 = 0

#If symbol is *, return mutliplication function, if +, return addition.
def symbol_parser(symbol):
  if symbol == "*": return math.prod
  if symbol == "+": return sum

#Groups numbers and symbol from the homework together by question, converts into int
for stuff in zip(*lines):
  homework.append((tuple(map(int, stuff[:-1])), symbol_parser(stuff[-1])))

for nums, func in homework:
  ans1 += func(nums)

print(f"The sum of the homework answers is {ans1}.")

## Part 2
# Problem: 

# Solution: 


end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")