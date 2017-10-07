# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
commands = []
mylist = []
for i in range(N):
    commands.append(raw_input())
for command in commands:
    f = command.split()
    if f[0] == "insert":
        mylist.insert(int(f[1]), int(f[2]) )
    if f[0] == "print":
        print mylist
    if f[0] == "remove":
        mylist.remove(int(f[1]))
    if f[0] == "append":
        mylist.append(int(f[1]))
    if f[0] == "sort":
        mylist.sort()
    if f[0] == "pop":
        mylist.pop()
    if f[0] == "reverse":
        mylist.reverse()