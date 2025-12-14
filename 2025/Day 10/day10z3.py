import time
import z3
from itertools import chain, combinations, product


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

start_time = time.perf_counter()

with open(r"D:\GitHub\Advent-Of-Code\2025\Day 10\input.txt") as f:
  lines = [x.split() for x in f.read().splitlines()]

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

def a_offset(i):
  return f"{chr(ord("a")+i)}"

manual = manual_maker(lines)
machine_inputs = machine_input_finder(manual)

ans1 = sum(map(len, machine_inputs))

print(f"The least number of button presses is {ans1}.")

ans2 = 0

for machine in manual:
  vars = [z3.Int(a_offset(i)) for i, x in enumerate(machine.schematics)]
  matrix = [[0 for _ in range(len(machine.schematics))] for _ in range(len(machine.joltage))]
  solver = z3.Solver()
  solver.add(*(v >= 0 for v in vars))
  for i, button in enumerate(machine.schematics):
    for light in button: matrix[light][i] = 1
  for row, joltage in zip(matrix, machine.joltage):
    stuff_to_consider = []
    for i, x in enumerate(row):
      if x == 1: stuff_to_consider.append(i)
    solver.add(z3.Sum([vars[x] for x in stuff_to_consider]) == joltage)
  while solver.check() == z3.sat:
    model = solver.model()
    answer = sum([model.evaluate(v, model_completion=True).as_long() for v in vars])
    solver.add(z3.Sum(vars) < answer)
  ans2 += answer

print(ans2)

  
end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")