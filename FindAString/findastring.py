st = raw_input()
subst = raw_input()
lenSS = len(subst)
count = 0 
for i in range(0, len(st)):
    if st[i:i+lenSS] == subst:
        count += 1
        
print count