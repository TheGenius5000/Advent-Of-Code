lines = [list(map(int, line.split())) for line in open("input.txt", "r").read().splitlines()]

safe_numbers = 0
#unsafe_numbers_list = []

for i, numbers in enumerate(lines):
  #unsafe_numbers_list.append([])
  past_num = numbers[0]
  increasing = past_num < numbers[1]
  unsafe = False
  for j, n in enumerate(numbers[1:]):
    if increasing != (past_num < n) or not(1 <= abs(past_num - n) <= 3):
      unsafe = True
      #unsafe_numbers_list[i].append(j)
      #unsafe_numbers_list[i].append(j+1)
    past_num = n
  if not unsafe:
    safe_numbers += 1
  if unsafe:
    for i, number in enumerate(numbers):
      line_check = numbers.copy()
      del line_check[i]
      past_num = line_check[0]
      increasing = past_num < line_check[1]
      for n in line_check[1:]:
        if increasing != (past_num < n) or not(1 <= abs(past_num - n) <= 3):
          break
        past_num = n
      else:
        safe_numbers += 1
        break

print(safe_numbers)

# for i, unsafe_numbers in enumerate(unsafe_numbers_list):
#   for index in unsafe_numbers:
#     line_check = lines[i].copy()
#     del line_check[index]
#     past_num = line_check[0]
#     increasing = past_num < line_check[1]
#     for n in line_check[1:]:
#       if increasing != (past_num < n) or not(1 <= abs(past_num - n) <= 3):
#         break
#       past_num = n
#     else:
#       safe_numbers += 1
#       break

# print(safe_numbers)
