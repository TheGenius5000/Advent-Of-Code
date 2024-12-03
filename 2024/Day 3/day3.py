import re

memory = open("input.txt", "r").read()

multiply_numbers = re.findall("(mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\))", memory)
total = 0
do_calculation = True

for multiply_string in multiply_numbers:
  if multiply_string == 'do()':
    do_calculation = True
  elif multiply_string == "don't()":
    do_calculation = False
  else:
    multiply_string = [int(re.sub('\D', '', multiply)) for multiply in multiply_string.split(",")]
    total += multiply_string[0]*multiply_string[1] if do_calculation else 0

print(total)

print(sum([(multiply_nums := [int(re.sub('\D', '', multiply)) for multiply in multiply_string.split(",")])[0]*multiply_nums[1] for multiply_string in re.findall("mul\([0-9]+,[0-9]+\)", open("input.txt", "r").read())]))