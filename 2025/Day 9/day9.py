import time
import itertools

## Day 9 - Movie Theater
## Average runtime: ~

start_time = time.perf_counter()

with open(r"D:\GitHub\Advent-Of-Code\2025\Day 9\input_test.txt") as f:
  coords = {tuple(map(int, x.split(","))) for x in f.read().splitlines()}

## Part 1
# Problem: Out of the 2d co-ordinates given that indicate red squares, which two together give the largest area?

# Solution: Permeate all the co-ordinates and keep track of the one with the largest area.

max_area = 0

for (x0, y0), (x1, y1) in itertools.combinations(coords, 2):
    if (current_area := (abs(x0-x1)+1)*(abs(y0-y1)+1)) > max_area:
      max_area = current_area

[print(''.join('#' if (x,y) in coords else '.' for x in range(15))) for y in range(10)]

print(f"The max square that can be made out of the red tiles is {max_area}.")

## Part 2
# Problem: Find the area of the largest rectangle you can make but with the extra restriction of it being within the bounding polygon of red tiles.

# Solution: A similar solution to above, but also with the restriction of all the corners of the rectangle existing within said polygon.

# for x in range(100000):
#   for y in range(100000):
#      if (x,y) in coords:
#         start = (x,y)
#         break

# print(start)

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")