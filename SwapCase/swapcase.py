# Enter your code here. Read input from STDIN. Print output to STDOUT
S = raw_input()
slist = list(S)
blist = []
for ch in slist:
    if ch.isupper():
        blist.append(ch.lower())
    elif ch.islower():
        blist.append(ch.upper())
    else:
        blist.append(ch)
final = "".join(blist)
print final