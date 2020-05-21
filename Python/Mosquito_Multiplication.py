def mosquito_multiplication(M, P, L, E, R, S, N):
    for i in range(N):
        dL = M * E
        dP = L // R
        dM = P // S

        L = dL
        P = dP
        M = dM

    print(M)

while True:
    try:
        inp = input().split()
        inp = [int(x) for x in inp]

        M = inp[0]
        P = inp[1]
        L = inp[2]
        E = inp[3]
        R = inp[4]
        S = inp[5]
        N = inp[6]

        mosquito_multiplication(M, P, L, E, R, S, N)
    except EOFError:
        break