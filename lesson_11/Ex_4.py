original_string = input("Input original string: ")
word_to_change = input("Input word to change: ")
new_word = input("Input new word: ")
number_of_changes = int(input("Number of changes: "))


def fake_string(string, word, word_new, number):
    return string.replace(word, word_new, number)


print(fake_string(original_string, word_to_change, new_word, number_of_changes))
