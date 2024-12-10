import time

start_time = time.time()

lines = [list(map(int, x.split("x"))) for x in open("input.txt").read().splitlines()]

total = 0
bow_total = 0

for line in lines:
  l,w,h = line
  surface_area = min([(s1 := l*w),(s2 := l*h),(s3 := w*h)]) + 2*sum([s1,s2,s3])
  bow_length = l*w*h + min([2*x + 2*y for i, x in enumerate(line) for y in line[i+1:]])
  total += surface_area
  bow_total += bow_length

print(total)
print(bow_total)
end_time = time.time()

print(f"{end_time-start_time} seconds")