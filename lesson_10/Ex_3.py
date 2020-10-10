some_list = list(map(int, input("Input numbers separated by spaces ").split()))
shift = int(input("Input number of elements to shift: "))


def shift_list(shifted_list, func_shift):
    shifted_list = shifted_list[-func_shift:] + shifted_list[:-func_shift]
    return shifted_list


print(shift_list(some_list, shift))
