some_dict = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
new_dict = {}


def remove_none_item(dictionary):
    for key, value in some_dict.items():
        if value is not None:
            new_dict[key] = value
    return new_dict


print(remove_none_item(some_dict))
