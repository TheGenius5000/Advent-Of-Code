lines = [list(map(list,x.split("\n"))) for x in open("D:/GitHub/Advent-Of-Code/2023/Day 13/test.txt").read().split("\n\n")]
total = 0

found = False

def find_mirror_index(pattern):
  global found
  prev = ''
  for i, x in enumerate(pattern):
      if x == prev:
        front = i
        back = i-1
        while True:
          try:
            if pattern[front] != pattern[back]: break
          except:
            return i
          front += 1
          back -= 1
          if back < 0: return i
      prev = x
  return 0

for ind, pattern in enumerate(lines):
  rows = []
  column_lines = []
  #columns = [''.join(y[i] for y in pattern) for i, x in enumerate(pattern[0])]
  #matches_rows = [[j for j, y in enumerate(pattern) if y == x and i != j] for i, x in enumerate(pattern)]
  for x, row in enumerate(pattern):
    for y, ch in enumerate(row):
      prev_val = pattern[x][y]
      pattern[x][y] = '#' if pattern[x][y] == '.' else '.'
      mirror_rows = find_mirror_index(pattern)
      total += mirror_rows*100
      columns = [[y[i] for y in pattern] for i, _ in enumerate(pattern[0])]
      #matches_columns = [[j for j, y in enumerate(columns) if y == x and i != j] for i, x in enumerate(columns)]
      rows.append(mirror_rows)
      mirror_columns = find_mirror_index(columns)
      total += mirror_columns
      column_lines.append(mirror_columns)
      pattern[x][y] = '#' if pattern[x][y] == '.' else '.'
      pass
  pass
  #print(f"Rows: {find_mirror_index(pattern)}")
  #print(f"Columns: {find_mirror_index(columns)}\n")

print(total)