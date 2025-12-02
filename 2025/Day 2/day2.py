import time

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
    print(start)
  num = start
  while num < end:
    num = get_next_repeating_number(num)
    if start <= num <= end: 
      print(num)
      ans1 += num

print(f"The sum of invalid IDs is {ans1}")

## Part 2
# Problem: 

# Solution: 

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")