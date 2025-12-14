import time
import numpy as np
from itertools import chain, combinations, product
from operator import sub


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


## Day 10 -  Factory
## Average runtime: ~

start_time = time.perf_counter()

with open(r"D:\GitHub\Advent-Of-Code\2025\Day 10\input_test.txt") as f:
  lines = [x.split() for x in f.read().splitlines()]

## Part 1
# Problem: You are given an indicator blue print and a set of buttons that activate mutliple switches. What is the minimum number of button presses to activate the lights in the way seen in the diagram?

# Solution: After parsing the input into Machine classes, find the combination of button presses reqiured. Since it is on or off, each button needs only be pressed once at most. You can look through the powerset of buttons, smallest first, to find the right ones.

class Machine():
  def __init__(self, diagram: tuple, schematics: list, joltage: list):
    self.diagram = diagram
    self.schematics = schematics
    self.joltage = joltage
  def __repr__(self):
    return f"Machine (Diagram: {self.diagram}, Schematics: {self.schematics}, Joltage: {self.joltage})"

def manual_maker(lines):
  manual = []
  for line in lines:
    inp_diagram, inp_schematics, inp_joltage = line[0], line[1:-1], line[-1]
    temp_diagram = tuple(1 if x == "#" else 0 for x in inp_diagram[1:-1])
    temp_schematics = [tuple(map(int, x[1:-1].split(","))) for x in inp_schematics]
    temp_joltage = tuple(map(int, inp_joltage[1:-1].split(",")))
    manual.append(Machine(temp_diagram, temp_schematics, temp_joltage))
  return manual


def machine_input_finder(manual):
  machine_inputs = []
  for machine in manual:
    for button_press_set in powerset(machine.schematics):
      machine_lights = [0]*len(machine.diagram)
      for button_presses in button_press_set: 
        for button_press in button_presses: machine_lights[button_press] = (machine_lights[button_press]+1)%2
      if tuple(machine_lights) == machine.diagram:
        machine_inputs.append(button_press_set)
        break
  return machine_inputs

manual = manual_maker(lines)
machine_inputs = machine_input_finder(manual)

ans1 = sum(map(len, machine_inputs))

print(f"The least number of button presses is {ans1}.")

## Part 2
# Problem: What is the least amount of button presses required for each of the machines to match the joltages listed? Each button press adds 1 joltage to its respective light.

# Solution: We can perform gaussian elimination on the joltages and the buttons. With the requirement that each button press cannot be less than 0, we can then add restrictions to find the minimum for each button press.

ans2 = 0

#Returns an augmented matrix of the linear equations created by button presses
def initialise_matrix(machine: Machine):
  matrix = np.c_[np.zeros((len(machine.joltage), len(machine.schematics)), dtype=np.int_), np.array(machine.joltage).T]
  for j, button in enumerate(machine.schematics):
    for light in button: 
      matrix[light][j] = 1
  return np.unique(matrix, axis=0)

#Find index of next available pivot, exlude already known pivots. None if variable is free
def find_pivot_row(matrix, j, pivot_rows):
  for i, row in enumerate(matrix):
    if any([i in pivot_rows, row[j] not in {-1, 1}]): continue
    return i
  return None

#Chooses and removes all variables outside of a given column.
def pivot_calc(matrix, pivot_row, pivot_column):
  if matrix[pivot_row][pivot_column] == -1: matrix[pivot_row] *= -1
  for i, row in enumerate(matrix):
    if any([i == pivot_row, row[pivot_column] == 0]): continue
    if row[pivot_column] > 0: matrix[i] -= matrix[pivot_row]
    elif row[pivot_column] < 0: matrix[i] += matrix[pivot_row]
  return matrix

#Generates a 2d-dictionary that describes the equations of the pivots
def equation_maker(pivots: dict, matrix):
  equations = dict()
  for row, column in pivots.items():
    if column is None: continue
    equations[column] = dict()
    equations[column] = {i: x*-1 for i, x in enumerate(matrix[column][:-1]) if not any([i == row, x == 0])}
    equations[column][len(matrix[column])-1] = matrix[column][-1]
  return equations


for machine in manual:
  matrix = initialise_matrix(machine)
  solution_slot = len(machine.schematics)
  pivots = dict() #{column index: row index (None if free)}
  for pivot_column, _ in enumerate(machine.schematics):
    pivots[pivot_column] = find_pivot_row(matrix, pivot_column, pivots.values())
    if pivots[pivot_column] is None: continue
    matrix = pivot_calc(matrix, pivots[pivot_column], pivot_column)
  equations = equation_maker(pivots, matrix)
  additions = dict()
  for d in equations.values():
    for k, v in d.items():
      if k not in additions: additions[k] = int(v)
      else: additions[k] += int(v)
  for k, v in pivots.items():
    if v is None: additions[k] += 1
  free_vars = [k for k, v in pivots.items() if v is None]
  inequalities = dict()
  for column in matrix:
    free_var_vector = tuple(x for i, x in enumerate(column) if i in free_vars)
    if (free_var_vector not in inequalities) or (inequalities[free_var_vector] > column[solution_slot]):
      inequalities[free_var_vector] = int(column[solution_slot])
  restrictions = {k: [0, None] for k in free_vars}
  for i, free_var in enumerate(free_vars):
    one_hot_tuple = tuple(1 if x == free_var else 0 for x in free_vars)
    happy = False
    for n in range(1,5):
      if (tuple_key := tuple(x*n for x in one_hot_tuple)) in inequalities: 
        restrictions[free_var][1] = int(inequalities[tuple_key])//n
        happy=True
        break
    one_hot_tuple_neg = tuple(-1 if x == free_var else 0 for x in free_vars)
    for n in range(-1, -5, -1):
      if (tuple_key := tuple(x*n for x in one_hot_tuple_neg)) in inequalities:
        if (lower_bound := -int(inequalities[tuple_key])) > 0: 
          restrictions[free_var][0] = lower_bound//n
          break
    if happy: continue
    restrictions[free_var][1] = [(v, tuple((-int(x),ind) for ind, (x,y) in enumerate(zip(k, free_vars)) if y != free_var)) for k, v in inequalities.items() if k[i] != 0]
  smallest = float("inf")
  for stuff in product(*restrictions.values()):
    cleaned_stuff = []
    val = additions[solution_slot]
    for s in stuff:
      if isinstance(s, int):
        cleaned_stuff.append(s)
        continue
      x, s = s[0]
      x += sum(x*stuff[y] for x,y in s)
      cleaned_stuff.append(x)
    for x,y in zip(cleaned_stuff, free_vars):
      val += additions[y]*x
    if val < smallest: smallest = val
  print(smallest)
  ans2 += smallest

  #print("Gap...............")


print(ans2)



end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")