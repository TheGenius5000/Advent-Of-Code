import time
import re

start_time = time.time()

def displayGrid(grid):
  for line in grid:
    print(''.join(line))
  print(f"\n")

def doubleUp(line):
  for old, double in [('#', '##'), ('O', '[]'), ('.', '..'), ('@','@.')]:
    line = line.replace(old, double)
  return line

def closesBox(ch1, ch2):
  return ch1 == '[' and ch2 == ']'

def moveStuffAround(old_x, old_y, vec_x, vec_y):
  global grid
  new_x, new_y = old_x+vec_x, old_y+vec_y
  moving_ch = grid[old_y][old_x]
  displaced_ch = grid[new_y][new_x]
  grid[old_y][old_x] = displaced_ch
  grid[new_y][new_x] = moving_ch
  return (displaced_ch, moving_ch)

grid, directions = ((lines := [x.splitlines()for x in open("input.txt").read().split("\n\n")])[0], lines[1])
directions = [x for d in directions for x in d]
grid = [list(doubleUp(line)) for line in grid]

displayGrid(grid)

directions_dict = {k: v for k, v in zip(['<', '>', '^', 'v'], [(-1,0), (1,0), (0,-1), (0,1)])}
robot_x, robot_y = [(i,j) for j, line in enumerate(grid) for i, ch in enumerate(line) if ch == '@'][0]

for iteration, dir in enumerate(directions):
  vec_x, vec_y = directions_dict[dir]
  x, y = robot_x, robot_y
  if dir in '<>':
    to_move = [(x,y)]
  elif dir in '^v':
    to_move = dict({x:[y]})
  forces_queue = [(x, y)]
  visited_columns = set([y])
  while forces_queue:
    x, y = x+vec_x, y+vec_y
    if dir in '<>':
      if (x,y) in to_move: continue
    elif dir in '^v': 
      if x in to_move: 
        if y in to_move[x]: continue
    if grid[y][x] == "#":
      to_move = []
      forces_queue = []
      break
    elif grid[y][x] == '.':
      forces_queue.pop(0)
      if forces_queue: x, y = forces_queue[0]
    elif grid[y][x] in '[]': 
      if dir in '<>': to_move.append((x,y))
      elif dir in '^v': to_move[x].append(y)
      for which_side, correct_ch in [(-1, '['),(1, ']')]:
        if grid[y][(sprouted_x := x+which_side)] == correct_ch: 
          if dir in '<>':
            to_move.append((sprouted_x, y))
          elif dir in '^v' and sprouted_x not in to_move: 
            to_move[x+which_side] = [y]
          else:
            to_move[x+which_side].append(y)
          forces_queue.append((sprouted_x,y))
  if to_move: robot_x, robot_y = robot_x+vec_x, robot_y+vec_y
  else: continue
  if dir in '<>':
    for old_x, old_y in to_move[::-1]:
      displaced_ch, moving_ch = moveStuffAround(old_x, old_y, vec_x, vec_y)
  elif dir in '^v':
    for old_x, ys in to_move.items():
      displaced_ch = '.'
      if dir == '^': ys = sorted(ys)
      elif dir == 'v': ys = sorted(ys)[::-1]
      for old_y in ys:
        displaced_ch, moving_ch = moveStuffAround(old_x, old_y, vec_x, vec_y)

displayGrid(grid)

box_coords = [(i,j) for j, line in enumerate(grid) for i, ch in enumerate(line) if ch == 'O']

print(sum([100*j+i for j, line in enumerate(grid) for i, ch in enumerate(line) if ch == '[']))

end_time = time.time()

print(f"{end_time-start_time} seconds")