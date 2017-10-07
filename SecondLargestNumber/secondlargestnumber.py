# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
myarr = raw_input()
numlist = [int(x) for x in myarr.split()]
numlist = set(numlist)
numlist = list(numlist)
numlist.sort()
print numlist[-2]