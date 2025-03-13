# Enter your code here. Read input from STDIN. Print output to STDOUT

x, y = [int(z) for z in input().split()]

A = {}
for a in range(x):
    inp = input()
    if inp not in A.keys():
        A[inp] = ""
    A[inp] = str(A[inp] + " " + str(a + 1)).strip()

for b in range(y):
    inp = input()
    if inp in A.keys():
        print(A[inp])
    else:
        print(-1)
