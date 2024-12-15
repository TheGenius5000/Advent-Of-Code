import time

start_time = time.time()

grid, directions = ((lines := [list(map(list, x.splitlines())) for x in open("D:\\GitHub\\Advent-Of-Code\\2024\\Day 15\\input.txt").read().split("\n\n")])[0], lines[1])
directions = [x for d in directions for x in d]

def display_grid(grid):
  for line in grid:
    print(''.join(line))
  print(f"\n")

print("Start")
display_grid(grid)

directions_dict = {k: v for k, v in zip(['<', '>', '^', 'v'], [(-1,0), (1,0), (0,-1), (0,1)])}
robot_x, robot_y = [(i,j) for j, line in enumerate(grid) for i, ch in enumerate(line) if ch == '@'][0]

for dir in directions:
  #print (f"Move {dir}:")
  vec_x, vec_y = directions_dict[dir]
  x, y = robot_x, robot_y
  stack = [(x, y)]
  while True:
    x, y = x+vec_x, y+vec_y
    if grid[y][x] == "#":
      stack = []
      break
    elif grid[y][x] == '.': break
    elif grid[y][x] == 'O': stack.append((x,y))
  if stack: robot_x, robot_y = stack[0][0]+vec_x, stack[0][1]+vec_y
  for old_x, old_y in stack[::-1]:
    new_x, new_y = old_x+vec_x, old_y+vec_y
    moving_ch = grid[old_y][old_x]
    displaced_ch = grid[new_y][new_x]
    grid[old_y][old_x] = displaced_ch
    grid[new_y][new_x] = moving_ch

display_grid(grid)
box_coords = [(i,j) for j, line in enumerate(grid) for i, ch in enumerate(line) if ch == 'O']

print(sum([100*j+i for j, line in enumerate(grid) for i, ch in enumerate(line) if ch == 'O']))

end_time = time.time()

print(f"{end_time-start_time} seconds")