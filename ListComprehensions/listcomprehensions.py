# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())
listoflists = [[p for p in range(0,x+1)], [q for q in range(0, y+1)], [r for r in range(0, z+1)]]
possibilities = list(itertools.product(*listoflists))
poss2 = [list(t) for t in possibilities]
final = [s for s in poss2 if sum(s)!= n]
print final