lines = open("D:/GitHub/Advent-Of-Code/2023/Day 15/input.txt").read().replace("\n", "").split(",")
print(lines)

str = "rn=1"
hashes = []

def holidayASCIIStringHelper(str):
  hash = 0
  for c in str:
    hash = ((hash + ord(c)) * 17) % 256
  return hash

print(sum([[(hash := ((hash + ord(c)) * 17) % 256) for c in str ][-1] for str in open("D:/GitHub/Advent-Of-Code/2023/Day 15/input.txt").read().split(",") if (hash := 0) == 0]))

boxes = [[] for x in range(256)]

for command in lines:
  
  if '=' in command:
    lens, focal_length = command.split('=')
    label = holidayASCIIStringHelper(lens)
    changed = False
    for i, local_lens in enumerate(boxes[label]):
      if local_lens[0] == lens:
        boxes[label][i] = lens, focal_length
        changed = True
        break
    if not changed:
      boxes[label].append((lens, focal_length))
  elif '-' in command:
    lens = command[:-1]
    label = holidayASCIIStringHelper(lens)
    for i, x in enumerate(boxes[label]):
      if x[0] == lens:
        del boxes[label][i]
        break

#print(boxes)

total = 0
for label, box in enumerate(boxes):
  for i, (_, focal_length) in enumerate(box):
    total += (label+1)*(i+1)*int(focal_length)

print(total)