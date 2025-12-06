import time
import math

## Day 6 - Trash Compactor
## Average runtime: ~0.006 seconds

start_time = time.perf_counter()

with open(r"input.txt") as f:
  lines = f.read().splitlines()

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
for stuff in zip(*[x.split() for x in lines]):
  homework.append((tuple(map(int, stuff[:-1])), symbol_parser(stuff[-1])))

for nums, func in homework:
  ans1 += func(nums)

print(f"The sum of the homework answers is {ans1}.")

## Part 2
# Problem: Solve the homework problems as before, but the numbers are read right-to-left in columns.

lines = [line[::-1] for line in lines]
ans2 = 0

# Solution: Similar to part 1, but instead of directly converting into integers, we read the columns on the reversed input via a caret.

caret = 0
nums = []

while True:
  if (caret >= len(lines[0])) or all([x[caret] == ' ' for x in lines]):
    answer = func(nums)
    #print(answer)
    ans2 += answer
    nums = []
    caret += 1
    if caret >= len(lines[0]): break
    continue
  nums.append(int(''.join([x[caret] for x in lines[:-1]]).strip()))#Vertical read
  if lines[-1][caret] != " ":
    func = symbol_parser(lines[-1][caret])
  caret += 1

print(f"The sum of the cephalopod-written homework answers is {ans2}")

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")