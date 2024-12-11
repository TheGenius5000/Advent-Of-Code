import time
import functools

start_time = time.time()

lines = list(map(int,"125 17".split(" ")))
lines = list(map(int,open("D:\\GitHub\\Advent-Of-Code\\2024\\Day 11\\input.txt").read().strip("\n").split(" ")))
blinks = 25

@functools.cache
def stoneBlink(stone_num, blink, num_of_blinks):
  if blink == num_of_blinks: return 1
  if stone_num == 0: return stoneBlink(1, blink+1, num_of_blinks)
  stone_num_str = str(stone_num)
  if len(stone_num_str) % 2 == 0:
   return stoneBlink(int(stone_num_str[:(half := len(stone_num_str)//2)]), blink+1, num_of_blinks) + stoneBlink(int(stone_num_str[half:]), blink+1, num_of_blinks)
  return stoneBlink(stone_num*2024, blink+1, num_of_blinks)

total1 = sum([stoneBlink(x,0,25) for x in lines])
total2 = sum([stoneBlink(x,0,75) for x in lines])

print(total1)
print(total2)

end_time = time.time()

print(f"{end_time-start_time} seconds")