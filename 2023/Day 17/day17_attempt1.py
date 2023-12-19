import numpy as np
import threading
import time

sem = threading.Semaphore(1)
start = time.perf_counter()
losses = [list(map(int, list(x))) for x in open("D:/GitHub/Advent-Of-Code/2023/Day 17/input.txt").read().splitlines()]
losses[0][0] = 0

end = (len(losses[0])-1, len(losses)-1)
journeys = []
min = 830
co_ords = [(x, y) for x in range(len(losses[0])) for y in range(len(losses))]
lowest_paths = dict.fromkeys(co_ords, float('inf'))

#@functools.cache
def traversal(location, dircetion_amount, direction, loss):
  global min
  global max_moves
  x, y = location
  if any([loss > min, y < 0, y > end[1], x < 0, x > end[0]]):
    return
  loss += losses[y][x]
  sem.acquire()
  if lowest_paths[location] < loss and location != (0,0):
    sem.release()
    return
  else:
    lowest_paths[location] = loss
    sem.release()

  if location == end:
    journeys.append(loss)
    print(loss)
    return
  match direction:
    case "S":
      if dircetion_amount < 3:
        traversal((x, y+1), dircetion_amount+1, "S", loss)
      traversal((x+1, y), 1, "E", loss)
      traversal((x-1, y), 1, "W", loss)
    case "N":
      if dircetion_amount < 3 and y > 0:
        traversal((x, y-1), dircetion_amount+1, "N", loss)
      traversal((x+1, y), 1, "E", loss)
      traversal((x-1, y), 1, "W", loss)
    case "E":
      if dircetion_amount < 3 and x < end[0]:
        traversal((x+1, y), dircetion_amount+1, "E", loss)
      traversal((x, y+1), 1, "S", loss)
      traversal((x, y-1), 1, "N", loss)
    case "W":
      if dircetion_amount < 3 and x > 0:
        traversal((x-1, y), dircetion_amount+1, "W", loss)
      traversal((x, y+1), 1, "S", loss)
      traversal((x, y-1), 1, "N", loss)


# for x in ["E", "S", "N", "W"]:
#   traversal((0,0), 1, x, -2)

# t1 = threading.Thread(target=traversal, args=((0,0), 0, "E", 0))
# t2 = threading.Thread(target=traversal, args=((0,0), 0, "S", 0))


# t1.start()
# t2.start()

# t1.join()
# t2.join()


# traversal((0,0), 0, "S", 0)
# print(sorted(journeys))
# #journeys = []
# lowest_paths = lowest_paths.fromkeys(co_ords, float('inf'))
# traversal((0,0), 0, "E", 0)
      
average = np.average([np.average(x) for x in losses])
end = time.perf_counter()
print(end-start)