page_ordering = (lines := open("input.txt").read().split("\n\n"))[0].splitlines()
page_numbers = lines[1].splitlines()
total = 0

impossible_numbers = {int(line.split("|")[1]): [] for line in page_ordering}#Numbers that can't exist after the number
incorrect_orderings = []

for line in page_ordering:
  before, after = line.split("|")
  impossible_numbers[int(after)].append(int(before))

for line in page_numbers:
  line = list(map(int, line.split(",")))
  for i, n in enumerate(line[:-1]):
    if n not in impossible_numbers:
      continue
    if any([x in line[i+1:] for x in impossible_numbers[n]]):
      incorrect_orderings.append()
      break
  else:
    total += line[len(line)//2]
    
print(total)
