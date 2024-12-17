import time

# #
#
# Only works for my input, sorry!
#
# #

start_time = time.time()

lines = open("input.txt").read().splitlines()

def xor_combinations(ans):
  return [(a,b) for a in range(8) for b in range(8) if a^b == ans]

instruction_pointer = 0

program = list(map(int, lines[-1].split(" ")[1].split(",")))
target = ''.join(map(str, program))
big_A = 0

for outpt in reversed(program):
  possibleAs = []
  for end_b, end_c in xor_combinations(outpt):
    start_b = end_b^7
    possible_a = (big_A << 3) + start_b
    b_c_shift = start_b^3
    c_from_b = possible_a >> b_c_shift
    if (c_from_b % 8) != end_c: continue
    possibleAs.append(possible_a)
  big_A = min(possibleAs)
  pass

print(big_A)

end_time = time.time()

print(f"{end_time-start_time} seconds")