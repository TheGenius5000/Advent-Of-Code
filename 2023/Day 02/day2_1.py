import time
import re
import numpy as np

#Given sanitised input, check games and find minimum possible amount for each bag.
def resultmatrixhelper(results, max_red, max_green, max_blue):
    i0 = 1
    colours = {
       'r': max_red,
       'g': max_green,
       'b': max_blue
    }
    while i0 < len(results):
      for x in results[i0]:
        for i1, c in enumerate(x):
          if not c.isdigit():
            for k, v in colours.items():
              if c == k:
                if int(x[:i1]) > v:
                    return 0 
            break              
      i0 += 1
    #We should have successfully proven that the game is under the maxs at this point
    game_id = int(re.findall("\d+", results[0][0])[0])
    return game_id

start = time.perf_counter()
with open("input.txt") as f:
    total = 0
    max_red = 12
    max_green = 13
    max_blue = 14
    for line in f:
        #This line regularises results of every game into a matrix with index [0] being the game that was played
        reg_result_matrix = [s.replace(" ", "").split(',') for s in line[:-1].replace(":", ";").split(';')]
        total += resultmatrixhelper(reg_result_matrix, max_red, max_green, max_blue)
    print(total)
end = time.perf_counter()

print(end-start)