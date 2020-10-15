original_string = input("Input original string: ").split()
word_to_change = input("Input word to change: ")
new_word = input("Input new word: ")
number_of_changes = int(input("Number of changes: "))


def fake_string(string, word, word_new, number):
    while number != 0:
        if word in string:
            string.insert(string.index(word), word_new)
            string.remove(word)
            number -= 1
    return " ".join(string)


print(fake_string(original_string, word_to_change, new_word, number_of_changes))
