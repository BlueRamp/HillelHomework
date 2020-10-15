score = tuple(map(int, input("Input quantity of win, draw and lose numbers separated by backspace: ").split()))


def count_score(some_score: tuple):
    counted_score = some_score[0]*3, some_score[1]*1, some_score[2]*0
    return sum(counted_score)


print(count_score(score))
