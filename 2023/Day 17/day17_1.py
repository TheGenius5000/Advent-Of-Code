import time
import heapq
from enum import Enum

start = time.perf_counter()
losses = [list(map(int, list(x))) for x in open("D:/GitHub/Advent-Of-Code/2023/Day 17/test.txt").read().splitlines()]

directions = {
  "W": (-1, 0),
  "E": (1, 0),
  "S": (0, 1),
  "N": (0, -1)
}

directions_as_num = {
  "W": 0,
  "E": 1,
  "S": 2,
  "N": 3,
}

backtracks = {
  "E": "W",
  "W": "E",
  "N": "S",
  "S": "N"
}

class Stuff:
  average = sum([sum(x)/len(x) for x in losses])/len(losses)
  end = (len(losses[0])-1, len(losses)-1)
  def get_heuristic(x, y):
    return (abs(Stuff.end[0]-x)+abs(Stuff.end[1]-y))

class State:
  def __init__(self, x, y, dir, dir_amount, total_cost, astar_score, h_n) -> None:
    self.x = x
    self.y = y
    self.direction = dir
    self.dir_amount = dir_amount
    self.total_cost = total_cost
    self.f_n = astar_score
    self.h_n = h_n
  def __lt__(self, other):
    return self.f_n < other.f_n
  def __repr__(self) -> str:
    return f"""(({self.x},{self.y}), Heuristic - {self.h_n}, A*: {self.f_n} "{self.direction}", {self.dir_amount})"""


visited = [[[[False for _ in range(3)] for _ in directions_as_num.keys()] for _ in range(len(losses[0]))] for _ in range(len(losses))]
priority_queue = []
heapq.heappush(priority_queue, State(0, 0, "E", 0, 0, 0, 0))

while True:
  current_state = heapq.heappop(priority_queue)
  if (current_state.x, current_state.y) == Stuff.end: 
    break
  if current_state.dir_amount != 0:
    visited[current_state.y][current_state.x][directions_as_num[current_state.direction]][current_state.dir_amount-1] = True
  for direction, (dir_x, dir_y) in directions.items():
    if current_state.direction == backtracks[direction]: continue
    next_x = current_state.x+dir_x
    next_y = current_state.y+dir_y
    if any([next_x < 0, next_y < 0, next_x > Stuff.end[0], next_y > Stuff.end[1]]): continue
    new_dir_amount = 1+current_state.dir_amount if direction == current_state.direction else 1
    if new_dir_amount > 3 or visited[next_y][next_x][directions_as_num[direction]][new_dir_amount-1]: continue
    h_n = Stuff.get_heuristic(next_x, next_y)
    g_n = losses[next_y][next_x] + current_state.total_cost
    heapq.heappush(priority_queue, State(next_x, next_y, direction, new_dir_amount, g_n, h_n+g_n, h_n))
  
print(current_state.total_cost)
end = time.perf_counter()
print(end-start)