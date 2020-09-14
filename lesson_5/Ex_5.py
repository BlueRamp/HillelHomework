import math
square_side = int(input("Input square side:"))
def find_values(square_side):
    square_perimeter = square_side * 4
    square_area = square_side ** 2
    square_diagonal = math.sqrt(2*square_area)
    return (square_perimeter, square_area, square_diagonal)
print(find_values(square_side))