while True:
    try:
        n = int(input("Input natural number:"))
    except ValueError as error:
        print(error)
    if n >= 0:
        i = 1
        some_string = ""
        while i <= n:
            some_string = some_string + str(i)
            i += 1
            print(some_string)
        break
    else:
        print("Not natural")
        continue