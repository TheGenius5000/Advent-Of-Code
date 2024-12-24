import time
import re

## Day 24: Crossed Wires
## Difficulty: Hard (Very Hard if not done manually)
## Need-to-know skills: Binary addition, Half adders, Full adders

## Problem:

## Solution: 

## Average runtime: ~ 0.038 seconds

start_time = time.perf_counter()

def XOR(a,b): return a^b
def AND(a,b): return a&b
def OR(a,b): return a|b
def sorted_tuple(*args): return tuple(sorted(args))

def bits_from_val(ch): return ''.join([str(bits[b]) for b in sorted([k for k in bits if re.match(f"{ch}[0-9]*", k)])])
def is_starting_register(bit): return bit[0] in 'xy' and bit[1].isdigit()
def is_z_register(bit): return bit[0] in 'z' and bit[1].isdigit()

operations = dict()
bits = dict()
eval_operations = {k:v for k, v in zip(["XOR", "AND", "OR"], [XOR, AND, OR])}
eval_operations_from_func = {k:v for k, v in zip([XOR, AND, OR],["XOR", "AND", "OR"])}
outputs_from = dict()

with open(r"input.txt") as f:
  inf = f.read()
  
starting_bits_stream, operations_stream = [x.splitlines() for x in inf.split("\n\n")]
del inf

highest_bit = 0
for inf_starting_bit in starting_bits_stream:
  var_name, value = inf_starting_bit.split(": ")
  bits[var_name] = int(value)
  nth_digit = int(var_name[1:])
  if nth_digit > highest_bit: highest_bit = nth_digit

for inf_operation in operations_stream:
  [input1, operation_name, input2], [output] = [x.strip().split(" ") for x in inf_operation.split("->")]
  operation = (eval_operations[operation_name], sorted_tuple(input1,input2))
  if operation not in operations: operations[operation] = output

not_visited = list(operations.keys())
while not_visited:
  operation = not_visited.pop(0)
  (gate, (input1, input2)) = operation
  if any(inp not in bits for inp in (input1, input2)): 
    not_visited.append(operation)
    continue
  output = operations[operation]
  bits[output] = gate(bits[input1], bits[input2])

for operation, output in operations.items():
  outputs_from[output] = operation

z_bits = list(map(int, bits_from_val('z')))
bad_bits = []

def print_half_adder(a, b, sum_store, carry_store):
  print(f"{a}: {bits[a]}, {b}: {bits[b]}")
  original_a, original_b = a,b
  if (XOR, sorted_tuple(a,b)) not in operations:
    _, needed_inputs = outputs_from[f"z{i:02}"]
    a_and_b = set([a,b])
    shared_var = [input for input in a_and_b for needed_input in needed_inputs if input == needed_input][0]
    a_and_b.remove(shared_var)
    useless_var = a_and_b.pop()
    needed_inputs = set(needed_inputs)
    needed_inputs.remove(shared_var)
    required_var = needed_inputs.pop()
    huge_problem_handler(useless_var, required_var)
    a,b = required_var,shared_var
  print(f"Sum bit at: {(sum_loc := operations[(XOR, sorted_tuple(a,b))])}, Carry out bit at: {(carry_out_loc :=  operations[(AND, sorted_tuple(a,b))])}")
  print(f"Sum bit: {bits[sum_loc]}, Carry bit: {bits[carry_out_loc]}")
  register[carry_store] = carry_out_loc
  register[sum_store] = sum_loc

def huge_problem_handler(wrong1, wrong2):
  print(f"\nHuge problem! Need to swap {wrong1} and {wrong2}\n")
  bad_bits.append(wrong2)
  bad_bits.append(wrong1)
  register_swapper(wrong1, wrong2)

def register_swapper(v0, v1):
  for k, v in register.items():
    if v == v0: register[k] = v1
    elif v == v1: register[k] = v0

x_loc, y_loc, z_loc = 'x00', 'y00', 'z00'
c_in, c0, c1, sum0, sum1 = "c_in", "c0", "c1", "sum0", "sum1"
register = {k: None for k in [c_in, c0, c1, sum0, sum1]}

#Full adder here
for i, z_bit in enumerate(z_bits):
  if i == len(z_bits) - 1: break
  if i == 0:
    print_half_adder(x_loc, y_loc, sum0, c_in)
    print()
    continue
  x_loc, y_loc, z_loc = [f"{ch}{i:02}" for ch in ('x','y','z')]
  print(f"Carry in ({register[c_in]}): {bits[register[c_in]]}")
 
  print("First half adder:")
  print_half_adder(x_loc, y_loc, sum0, c0)

  print("Second half adder:")
  print_half_adder(register[sum0], register[c_in], sum1, c1)
  if not is_z_register(register[sum1]):
    huge_problem_handler(z_loc, register[sum1])
    
  print(f"Carry 1 ({register[c0]}): {bits[register[c0]]}, Carry 2 ({register[c1]}): {bits[register[c1]]}")
  register[c_in] = operations[(OR, sorted_tuple(register[c0], register[c1]))]
  
  print(f"Final sum bit ({register[sum1]}): {bits[register[sum1]]}, Final carry out bit ({register[c_in]}): {bits[register[c_in]]}\n")
  if not is_z_register(register[c_in]): continue
  print(f"\nHuge problem! Need to swap {register[c_in]} and {register[sum1]}\n")
  bad_bits.append(register[sum1])
  bad_bits.append(register[c_in])
  register[sum1], register[c_in] = register[c_in], register[sum1]


  

print(int(''.join(map(str, z_bits[::-1])), 2))
print(','.join(list(sorted(set(bad_bits)))[:-2]))

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")