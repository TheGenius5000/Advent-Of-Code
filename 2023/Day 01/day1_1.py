import re
import numpy as np
long_num_strings = []
nums = []
with open("input.txt", "r") as f:
    for line in f:
        long_num = ''.join(re.findall("\d+", line))
        long_num_strings.append(long_num)
        #print(long_num)

for n in long_num_strings:
    num = ''.join([n[0], n[-1]])
    print(num)
    nums.append(int(num))

print(np.sum(nums))