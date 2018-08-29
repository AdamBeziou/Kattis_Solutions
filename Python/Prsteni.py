import fractions

num = int(input())
rings = input().split()
rings = [int(x) for x in rings]
firstRing = rings.pop(0)
for i in rings:
    if '/' not in str(fractions.Fraction(firstRing / i).limit_denominator()):
        print(str(fractions.Fraction(firstRing / i).limit_denominator()) + "/1")
    else:
        print(fractions.Fraction(firstRing / i).limit_denominator())