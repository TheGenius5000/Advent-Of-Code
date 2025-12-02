import time
import math

## Day 2 - Gift Shop
## Average runtime: ~

start_time = time.perf_counter()

with open(r"input.txt") as f:
  lines = f.read()[:-1]

id_ranges = [x.split("-") for x in lines.split(",")]

## Part 1
# Problem: Given a list of ID ranges, find and sum all the invalid IDs, which are those which have two repeating numbers inside e.g. 123123.

# Solution: Go through the range of IDs, finding each repeating number.

def get_next_repeating_number(num):
  str_num = str(num)
  if len(str_num) % 2 == 1:
    new_num  = ("1"+"0"*(len(str_num)//2))*2
    return int(new_num)
  half = str_num[:len(str_num)//2]
  if (new_num := int(half*2)) > num:
    return new_num
  half = int(half)+1
  new_num = int(str(half)*2)
  return new_num

def check_if_repeating(num):
  str_num = str(num)
  return str_num[len(str_num)//2:] == str_num[:len(str_num)//2]

#Sum of all invalid IDs
ans1 = 0

for start, end in id_ranges:
  start = int(start)
  end = int(end)
  if check_if_repeating(start): 
    ans1 += start
    #print(start)
  num = start
  while num < end:
    num = get_next_repeating_number(num)
    if start <= num <= end: 
      #print(num)
      ans1 += num

print(f"The sum of invalid IDs for part 1 is {ans1}")

## Part 2
# Problem: Find the sum of invalid IDs 

# Solution: Go through the range of IDs, finding each repeating number. The function has been generalised to handle any n-length sequence of repeating numbers.

#N - how many repeating digits there are.
def get_next_n_repeating_number(num, n):
  str_num = str(num)
  multiple = len(str_num)//n
  repeating_num = int(str_num[:n])
  new_num = int(str(repeating_num)*multiple)
  if new_num <= num:
    if str(repeating_num) == "9"*n: 
      repeating_num = "1"+"0"*(n-1)
      new_num = int(repeating_num*(multiple+1))
    else: 
      repeating_num += 1
      new_num = int(str(repeating_num)*multiple)
  return new_num

def check_if_n_repeating_number(num, n):
  if num < 10: return False
  str_num = str(num)
  repeating_num = str_num[:n]
  return int(repeating_num*(len(str_num)//n)) == num

#Sum of all invalid IDs (for part 2)
ans2 = 0

for start, end in id_ranges:
  str_start, str_end = start, end
  start = int(start)
  end = int(end)
  invalid_ids = set()
  invalid_idsp1 = set()
  for n in range(1, len(str_end)//2+1):
    if (len(str_start) % n == 0) or (len(str_end) % n == 0):
      num = start
    else:
      continue 
    if check_if_n_repeating_number(start, n): invalid_ids.add(start)

    while num < end:
      num = get_next_n_repeating_number(num, n)
      if num < 10: continue
      if num == -1: break
      if start <= num <= end:
        invalid_ids.add(num)
  ans2 += sum(invalid_ids)

print(f"The sum of all invalid IDs for part 2 is {ans2}")

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")