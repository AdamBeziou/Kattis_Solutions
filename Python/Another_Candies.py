cases = int(input())

for i in range(cases):
    blank = input()
    candies = 0
    num = int(input())
    for j in range(num):
        candies += int(input())

    if candies % num == 0:
        print("YES")
    else:
        print("NO")