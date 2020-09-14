side_length = float(input("Input side of your figure:"))
height = float(input("Input height of your figure:"))
option = input("Do you want to find square area too?").upper()
def find_area(side_length, height, option):
    triangle_area = 0.5 * side_length * height
    square_area = side_length ** 2
    if option == "YES":
        return triangle_area, square_area
    else:
        return triangle_area
print(find_area(side_length, height, option))