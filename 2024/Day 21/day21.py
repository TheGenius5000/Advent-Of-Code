import time
import io

## Day 21: Keypad Conundrum
## Difficulty: Extreme
## Need-to-know skills: Memoisation, State Pruning, BFS, DFS, Ammortized analysis, 2D movement

## Problem: You are trying to press a keypad with a remote-controlled robot on a remote-controlled D-pad, only that robot is remotely accessed also with another robot 
##          and that other robot is accessed remotely. In summary: Keypad <- Robot <- Robot <- Robot <- You.
##          Part 1: Find the complexity of the sequences of the presses on the D-Pad that you need to make for each keycode you are given.
##          Part 2: The above with 26 robots between you and the keypad.

## Solution: Part 1: For each keycode, work out the complexity sequence by finding the shortest path that presses the keycode, starting at 'A'.
##                   Then for each unit of movement, substitute in the shortest path on the D-pad to press that button, starting at 'A'.
##                   Do this a third time, and you have now what you should press.
##                   The shortest paths are the ones that attempt to move left earliest and least often, as well as moving in the same direction as much as possible.
##           Part 2: Instead of manual substitution, we create a lookup table that remembers the frequency of occurences of one button on the D-pad followed by another.
##                   Then with the knowledge of the shortest paths between any two points, we can add to a new lookup table the same frequency for each connection
##                   of one button to another in the shortest path. Do this 25 times (the inital keypad directions are worked out manually).

## Average runtime: ~ 0.005 seconds

start_time = time.perf_counter()

lines = open("input.txt").read().splitlines()

ans1 = 0
ans2 = 0

numeric_keypad = [['7','8','9'],['4','5','6'],['1','2','3'],[None,'0','A']]
directional_keypad = [[None, '^','A'],['<','v','>']]

dirs_to_instructions = {k:v for k, v in zip([(-1,0), (1,0), (0,-1), (0,1)], ['<','>','^','v'])}
instructions_to_dirs = {k:v for k, v in zip(['<','>','^','v'], [(-1,0), (1,0), (0,-1), (0,1)])}

def unit_vec(vec):
  return 0 if vec == 0 else vec//abs(vec)

def get_the_path(start, end, keypad):
  if start == end: return 'A'
  start_x, start_y = start
  end_x, end_y = end
  delta_x, delta_y = end_x-start_x, end_y-start_y
  need_to_move_queue = []
  if delta_x < 0: 
    need_to_move_queue.append((delta_x,0))
    need_to_move_queue.append((0,delta_y))
  else:
    need_to_move_queue.append((0,delta_y))
    need_to_move_queue.append((delta_x,0))
  x,y = start
  instruction_stream = io.StringIO()
  while need_to_move_queue:
    vec_x, vec_y = need_to_move_queue.pop(0)
    if (vec_x, vec_y) == (0,0): continue
    uvec_x, uvec_y = unit_vec(vec_x), unit_vec(vec_y)
    x, y = x+vec_x, y+vec_y
    if keypad[y][x] is not None: 
      instruction_stream.write(dirs_to_instructions[(uvec_x, uvec_y)]*abs(vec_x+vec_y))
      continue
    need_to_move_queue.append((vec_x, vec_y))
    x, y = x-vec_x, y-vec_y
  instruction_stream.write('A')
  instructions = instruction_stream.getvalue()
  return instructions

def travel_table_builder(keypad):
  return {(button_source, button_dest): get_the_path((i0, j0), (i1,j1), keypad) if not any([button_source is None, button_dest is None]) else None 
          for j0, keypad_row_start in enumerate(keypad) 
          for i0, button_source in enumerate(keypad_row_start) 
          for j1, keypad_row_dest in enumerate(keypad) 
          for i1, button_dest in enumerate(keypad_row_dest)}

def init_travelling_record():
  return {(k,v):0 for keypad_line in directional_keypad for k in keypad_line for keypad_line2 in directional_keypad for v in keypad_line2 if not any(b is None for b in [k,v])}

def press_cascade(numeric_instruction, max_depth):
  travelling_record_old = init_travelling_record()
  travelling_record = init_travelling_record()

  keypad_pos = 'A'
  first_keypad_instruction_stream = io.StringIO()
  for next_button in numeric_instruction:
    first_keypad_instruction_stream.write(travelling_table_numeric[(keypad_pos, next_button)])
    keypad_pos = next_button
  current_instruction = first_keypad_instruction_stream.getvalue()
  
  keypad_pos = 'A'
  for button in current_instruction:
    travelling_record_old[(keypad_pos, button)] += 1
    keypad_pos = button
  
  for _ in range(max_depth-1):
    for k, v in travelling_record_old.items():
      if v == 0: continue
      new_path = travelling_table_directional[k]
      keypad_pos = 'A'
      for b in new_path:
        travelling_record[(keypad_pos, b)] += v
        keypad_pos = b
    travelling_record_old = travelling_record
    travelling_record = init_travelling_record()

  return sum(travelling_record_old.values())


travelling_table_numeric = travel_table_builder(numeric_keypad)
travelling_table_directional = travel_table_builder(directional_keypad)

for instruction in lines:
  sequence_3robots = press_cascade(instruction, 3)
  sequence_26robots = press_cascade(instruction, 26)
  numeric_code = int(instruction[:-1])
  ans1 += numeric_code*sequence_3robots
  ans2 += numeric_code*sequence_26robots

print(ans1)
print(ans2)

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")