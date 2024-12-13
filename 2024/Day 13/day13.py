import time
import numpy as np

start_time = time.time()

lines = [x.strip("\n").split("\n") for x in open("input.txt").read().split("\n\n")]
total = 0
total2 = 0

def interpret(config):
  parsed_nums = []
  for line in config[:2]:
    parsed_nums.append((keep_nums := lambda line: [int(''.join([ch for ch in seg if ch.isdigit()])) for seg in line.split(",")])(line))
  targets = keep_nums(config[2])
  return (parsed_nums, targets)

for config in lines:
  print(config)
  delta_buttons, targets = interpret(config)
  delta_buttons = np.array(delta_buttons).T.astype(np.float64)
  targets = np.array(targets).astype(np.float64)
  presses = np.linalg.solve(delta_buttons, targets)
  tokens = np.sum(presses*np.array([3,1]))
  #For unstable maths
  if any([x < 0 for x in presses]): continue
  if np.isclose(tokens, int(tokens)): 
    total += tokens

for config in lines:
  delta_buttons, targets = interpret(config)
  delta_buttons = np.array(delta_buttons).T.tolist()
  targets = [x+10**13 for x in targets]
  A = (targets[1]*delta_buttons[0][1] - delta_buttons[1][1]*targets[0])/(delta_buttons[1][0]*delta_buttons[0][1]-delta_buttons[1][1]*delta_buttons[0][0])
  B = (targets[0]-delta_buttons[0][0]*A)/delta_buttons[0][1]
  if int(A) == A and B == int(B):
    total2 += 3*A+B


print(int(total))
print(int(total2))

end_time = time.time()

print(f"{end_time-start_time} seconds")