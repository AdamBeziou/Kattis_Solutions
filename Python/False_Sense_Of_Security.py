import sys

morseConversion = {"A":
                ".-",
                "H":
                "....",
                "O":
                "---",
                "V":
                "...-",
                "B":
                "-...",
                "I":
                "..",
                "P":
                ".--.",
                "W":
                ".--",
                "C":
                "-.-.",
                "J":
                ".---",
                "Q":
                "--.-",
                "X":
                "-..-",
                "D":
                "-..",
                "K":
                "-.-",
                "R":
                ".-.",
                "Y":
                "-.--",
                "E":
                ".",
                "L":
                ".-..",
                "S":
                "...",
                "Z":
                "--..",
                "F":
                "..-.",
                "M":
                "--",
                "T":
                "-",  
                "G":
                "--.",
                "N":
                "-.",
                "U":
                "..-",
                "_":
                "..--",
                ".":
                "---.",
                ",":
                ".-.-",
                "?":
                "----"}

for line in sys.stdin:
    translation = ""
    morse = ""
    nums = []
    counter = 0

    for i in line:
        if i != "\n":
            morse = morse + morseConversion[i]
            nums.append(len(morseConversion[i]))

    nums.reverse()

    for number in nums:
        for letter, morseTerm in morseConversion.items():
            if morseTerm == morse[counter:counter + number]:
                translation = translation + letter
        
        counter += number
    
    print(translation)

    

    

     