import collections

lines = [x.split("\n") for x in open("D:/GitHub/Advent-Of-Code/2023/Day 13/input.txt").read().split("\n\n")]
#lines = [list(map(list, x)) for x in lines]
total = 0
rows = []
column_lines = []


def find_another_mirror_index(pattern, front, back):
  difference = 0
  while True:
    try:
      difference += sum([pattern[front][i] != pattern[back][i] for i in range(len(pattern[front]))])
    except:
      return difference
    if difference > 1:
      return difference
    back -= 1
    front += 1
    if back < 0: return difference

def find_mirror_index(pattern):
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
  return None

for ind, pattern in enumerate(lines):
  #columns = [''.join(y[i] for y in pattern) for i, x in enumerate(pattern[0])]
  #matches_rows = [[j for j, y in enumerate(pattern) if y == x and i != j] for i, x in enumerate(pattern)]
  mirror_rows = find_mirror_index(pattern)
  total += mirror_rows*100 if mirror_rows else 0
  columns = [''.join(y[i] for y in pattern) for i, x in enumerate(pattern[0])]
  #matches_columns = [[j for j, y in enumerate(columns) if y == x and i != j] for i, x in enumerate(columns)]
  rows.append(mirror_rows)
  mirror_columns = find_mirror_index(columns)
  total += mirror_columns if mirror_columns else 0
  column_lines.append(mirror_columns)
  pass
  #print(f"Rows: {find_mirror_index(pattern)}")
  #print(f"Columns: {find_mirror_index(columns)}\n")

print(total)
iter1 = []
for i, x in enumerate(column_lines):
  if x:
    iter1.append((x, "Col"))
  else:
    iter1.append((rows[i], "Row"))

total2 = 0
total1 = 0
iter2 = []

for ind, pattern in enumerate(lines):
  permutations_row = []
  permutations_col = []
  columns = [[y[i] for y in pattern] for i, _ in enumerate(pattern[0])]
  for i in range(len(pattern)-1):
    permutations_row.append(find_another_mirror_index(pattern, i+1, i))
  for i in range(len(columns)-1):
    permutations_col.append(find_another_mirror_index(columns, i+1, i))
  
  if 0 in permutations_col:
    total1 += permutations_col.index(0)+1
  if 0 in permutations_row:
    total1 += (permutations_row.index(0)+1)*100
  if 1 in permutations_col:
    total2 += permutations_col.index(1)+1
  if 1 in permutations_row:
    total2 += (permutations_row.index(1)+1)*100
  #for x, row in enumerate(pattern):


    # for y, ch in enumerate(row):
    #   new_match = ()
    #   pattern[x][y] = '#' if pattern[x][y] == '.' else '.'
    #   mirror_rows = find_mirror_index(pattern)
    #   #total += mirror_rows*100 if mirror_rows else 0
    #   columns = [[y[i] for y in pattern] for i, _ in enumerate(pattern[0])]
    #   #matches_columns = [[j for j, y in enumerate(columns) if y == x and i != j] for i, x in enumerate(columns)]
    #   mirror_columns = find_mirror_index(columns)
    #   if mirror_columns or mirror_rows:
    #     new_match = (mirror_rows, "Row") if mirror_rows else (mirror_columns, "Col")
    #   #total += mirror_columns if mirror_columns else 0
    #   column_lines.append(mirror_columns)
    #   if new_match != this_match and new_match != ():
    #     changed = True
    #     iter2.append(new_match)
    #     break
    #   pattern[x][y] = '#' if pattern[x][y] == '.' else '.'
    #   pass
    # else:
    #   continue
    # break

  """items = []
  change = False
  for x in rows:
    items.append((x, "Row"))
  for x in column_lines:
    items.append((x, "Col"))
  val = iter1[ind]
  items.remove(val)
  try:
    val = items[0]
    change = True
  except:
    change = False
    pass
  if val[1] == "Row":
    total += val[0]*100
  else:
    total += val[0]
  pass """
  


print(total1, total2)