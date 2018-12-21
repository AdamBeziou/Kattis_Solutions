import math

case = 0
while True:
    case += 1
    try:
        n = int(input())
    except EOFError:
        break
    nums = []

    for i in range(n):
        nums.append(int(input()))

    m = int(input())

    nums.sort()
    print(f"Case {case}:")
    if n == 1:
        for i in range(m):
            sum = int(input())
            print(f"Closest sum to {sum} is {nums[0]}.")
    else:
        for i in range(m):
            sum = int(input())
            dif = 20**7
            sl = 0
            sr = len(nums) - 1
            l = 0
            r = len(nums) - 1
            while(r > l):
                if math.fabs(nums[l] + nums[r] - sum) < dif:
                    dif = math.fabs(nums[l] + nums[r] - sum)
                    sl = l
                    sr = r

                if nums[l] + nums[r] < sum:
                    l += 1
                else:
                    r -= 1

            print(f"Closest sum to {sum} is {nums[sl] + nums[sr]}.")



            
                



            