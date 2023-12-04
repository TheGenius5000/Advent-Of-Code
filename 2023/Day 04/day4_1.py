import time
start = time.perf_counter()
print(sum(list(map(lambda x: 0 if x < 1 else 2**(x-1), list(map(lambda x: (len([n0 for n0 in x[0] if n0 in x[1]])),list(map(lambda x: list(map(lambda y: y.split(), x)) ,list(map(lambda x: x.split(":")[1].split("|"), list(map(lambda x: x.strip("\n"), open("input.txt").readlines()))))))))))))
end = time.perf_counter()
print(end-start)