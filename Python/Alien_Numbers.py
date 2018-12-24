cases = int(input())

for i in range(cases):
    NSA = input().split()
    num = list(NSA[0])
    sourceLanguage = list(NSA[1])
    alienLanguage = list(NSA[2])
    conv = []
    sourceBase = len(sourceLanguage)
    tBase = len(alienLanguage)

    sConv = 0
    for j, n in enumerate(num[::-1]):
        sConv += sourceLanguage.index(n) * sourceBase**j
    
    while sConv > 0:
        conv.append(alienLanguage[sConv % tBase])
        sConv = sConv // tBase

    print(f"Case #{i + 1}: " + ''.join(conv[::-1]))
