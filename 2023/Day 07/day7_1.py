import numpy as np
from functools import reduce
import time

#Procedure to add hands given a hand and a bid
#index means the type that the card has
def add_to_hands(hand, bid, index):
  global hands
  for i, tup in enumerate(hands[index]):
    old_hand, _ = tup
    for j, ch in enumerate(old_hand):
      label_rank = labels.index(hand[j])
      label_rank_old = labels.index(old_hand[j])
      if label_rank > label_rank_old:
        hands[index].insert(i, (hand, bid))
        return
      elif label_rank < label_rank_old:
        break
  hands[index].append((hand, bid))

start = time.perf_counter()

hands = [[], [], [], [], [], [], []]
length = 0
labels = "23456789TJQKA"

with open("input.txt") as f:
  for line in f:
    [hand, bid] = line.split()
    kinds = [hand.count(x) for x in set(hand)]
    if 5 in kinds:
      add_to_hands(hand, bid, 0)
    elif 4 in kinds:
      add_to_hands(hand, bid, 1)
    elif 3 in kinds:
      if 2 in kinds:
        add_to_hands(hand, bid, 2)
      else:
        add_to_hands(hand, bid, 3)
    elif kinds.count(2) >= 2:
      add_to_hands(hand, bid, 4)
    elif kinds.count(2) == 1:
      add_to_hands(hand, bid, 5)
    else:
      add_to_hands(hand, bid, 6)
  length += 1

#unpack the tuple for the bids and flatten
bids = np.array(reduce(lambda x, y: x+y, [[x[1] for x in xs] for xs in hands]), dtype=int)
ranks = np.arange(len(bids), 0, -1)

print(np.sum(np.multiply(ranks, bids)))

end = time.perf_counter()
print(end-start)