row = [[], []]
with open("input.txt", "r") as f:
  for line in f.readlines():
    line = line.split("   ")
    row[0].append(int(line[0]))
    row[1].append(int(line[1][:-1]))

row[0].sort()
row[1].sort()

diff = 0

for i, n in enumerate(row[0]):
  diff += abs(row[0][i] - row[1][i])

print(diff)

number_table = {}

for n in row[0]:
  if n in number_table.keys():
    number_table[n][1] += 1
  else:
    number_table[n] = [0,1]

for n in row[1]:
  if n in number_table.keys():
    number_table[n][0] += 1

sim_score = sum([key*value[0]*value[1] for key, value in number_table.items()])

print(sim_score)

pass