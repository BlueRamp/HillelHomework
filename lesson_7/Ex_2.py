def input_data():
    try:
        temperature = float(input("Input temperature: "))
    except ValueError as error:
        print("Please input numbers.")
    unit = input("Input unit(as K,C,F): ")
    if unit not in ("K", "C", "F"):
        print("Please input K,C or F")
    return calculations(temperature, unit.upper())


def kelvin(temperature):
    kelvin_t = (temperature, "K")
    celsius_t = (temperature - 273.15, "C")
    fahrenheit_t = (temperature * 1.8, "F")
    return kelvin_t, celsius_t, fahrenheit_t


def celsius(temperature):
    kelvin_t = (temperature + 273.15, "K")
    celsius_t = (temperature, "C")
    fahrenheit_t = (temperature * 1.8 + 32, "F")
    return kelvin_t, celsius_t, fahrenheit_t


def fahrenheit(temperature):
    kelvin_t = ((temperature + 459.67) / 1.8, "K")
    celsius_t = ((temperature - 32) / 1.8, "C")
    fahrenheit_t = (temperature, "F")
    return kelvin_t, celsius_t, fahrenheit_t


def calculations(temperature, unit):
    if unit == "K":
        kelvin_t, celsius_t, fahrenheit_t = kelvin(temperature)
    if unit == "C":
        kelvin_t, celsius_t, fahrenheit_t = celsius(temperature)
    if unit == "F":
        kelvin_t, celsius_t, fahrenheit_t = fahrenheit(temperature)
    print(f"In kelvin {kelvin_t}, in celsius {celsius_t}, in fahrenheit {fahrenheit_t}")


some_input = ""
while some_input == "":
    input_data()
    some_input=(input("To continue press Enter, to stop - input any symbol."))