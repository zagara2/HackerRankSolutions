# Enter your code here. Read input from STDIN. Print output to STDOUT
#just realized the instructions said a dictionary was required so here ya go!
n = int(raw_input())
studentlist = []
mydict = {}
for x in range(n):
    studentlist.append(raw_input())
target = raw_input()
for item in studentlist:
    isplit = item.split()
    student = isplit[0]
    mydict[student] = [float(isplit[1]), float(isplit[2]), float(isplit[3])]

for (k, v) in mydict.items():
    if k == target:
        av = sum(v)/3.0
        print format(av, ".2f")