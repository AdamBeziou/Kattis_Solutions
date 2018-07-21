import math

binToOct = {"000" : "0",
            "001" : "1",
            "010" : "2",
            "011" : "3",
            "100" : "4",
            "101" : "5",
            "110" : "6",
            "111" : "7"}

octSequence = ""
binarySequence = input()
divSequence = "0" * round(3 * (math.ceil(len(binarySequence) / 3) - len(binarySequence) / 3)) + binarySequence

for i in range(0, len(divSequence) // 3):
    octSequence = octSequence + binToOct[divSequence[3 * i:3 * i + 3]]

print(octSequence)