import numpy as np
import time

calibration_vals = []
numbers = {
    'one': '1',
    'two': '2', 
    'three': '3', 
    'four': '4',
    'five': '5', 
    'six': '6', 
    'seven': '7', 
    'eight': '8', 
    'nine': '9'
}

def wordnumFrom(x, from_beginning=True):
    max = len(x)
    size = 1
    while(size <= max):
        string = x[:size] if from_beginning else x[-size:]
        for k, v in numbers.items():
            if k in string or v in string:
                return v  
        size += 1

start = time.perf_counter()
with open("input.txt", "r") as f:
    for line in f:
        first = wordnumFrom(line)
        last = wordnumFrom(line, False)
        calibrated_num = first+last
        calibration_vals.append(int(calibrated_num))
        #print(first, last)

total = np.sum(calibration_vals)
end = time.perf_counter()
print(total)
print(end-start)