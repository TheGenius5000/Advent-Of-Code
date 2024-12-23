import time

## Day 23: LAN Party
## Difficulty: Medium
## Need-to-know skills: Greedy algorithms, Graph theory, Clique problem

## Problem: You're at a LAN party. You have a list of two-connected computers, and that connection is bidirectional.
##          Part 1: Find the number of 3-sized cliques in the connection graph that have a computer that starts with the letter 't'.
##          Part 2: Find the largest clique, and list the computers in it alphabetically.

## Solution: Part 1: Search through all computers and all of its connections' connections. For this bottom connection, see if it is 
##                   connected to the original computer. If it is, remember it. Then, count all the ones where any computer in this tuple of
##                   3-way connections starts with the letter 't'.
##           Part 2: This is the maximum clique problem, and its NP-hard. 
##                   For each computer, create its own list. Then for each computer, go through every other computer.
##                   If the computer is connected to every other computer in its designated list, then add it aswell.
##                   We now have a list of maximal cliques. Sort the biggest one alphabetically, and then output it.

## Average runtime: ~0.233 seconds

start_time = time.perf_counter()

with open("input.txt") as f:
  lines = f.read().splitlines()

connections = dict()

ans1 = 0

for line in lines:
  computer1, computer2 = line.split("-")
  if computer1 not in connections: connections[computer1] = set([computer2])
  else: connections[computer1].add(computer2)
  if computer2 not in connections: connections[computer2] = set([computer1])
  else: connections[computer2].add(computer1) 

three_connected_together = set()

for computer1 in connections:
  for computer2 in connections[computer1]:
    for computer3 in connections[computer2]:
      if computer3 in connections[computer1]: three_connected_together.add(tuple(sorted([computer1, computer2, computer3])))

maximal_computer_cliques = [[k] for k in connections]

for computer_clique in maximal_computer_cliques:
  for next_computer in connections:
    if all(next_computer in connections[clique_computer] for clique_computer in computer_clique): computer_clique.append(next_computer)

for computers in three_connected_together:
  if len(computers) == 3 and any(computer[0] == 't' for computer in computers): ans1 += 1

print(ans1)
print(','.join(sorted(max(maximal_computer_cliques, key=len))))

end_time = time.perf_counter()

print(f"{end_time-start_time} seconds")