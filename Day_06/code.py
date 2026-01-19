# A program that converts temperatures between Fahrenheit and Celsius.

def temp_converter():
    temp = float(input("Enter temperature: "))
    type = int(input("Select a conversion type (1 for Fahrenheit t Celsius, 2 for Celsius to Fahrenheit): "))

    if type == 1:
        result = (temp - 32) * 5/9
        print(f"Converted temperature: {result} °C")
    elif type == 2:
        result = (temp * 9/5) + 32
        print(f"Converted temperature: {result} °F")

    else:
        print("Coversion impossible")
        

temp_converter()
