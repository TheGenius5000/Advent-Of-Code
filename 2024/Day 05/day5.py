page_ordering = (lines := open("input.txt").read().split("\n\n"))[0].splitlines()
page_numbers = [list(map(int, line.split(","))) for line in lines[1].splitlines()]
total = 0

impossible_numbers = {int(line.split("|")[1]): [] for line in page_ordering}#Numbers that can't exist after the number
incorrect_orderings = []

for line in page_ordering:
  before, after = line.split("|")
  impossible_numbers[int(after)].append(int(before))

for i, line in enumerate(page_numbers):
  for j, n in enumerate(line[:-1]):
    if n not in impossible_numbers:
      continue
    if any([x in line[j:] for x in impossible_numbers[n]]):
      incorrect_orderings.append(i)
      break
  else:
    total += line[len(line)//2]
    
print(total)

corrected_lines = []

for i in incorrect_orderings:#Merge sort
  line = [[j] for j in page_numbers[i]]#Split for merge sort
  while len(line) > 1:
    new_list = []
    for j in range(0, len(line), 2):
      if j+1 == len(line):
        new_list.append(line[j])
        continue
      list_one, list_two = (line[j], line[j+1])
      temp_list = [None]*(len(list_one+list_two))
      list2_watch = list_two.copy()#List for considering potentially larger values
      for index, n in enumerate(list_one):
        offset = temp_list.index(list_one[index-1]) if index > 0 else -1
        if n not in impossible_numbers:
          temp_list[offset+1] = n
          continue
        temp_list[offset+1 + (commonality := len(set(impossible_numbers[n]) & set(list2_watch)))] = n
        list2_watch = list2_watch[commonality:]
      for n in list_two:
        temp_list[temp_list.index(None)] = n
      new_list.append(temp_list)
    line = new_list.copy()
  corrected_lines += line

#print(corrected_lines)

print(sum([line[len(line)//2] for line in corrected_lines]))
        
pass
