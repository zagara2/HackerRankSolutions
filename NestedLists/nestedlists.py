# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
biglist = []
for x in range(N*2):
    biglist.append(raw_input())
namelist = [y for y in biglist if biglist.index(y) % 2 ==0]
gradelist = [z for z in biglist if biglist.index(z)%2 !=0]
numgradelist = [float(a) for a in gradelist]
#print namelist
#print numgradelist
bigbiglist = []
for b in range(N):
    bigbiglist.append([namelist[b], numgradelist[b]])
newlist = numgradelist[:]
newlist = set(newlist)
newlist = list(newlist)
newlist.sort()
secondlowest = newlist[1]
final = []
for item in bigbiglist:
    if item[1] == secondlowest:
        final.append(item[0])
final.sort()
for thing in final:
    print thing