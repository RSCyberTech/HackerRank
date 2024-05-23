# Enter your code here. Read input from STDIN. Print output to STDOUT

inp = input().split()
array = input().split()
set1 = set(input().split())
set2 = set(input().split())

happy = 0
for a in array:
    if a in set1:
        happy += 1
    elif a in set2:
        happy -= 1

print(happy)
