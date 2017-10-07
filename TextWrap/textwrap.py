# Enter your code here. Read input from STDIN. Print output to STDOUT
import textwrap
S = raw_input()
w = int(raw_input())
print textwrap.fill(S, w)