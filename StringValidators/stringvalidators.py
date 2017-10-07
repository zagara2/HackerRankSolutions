# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
first = False
sec = False
third = False
fourth = False
fifth = False
for ch in s:
    if ch.isalnum():
        first = True
    if ch.isalpha():
        sec = True
    if ch.isdigit():
        third = True
    if ch.islower():
        fourth = True
    if ch.isupper():
        fifth = True
print first
print sec
print third
print fourth
print fifth