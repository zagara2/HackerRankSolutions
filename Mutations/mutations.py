# Enter your code here. Read input from STDIN. Print output to STDOUT
mystring = raw_input()
info = raw_input()
info = info.split()
ind = int(info[0])
letter = info[1]
stlist = list(mystring)
stlist[ind] = letter
print "".join(stlist)