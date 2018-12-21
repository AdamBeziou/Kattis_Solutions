newBit = []

NAB = input().split()
N = int(NAB[0])
A = NAB[1]
B = NAB[2]
newA = []
newB = []

startInt =  0
if int(A[0]):
    startInt += 2**(N - 1)
newA.append(A[0])
for i in range(1, N):
    if (A[i] != newA[i - 1]):
        startInt += 2**(N - i - 1)
        newA.append('1')
    else:
        newA.append('0')

endInt = 0
if int(B[0]):
    endInt += 2**(N - 1)
newB.append(B[0])

for i in range(1, N):
    if (B[i] != newB[i - 1]):
        endInt += 2**(N - i - 1)
        newB.append('1')
    else:
        newB.append('0')

print(endInt - startInt - 1)