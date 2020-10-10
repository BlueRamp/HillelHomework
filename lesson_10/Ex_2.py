palindrome = input("Input palindrome: ")


def palindrome_check(some_string):
    stop = int(len(some_string)/2)
    if some_string[0:stop:1] == some_string[len(some_string):stop:-1]:
        return "Is palindrome"
    else:
        return "Not palindrome"


print(palindrome_check(palindrome))
