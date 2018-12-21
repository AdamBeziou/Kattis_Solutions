import math

num = ""
while True:
    try:
        num = int(input())
    except EOFError:
        break

    divisors = 1
    div1 = 2
    while div1 < num**(1/2):
        if num % div1 == 0:
            div2 = num / div1
            divisors += div1
            divisors += div2
        div1 += 1
    if num**(1/2) % 1 == 0:
        divisors += num**(1/2)
    
    r = math.fabs(num - divisors)
    if r == 0:
        print(f"{num} perfect")
    elif r <= 2:
        print(f"{num} almost perfect")
    else:
        print(f"{num} not perfect")

    
            