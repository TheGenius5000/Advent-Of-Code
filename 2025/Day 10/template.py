import time
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


## Day 10 -  Factory
## Average runtime: ~

start_time = time.perf_counter()

with open(r"input.txt") as f:
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

manual = []

for line in lines:
  inp_diagram, inp_schematics, inp_joltage = line[0], line[1:-1], line[-1]
  temp_diagram = tuple(1 if x == "#" else 0 for x in inp_diagram[1:-1])
  temp_schematics = [tuple(map(int, x[1:-1].split(","))) for x in inp_schematics]
  temp_joltage = tuple(map(int, inp_joltage.split(",")[1:-1]))
  manual.append(Machine(temp_diagram, temp_schematics, temp_joltage))

machine_inputs = []

for machine in manual:
  for button_press_set in powerset(machine.schematics):
    machine_lights = [0]*len(machine.diagram)
    for button_presses in button_press_set: 
      for button_press in button_presses: machine_lights[button_press] = (machine_lights[button_press]+1)%2
    if tuple(machine_lights) == machine.diagram:
      machine_inputs.append(button_press_set)
      break

ans1 = sum(map(len, machine_inputs))

print(f"The least number of button presses is {ans1}.")

## Part 2
# Problem: 

# Solution: 


end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")