import time
import numpy as np

#Given sanitised input, check games and find minimum possible amount for each bag.
#Result given as [red,green,blue], as in RGB
def resultmatrixhelper(results):
    i0 = 1
    min_colours = {
       'r': 0,
       'g': 0,
       'b': 0
    }
    while i0 < len(results):
      for x in results[i0]:
        for i1, c in enumerate(x):
          if not c.isdigit():
            for k, v in min_colours.items():
              if c == k:
                possible_new = int(x[:i1])
                if possible_new > v:
                  min_colours[k] = possible_new
                break
            break
      i0 += 1
    return [min_colours['r'], min_colours['g'], min_colours['b']]

start = time.perf_counter()
with open("input.txt") as f:
    total = 0
    for line in f:
      #This line regularises results of every game into a matrix with index [0] being the game that was played
      reg_result_matrix = [s.replace(" ", "").split(',') for s in line[:-1].replace(":", ";").split(';')]
      total += np.prod(resultmatrixhelper(reg_result_matrix))
    print(total)
end = time.perf_counter()

print(end-start)