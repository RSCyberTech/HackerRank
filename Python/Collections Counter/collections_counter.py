# Enter your code here. Read input from STDIN. Print output to STDOUT

_ = input()
sizesAvailable = input().split()
numberCustomers = input()
x = []
for _ in range(int(numberCustomers)):
    x.append(input().split())

money = 0
while x:
    toWork = x.pop(0)
    if toWork[0] in sizesAvailable:
        money += int(toWork[1])
        sizesAvailable.remove(toWork[0])

print(money)
