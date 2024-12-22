import time

## Day 22: Monkey Market
## Difficulty: Medium
## Need-to-know skills: Binary operations, Hashmaps

## Problem: You want to buy bananas. You are selling hiding spots for bananas.
##          The asking price is computed in a pseudo-random way for each iteration. 
##          Part 1: Find this pseudo-random number after 2000 iterations. Work out the sum of all the pseudo-random number for each
##                  line of your input.
##          Part 2: The actual asking price is the last digit in the pseudo-random number.
##                  There is a certain sequence of 4 numbers that, together, can result in the highest
##                  asking price overall for you. You need to find the sequence and the corresponding
##                  number attached to it.

## Solution: Part 1: Just go through 2000 iterations and work out the pseudo-random number for each of the
##                   starting numbers, and add them together.
##           Part 2: During the iterations, remember the last 4 changes in price. You can create a tuple out of them and store a dictionary
##                   of it with the known prices in a lookup table. Add to it the prices you see (or assign if it's the first time seeing the sequence)
##                   Finally, output the highest numbers of any of these sequences, which yields the most bananas.

## Average runtime: ~ 3.35 seconds

start_time = time.perf_counter()

with open("input.txt") as f: 
  lines = list(map(int, f.read().splitlines()))

price_change_sequences = dict()

def secret_number(secret_num, number_iteration):
  new_secret_num = secret_num
  price_sequence = []
  change_sequences_seen = set()
  for _ in range(number_iteration):
    prev_secret_num = new_secret_num
    new_secret_num = (new_secret_num ^ new_secret_num*64) % 16777216
    new_secret_num = (new_secret_num//32 ^ new_secret_num) % 16777216
    new_secret_num = (new_secret_num*2048 ^ new_secret_num) % 16777216
    prev_actual_price = (prev_secret_num % 10)
    current_actual_price = (new_secret_num % 10)
    price_change = current_actual_price - prev_actual_price
    price_sequence.append(price_change)
    if len(price_sequence) > 4: price_sequence.pop(0)
    if len(price_sequence) < 4: continue
    seq = tuple(price_sequence)
    if seq in change_sequences_seen: continue
    if seq not in price_change_sequences:
      price_change_sequences[seq] = current_actual_price
    else:
      price_change_sequences[seq] += current_actual_price
    change_sequences_seen.add(seq)
  return new_secret_num

ans1 = 0
ans2 = 0

for start_num in lines:
  secret_num = secret_number(start_num, 2000)
  ans1 += secret_num
  
print(ans1)
print(max(price_change_sequences.values()))

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")