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

(diagonal := lambda lines: [''.join(x) for x in [[lines[y][x] for x, y in [*coords]] for diagonal, coords in itertools.groupby(sorted(itertools.product(range(len(lines)), repeat=2), key=sum), key=sum,)]])

print(sum([(find_xmas := lambda lines: sum([x.count('XMAS')+x.count('SAMX') for x in lines]))(lines), find_xmas(lines_t), find_xmas(lines_diag), find_xmas(lines_diag_t)]))
print(sum([(find_xmas := lambda lines: sum([x.count('XMAS')+x.count('SAMX') for x in lines]))((lines := open("input.txt").read().splitlines())), find_xmas([''.join(x) for x in [*zip(*lines)]]), find_xmas((diagonal := lambda lines: [''.join(x) for x in [[lines[y][x] for x, y in [*coords]] for diagonal, coords in itertools.groupby(sorted(itertools.product(range(len(lines)), repeat=2), key=sum), key=sum,)]])(lines)), find_xmas(diagonal(list(reversed(lines))))]))

for y in range(1, len(lines)-1):
  for x in range(1, len(lines[0])-1):
    if lines[y][x]=='A':
      if any([all([lines[y-1][x-1] == 'M', lines[y-1][x+1] == 'S', lines[y+1][x-1] == 'M', lines[y+1][x+1] == 'S']),
all([lines[y-1][x-1] == 'M', lines[y-1][x+1] == 'M', lines[y+1][x-1] == 'S', lines[y+1][x+1] == 'S']),
all([lines[y-1][x-1] == 'S', lines[y-1][x+1] == 'M', lines[y+1][x-1] == 'S', lines[y+1][x+1] == 'M']),
all([lines[y-1][x-1] == 'S', lines[y-1][x+1] == 'S', lines[y+1][x-1] == 'M', lines[y+1][x+1] == 'M'])]):
        x_mas_total += 1

#sum([len((lines := open("D:\\GitHub\\Advent-Of-Code\\2024\\Day 4\\input.txt").read().splitlines()))]+[1 for x in range(1, len((lines := open("D:\\GitHub\\Advent-Of-Code\\2024\\Day 4\\input.txt").read().splitlines())[0]-1)) for y in range(1, len(lines)-1) if (xmas_cross := lambda x,y,a,b,c,d,lines: all(lines[x][y] == 'A' lines[y-1][x-1] == a, lines[y-1][x+1] == b, lines[y+1][x-1] == c, lines[y+1][x+1] == d))(x,y,'M','S','M','S')])

print(x_mas_total)