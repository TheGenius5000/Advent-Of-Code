import itertools
import time

start_time = time.time()

encoding = "14113"
#encoding = "2333133121414131402" 
encoding = open("D:\\GitHub\\Advent-Of-Code\\2024\\Day 9\\input.txt").read().strip("\n")

encoding = list(map(int, encoding))
id = -1
memory_block = ['.' if i%2 == 1 else str(i//2) for (i, n) in enumerate(encoding) for _ in range(n)]
memory_block2 = [(x, len(list((y)))) for x, y in itertools.groupby(memory_block.copy())]
encoded_memory_block = ""
checksum = 0
header = 0
total2 = 0
total1 = 0

#print(encoding)z

if any([x[0] == '.' for x in memory_block]):
  for i, mem in enumerate(memory_block[::-1]):
    if memory_block.index('.') > len(memory_block)-i-1:
      #memory_block = memory_block[:len(memory_block)-i+1]
      break
    if mem == '.': continue
    memory_block[memory_block.index('.')], memory_block[len(memory_block)-i-1] = mem, '.'

  i = len(memory_block2)

  while i > [i for i, x in enumerate(memory_block2) if x[0] == '.'][0]:
    i -= 1
    mem, size = memory_block2[i]
    if mem == '.': continue
    for j, (orig_mem, orig_size) in enumerate(memory_block2[:i]):
      if orig_mem != '.': continue
      if orig_size < size: continue
      leftover = orig_size-size
      memory_block2[j] = (mem, size)
      memory_block2[i] = ('.', size)
      if leftover > 0: 
        memory_block2[j+1:j+1] = [('.', leftover)]
        i += 1
      break
  
for mem, size in memory_block2:
  if mem in '.':
    header += size
    continue
  for n in range(size):
    total2 += int(mem)*header
    header += 1

header = 0

print(sum([int(ch)*i for i, ch in enumerate(filter(lambda x: x != '.', memory_block))]))
print(total2)
print(total1)
pass

end_time = time.time()

print(f"{end_time-start_time} seconds")