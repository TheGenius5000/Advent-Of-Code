import re

memory = open("input_test.txt", "r").read()
memory_split = [x.split("do()") for x in open("input_test.txt", "r").read().split("don't()")]

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

print(sum([(multiply_nums := [int(re.sub('\D', '', multiply)) for multiply in multiply_string.split(",")])[0]*multiply_nums[1] for multiply_string in re.findall("mul\([0-9]+,[0-9]+\)",)]))

print((split_by_do_dont := [memory.split("do()") for memory in open("input.txt", "r").read().split("don't()")])[0], sum([(multiply_nums := [int(re.sub('\D', '', multiply)) for multiply in multiply_string.split(",")])[0]*multiply_nums[1] for multiply_string in re.findall("mul\([0-9]+,[0-9]+\)", ''.join(split_by_do_dont[0]))]))
print(sum([sum([(multiply_nums := [int(re.sub('\D', '', multiply)) for multiply in multiply_string.split(",")])[0]*multiply_nums[1] for multiply_string in re.findall("mul\([0-9]+,[0-9]+\)", ''.join(memory[1:]))]) for memory in [memory.split("do()") for memory in open("input.txt", "r").read().split("don't()")][1:]], sum([(multiply_nums := [int(re.sub('\D', '', multiply)) for multiply in multiply_string.split(",")])[0]*multiply_nums[1] for multiply_string in re.findall("mul\([0-9]+,[0-9]+\)", open("input.txt", "r").read().split("don't()")[0])])))