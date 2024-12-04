import itertools

lines = open("input.txt").read().splitlines()
lines_t = [''.join(x) for x in [*zip(*lines)]]

def diagonalLines(lines):
  canvas = []
  for diagonal, coords in itertools.groupby(sorted(itertools.product(range(len(lines)), repeat=2), key=sum), key=sum,):#Diagonal co-ordinates
    diag_line = []
    for x,y in [*coords]:
      diag_line.append(lines[y][x])
    canvas.append(diag_line.copy())
  return [''.join(x) for x in canvas]

lines_diag = diagonalLines(lines)
lines_diag_t = diagonalLines(list(reversed(lines)))
x_mas_total = 0

# for line in lines_diag_t:
#   print(line)

# for line in lines_diag:
#   print(line)

print(sum([(find_xmas := lambda lines: sum([x.count('XMAS')+x.count('SAMX') for x in lines]))(lines), find_xmas(lines_t), find_xmas(lines_diag), find_xmas(lines_diag_t)]))

for y in range(1, len(lines)-1):
  for x in range(1, len(lines[0])-1):
    if lines[y][x]=='A':
      if any([all([lines[y-1][x-1] == 'M', lines[y-1][x+1] == 'S', lines[y+1][x-1] == 'M', lines[y+1][x+1] == 'S']),
all([lines[y-1][x-1] == 'M', lines[y-1][x+1] == 'M', lines[y+1][x-1] == 'S', lines[y+1][x+1] == 'S']),
all([lines[y-1][x-1] == 'S', lines[y-1][x+1] == 'M', lines[y+1][x-1] == 'S', lines[y+1][x+1] == 'M']),
all([lines[y-1][x-1] == 'S', lines[y-1][x+1] == 'S', lines[y+1][x-1] == 'M', lines[y+1][x+1] == 'M'])]):
        x_mas_total += 1

print(x_mas_total)