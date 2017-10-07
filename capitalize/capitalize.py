# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
slist = list(s)
slist[0] = slist[0].upper()
for i in range(0, len(slist)):
    if slist[i-1]==" ":
        slist[i] = slist[i].upper()
print "".join(slist)