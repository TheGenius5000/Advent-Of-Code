lines = open("D:\\GitHub\\Advent-Of-Code\\2024\\Day 2\\input.txt", "r").read().splitlines()

safe_lines = 0

for line in lines:
  past_num = (numbers := list(map(int, line.split())))[0]
  increasing = past_num < numbers[1]
  for n in numbers[1:]:
    if increasing != (past_num < n):
      break
    if not(1 <= abs(past_num - n) <= 3):
      break
    past_num = n
  else:
    safe_lines += 1

print(safe_lines)