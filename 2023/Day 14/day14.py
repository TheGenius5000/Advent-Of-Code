import re
lines = [list(x.strip()) for x in open("D:/GitHub/Advent-Of-Code/2023/Day 14/input.txt").readlines()]
lines2 = [list(x.strip()) for x in open("D:/GitHub/Advent-Of-Code/2023/Day 14/input.txt").readlines()]

def move_rocks(lines, rotation):
  changed = True
  while changed:
    changed = False
    for i, x in enumerate(lines[:-1]):
      for j, y in enumerate(x):
        if y == '.':
          if lines[i+1][j] == 'O':
            lines[i][j] = 'O'
            lines[i+1][j] = '.'
            changed = True
  return lines

def shift_rocks(lines):
  new_lines = []
  for s in lines:
    split_line = list(filter(lambda a: a, re.split("(#)", s)))
    to_append = ""
    for n in split_line:
      if 'O' in n:
        n = 'O'*n.count('O')+'.'*n.count('.')
      to_append += n
    new_lines.append(to_append)
  return new_lines

def count_rocks(lines):
  total = 0
  height = len(lines)
  for x in lines:
    total += height*x.count('O')
    height -= 1
  return total

pass
lines = shift_rocks([''.join(x) for x in list(zip(*lines))[::-1]])
#lines2 = [''.join(x) for x in list(zip(*lines2))[::-1]]
#lines2 = list(map(list, list(zip(*lines2))[::-1]))
lines2 = list(map(list, list(zip(*list(zip(*lines2))[::-1]))[::-1]))
#lines2 = list(map(list, list(zip(*list(zip(*lines2))[::-1]))[::-1]))

#lines2 = shift_rocks([''.join(x) for x in list(zip(*lines2[::-1]))])
#lines2 = list(map(list, list(zip(*lines2[::-1]))))
check = count_rocks(list(map(list, list(zip(*list(zip(*lines2))[::-1]))[::-1])))
total1 = count_rocks(list(zip(*lines[::-1])))
print(total1)
last_iter = 0
cycle_point = 1_000_000 % 7
rock_counts = []
base_count = 0
for n in range(1000):
  
  for z in range(4):
    lines2 = shift_rocks([''.join(x) for x in list(zip(*lines2[::-1]))])
  count = count_rocks(list(map(list, list(zip(*list(zip(*lines2))[::-1]))[::-1])))
  # if 81 <= n <= 90:
  #   print(f"{count}, {n}")
  # if n == 81:
  #   base_count = count
  #if count == base_count:
  print(f"Cycle at spin cycle {n+1}: {count}")
  last_iter = n

