import re
import itertools
import math

#def permutate()

#lines = [x.strip().split() for x in open("D:/GitHub/Advent-Of-Code/2023/Day 12/test.txt")]
lines = [(list(filter(None, re.split('(\.)',''.join(re.sub('\.\.+', '.', x[0])).strip('.')))), [int(y) for y in x[1].split(",")]) for x in [x.strip().split() for x in open("D:/GitHub/Advent-Of-Code/2023/Day 12/test.txt")]]
#[print(f"{l}") for l in lines]
#print([[len(x) if ('#' in x or '?' in x) else 0 for x in str[0]] for str in lines])
arrangements = [1,4,1,1,4,10]
observed_arr = []
total = 0

for i, (conditions, groups) in enumerate(lines):
  total = 0
  minimum_str = ''.join(['#'*x+'.' for x in groups])[:-1]
  string = ''.join(conditions)
  diff = len(string)-len(minimum_str)
  nums = list(enumerate(groups.copy()))
  print(nums)
  if diff == 0:
    print("difference is zero. 1 possible combination. Moving along...")
    total = 1
  else:
    #bins = [[''.join(g) for k, g in itertools.groupby(x)] for x in conditions if '.' not in x]
    bins = [''.join(x) for x in conditions if '.' not in x]
    changes = [len(re.sub('\#\#+', '#', x)) for x in conditions if '.' not in x]
    sizes = [[(k, len(''.join(g))) for k, g in itertools.groupby(x)] for x in conditions if '.' not in x]
    #places = [[[n  for n in nums if (n >= len(str) and not nums.remove(n))] for str in bin if '#' in str] for i, bin in enumerate(bins)]
    #print(places)
    places = [(None, None) for b in bins]
    for i, bin in enumerate(bins):
      if '#' in bin:
        min = bin.count('#')
        for i, n in nums:
          if n <= len(bin) and n >= min:
            places[i] = (i,n)
            nums.remove((i,n))
            break
    # for i, bin in enumerate(sizes):
    #   length = len(bins[i])
    #   for n in nums:
    #     for j , (ch, amount) in enumerate(bin):
    #       if ch == '#' and n >= amount and n <= length:
    #         places.append((n,i,j))
    #         nums.remove(n)
    #         break
    print(places)
    """ print(bins)
    nums = groups.copy()
    for i, bin in enumerate(bins):
      for str in bin:
        if '#' in str:
          for j, n in enumerate(nums):
            if n >= len(str):
              places[i] = (nums[:j], (n,i))
              nums = nums[j+1:]
              break
    print(places)
    index = 0
    bins = [''.join(x) for x in bins]
    for prevs, (num, num_index) in places:
      if num:
        for bin in bins[index:num_index]:
          len_bin = len(bin)
          use_these = []
          for i, prev in enumerate(prevs):
            len_bin -= prev+1
            if len_bin > 1:
              use_these.append(i)
          possible = len(bin) + len(use_these) - sum(use_these)
          total += math.comb(possible, len(use_these))
      index = num_index    
    for n in nums:
      for bin in bins:
        if  """
    print(bins, sizes, changes)
    print(nums)
    print(f"{len(bins)} bins, {len(groups)} groups {'LOOK HERE!' if (len(bins) > len(groups)) else ''}")
    observed_arr.append(total)
      
print(observed_arr == arrangements)