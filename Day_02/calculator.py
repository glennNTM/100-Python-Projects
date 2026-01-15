# User provides two numbers and selects an operation (addition, subtraction, multiplication, division)

def calculator():
    first_number = input("Enter the first number: ")

    operation = input("Enter operation (+, -, *, /): ")

    second_number = input("Enter the second number: ")

    if operation == "+":
        return int(first_number) + int(second_number)  
    elif operation == "-":
                return int(first_number) - int(second_number) 
    elif operation == "*":
                return int(first_number) * int(second_number)
    elif operation == "/":
                return int(first_number) / int(second_number)    


print(calculator())