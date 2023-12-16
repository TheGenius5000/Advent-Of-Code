import time

start = time.perf_counter()
def light_beam_travel(start, direction, threshold):
  global lines
  global energised
  global max_allowed
  x, y = start
  while True:
    match direction:
      case 270:
        x -= 1
      case 90:
        x += 1
      case 180:
        y += 1
      case 0:
        y -= 1
    if any([x < 0, y < 0, y >= len(lines), x >= len(lines[0]), threshold > max_allowed]): 
      return
    try:
      if energised[y][x] == '#':
        threshold += 1
      else:
        energised[y][x] = '#'
      this_char = lines[y][x]
      if this_char == '|' and direction in [270, 90]:
        light_beam_travel((x, y), 180, threshold)
        light_beam_travel((x, y), 0, threshold)
        return
      elif this_char == '-' and direction in [0, 180]:
        light_beam_travel((x, y), 270, threshold)
        light_beam_travel((x, y), 90, threshold)
        return
      elif this_char == '/':
        match direction:
          case 0:
            direction = 90
          case 90:
            direction = 0
          case 180:
            direction = 270
          case 270:
            direction = 180
      elif this_char == chr(92):
        match direction:
          case 0:
            direction = 270
          case 90:
            direction = 180
          case 180:
            direction = 90
          case 270:
            direction = 0
    except:
      return

lines = list(map(list, open("input.txt").read().splitlines()))
largest = 0
possible = []
max_allowed = 500

for x, dir in [(-1, 90), (111, 270)]:
  for y in range(110):
    energised = [list('.'*len(x)) for x in lines]
    light_beam_travel((x, y), dir, 0)
    total = sum([x.count('#') for x in energised])
    possible.append((x, y, total, dir))

for y, dir in [(-1, 180), (111, 0)]:
  for x in range(110):
    energised = [list('.'*len(x)) for x in lines]
    light_beam_travel((x, y), dir, 0)
    total = sum([x.count('#') for x in energised])
    possible.append((x, y, total, dir))

probably_max = sorted(possible, key=lambda tup: tup[2])
print(probably_max[-1])
end = time.perf_counter()
print(end-start)