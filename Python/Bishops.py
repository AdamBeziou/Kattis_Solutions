while True:
    try:
        entry = int(input())
    except EOFError:
        break

    if entry == 1:
        print(1)
    else:
        print(entry + entry - 2)