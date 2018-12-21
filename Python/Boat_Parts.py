PN = list(map(int, input().split()))
days = 0
parts = set()
for i in range(PN[1]):

    if len(parts) != PN[0]:
        days += 1
    parts.add(input())


if len(parts) != PN[0]:
    print("paradox avoided")
else:
    print(days)