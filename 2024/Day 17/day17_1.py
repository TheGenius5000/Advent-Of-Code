import time

start_time = time.time()

lines = open("D:\\GitHub\\Advent-Of-Code\\2024\\Day 17\\input.txt").read().splitlines()

class Operand():
  def __init__(self, value: int):
    self.value = value
  def __repr__(self) -> str:
    return f"Combo: {self.combo()} Literal: {self.literal()}"
  def combo(self) -> int:
    return registers[self.value] if self.value >= 4 else self.value 
  def literal(self) -> int:
    return self.value

def adv(o: Operand):
  ans = registers[4] >> o.combo()
  registers[4] = ans
  
def bxl(o: Operand):
  ans = registers[5]^o.literal()
  registers[5] = ans

def bst(o: Operand):
  ans = o.combo() % 8 
  registers[5] = ans

def jnz(o: Operand):
  global instruction_pointer
  if (done_something := registers[4] != 0):
    instruction_pointer = o.literal()
  return done_something

def bxc(o: Operand):
  ans = registers[5]^registers[6]
  registers[5] = ans

def out(o: Operand):
  ans = o.combo() % 8
  #print(f"{ans},", end="")
  outputs.append(ans)

def bdv(o: Operand):
  ans = registers[4] >> o.combo()
  registers[5] = ans

def cdv(o: Operand):
  ans = registers[4] >> o.combo()
  registers[6] = ans

# Register B = operand[5]
# Register A = operand[4]
registers = {x: None for x in range(4,8)}
opcode_table = {
  0: adv,
  1: bxl,
  2: bst,
  3: jnz,
  4: bxc,
  5: out,
  6: bdv,
  7: cdv
}

outputs = []

instruction_pointer = 0

for i, x in enumerate(lines[:3]):
  registers[4+i] = int(x.split(" ")[2])

program = lines[-1].split(" ")[1].split(",")
target = ''.join(map(str, program))


instruction_pointer = 0
outputs = []
registers[4] = 117440
print(f"Program: {target}")
starting_reg = registers[4]
while instruction_pointer <= len(program):
  if instruction_pointer >= len(program): break
  opcode = opcode_table[int(program[instruction_pointer])]
  operand = Operand(int(program[instruction_pointer+1]))
  outcome = opcode(operand)
  if opcode != jnz or not outcome:
    instruction_pointer += 2

stuff = ''.join(map(str, outputs))
binary_str = []

for p in reversed(program):
  binary_str.append(f'{int(p):03b}')

binary_str.append("000")

p2 = int(''.join(binary_str), 2)

print(outputs)
print(p2)

end_time = time.time()

print(f"{end_time-start_time} seconds")