import time
import re

## Day 24: Crossed Wires
## Difficulty: 
## Need-to-know skills: 

## Problem: 

## Solution: 

## Average runtime: ~

start_time = time.perf_counter()

def XOR(a,b): return a^b
def AND(a,b): return a&b
def OR(a,b): return a|b
def sorted_tuple(*args): return tuple(sorted(args))

operations = dict()
bits = dict()
eval_operations = {k:v for k, v in zip(["XOR", "AND", "OR"], [XOR, AND, OR])}


with open(r"input.txt") as f:
  inf = f.read()
  
starting_bits_stream, operations_stream = [x.splitlines() for x in inf.split("\n\n")]
del inf

for inf_starting_bit in starting_bits_stream:
  var_name, value = inf_starting_bit.split(": ")
  bits[var_name] = int(value)

for inf_operation in operations_stream:
  [input1, operation_name, input2], [output] = [x.strip().split(" ") for x in inf_operation.split("->")]
  operation = (eval_operations[operation_name], (input1,input2))
  if operation not in operations: operations[operation] = [output]
  else: operations[operation].append(output)

not_visited = list(operations.keys())
while not_visited:
  operation = not_visited.pop(0)
  (gate, (input1, input2)) = operation
  if any(inp not in bits for inp in (input1, input2)): 
    not_visited.append(operation)
    continue
  for output in operations[operation]:
    bits[output] = gate(bits[input1], bits[input2])

z_bits = int(''.join(reversed([str(bits[b]) for b in sorted([k for k,v in bits.items() if re.match("z[0-9]*", k)])])), 2)

print(z_bits)

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")