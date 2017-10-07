# Enter your code here. Read input from STDIN. Print output to STDOUT
A = int(raw_input())
B = raw_input()
mylist = []

for x in B.split():
    mylist.append(int(x))

t = tuple(mylist)
print hash(t)