if __name__ == '__main__':
    students={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in students.keys():
            students[score]=[]
        students[score].append(name)
    secondLast=sorted(students.keys())[1]
    for s in sorted(students[secondLast]):
        print(s)
