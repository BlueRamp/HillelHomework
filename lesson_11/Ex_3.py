string = (input("Input your string: ")).split()


def longest_word(some_string):
    return max(some_string, key=len)


print(longest_word(string))
