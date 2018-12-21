PT = list(map(int, input().split()))
passed = 0
for i in range(PT[0]):
    point = True
    for i in range(PT[1]):
        case = input()
        for i in case[1:]:
            if ord(i) > 122 or ord(i) < 97:
                point = False
                break
    if point:
        passed += 1
print(passed)