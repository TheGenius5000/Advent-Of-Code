import numpy as np

lines = [tuple(x.split()) for x in open("D:/GitHub/Advent-Of-Code/2023/Day 18/input.txt").read().splitlines()]

print(lines)

x_coords = []
y_coords = []
x = 0
y = 0
real_codes = [bla[2][2:-1] for bla in lines]
commands = []
lengths = []
print(real_codes)
#shape = [['.' for x in range(7)] for y in range(10)]

for real_code in real_codes:
  amount = int(real_code[:-1], 16)
  lengths.append(amount)
  command = ""
  match int(real_code[-1]):
    case 0:
      command += "R "
      x += amount
    case 2:
      command += "L "
      x -= amount
    case 1:
      command += "D "
      y += amount
    case 3:
      command += "U "
      y -= amount
  command += str(amount)
  commands.append(command)
  x_coords.append(x)
  y_coords.append(y)

length = sum(lengths)

lengths_old =sum([int(x[1]) for x in lines])
#Shoelace formula
x_coords = np.asarray(x_coords, dtype=np.longlong)
y_coords = np.asarray(y_coords, dtype=np.longlong)
A = 0.5*np.abs(np.dot(x_coords, np.roll(y_coords, 1)) - np.dot(y_coords, np.roll(x_coords, 1)))
#Pick's theorem
i = A+1-length/2

print(i+length)

