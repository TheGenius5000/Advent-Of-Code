import numpy as np
import time

wins = []
total = 0

start = time.perf_counter()
with open("input.txt") as f:
  wins = list(map(lambda x: (len([n for n in x[0] if n in x[1]])),list(map(lambda x: list(map(lambda y: y.split(), x)) ,list(map(lambda x: x.split(":")[1].split("|"), list(map(lambda x: x.strip("\n"), f.readlines()))))))))

scratchcard_instances = np.ones((len(wins)), dtype=int)

for i, win in enumerate(wins):
  total += scratchcard_instances[i]
  scratchcard_instances[i+1:i+win+1] += scratchcard_instances[i]

print(total)
end = time.perf_counter()
print(end-start)