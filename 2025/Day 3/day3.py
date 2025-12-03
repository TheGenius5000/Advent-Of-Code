import time

## Day 3 - Lobby
## Average runtime: ~

start_time = time.perf_counter()

with open(r"D:\GitHub\Advent-Of-Code\2025\Day 3\input.txt") as f:
  lines = f.read().splitlines()

## Part 1
# Problem: Find the maximum joltage (any two digits, the first appearing before the second) for each battery bank (each row of the input) and give the sum.

# Solution: Go through each row, and for each row, look for the maximum digits the first and second could be. Going in reverse order helps with this.

ans1 = 0

#Function that gives a tuple of (digit of the nth place, location of said digit)
def find_nth_digit(lst, n, min_range):
  digit = -1
  for i, x in enumerate(list(map(int, list(lst[min_range:])))):
    if i+min_range >= len(lst)-n+1: break
    if x > digit:
      index = i+min_range
      digit = x 
    if digit == 9: break 
  return (digit, index)


for line in lines:
  ten, ten_index = find_nth_digit(list(line), 2, 0)
  unit, unit_index  = find_nth_digit(list(line), 1, ten_index+1)
  num = ten*10 + unit
  ans1 += num

print(f"The sum of all the 2-digit joltage is {ans1}")

ans2 = 0

for line in lines:
  line = list(line)
  indexes = [None]*12
  digits = [None]*12
  prev_digit_index = -1
  for n in range(12, 0, -1):
    digit, index = find_nth_digit(line, n, prev_digit_index+1)
    indexes[len(indexes)-n] = index
    digits[len(digits)-n] = digit
    prev_digit_index = index
  #print(digits)
  #print(indexes)
  num = int("".join(list(map(str, digits))))
  #print(num)
  ans2 += num


## Part 2
# Problem: Find the joltage value, but instead of two digits being applied as the joltage, find 12 digits for the joltage.

# Solution: The above solution has been extracted into a function and allowed to pass the nth digit needed. It removed the two previously hard-coded tens and units check.

print(f"The sum of 12-digit joltage was {ans2}")


end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")