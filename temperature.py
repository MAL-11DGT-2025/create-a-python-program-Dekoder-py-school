def convert(number, conversion):
    if conversion == "f":
        result = number - 32 * (5 / 9)
        return result
    elif conversion == "c":
        result = number * (9 / 5) + 32
        return result


f_to_c_options = ["a", "a)", "a) fahrenheit to celcius", "fahrenheit to celcius"]
c_to_f_options = ["b", "b)", "b) celcius to fahrenheit", "celcius to fahrenheit"]

original_temp = float(input("What is the temperature you'd like to convert?\n>>"))
conversion = input(
    "Do you want to convert:\na) Fahrenheit to Celcius\nb) Celcius to Fahrenheit\n>> "
)

if conversion in f_to_c_options:
    print(convert(original_temp, "f"))
elif conversion in c_to_f_options:
    print(convert(original_temp, "c"))
else:
    print("Invalid conversion was chosen.")
