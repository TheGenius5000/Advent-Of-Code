lines = open("D:/GitHub/Advent-Of-Code/2023/Day 15/input.txt").read().replace("\n", "").split(",")
print(lines)

str = "rn=1"
hashes = []

for str in lines:
  if (hash := 0) == 0:
    for c in str:
      hash = ((hash + ord(c)) * 17) % 256
    hashes.append(hash)

print(sum([[(hash := ((hash + ord(c)) * 17) % 256) for c in str ][-1] for str in open("D:/GitHub/Advent-Of-Code/2023/Day 15/input.txt").read().split(",") if (hash := 0) == 0]))