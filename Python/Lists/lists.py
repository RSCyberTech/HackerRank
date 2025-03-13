if __name__ == "__main__":
    N = int(input())

out = []
for i in range(N):
    inp = input().split()
    if inp[0].lower() == "print":
        print(out)
    else:
        getattr(out, inp[0])(*[int(i) for i in inp[1:]])
