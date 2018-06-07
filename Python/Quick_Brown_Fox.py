import string

for x in range(int(input())):
    alphabet = list(string.ascii_lowercase)

    phrase = list(input().lower())
    phraseAlpha = list(filter(lambda x: x in string.ascii_letters, phrase))
    for i in phraseAlpha:
        try:
            alphabet.remove(i)
        except ValueError:
            pass
            
    if len(alphabet) == 0:
        print("pangram")
    else:
        print("missing ", ''.join(alphabet))