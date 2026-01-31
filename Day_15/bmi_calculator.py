def bmi_calculator(weight, height):
    w = float(input("Enter weight (in kilograms): "))
    h = float(input("Enter height (in meters): "))

    bmi = w / (h ** 2)
    if bmi < 18.5:
        print(f"BMI: {bmi}")
        print("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        print(f"BMI: {bmi}")
        print("Category: Normal Weight")    
    elif 25 <= bmi < 29.9:
        print(f"BMI: {bmi}")
        print("Category: Overweight")    
    else:
        print("Category: Obesity")

bmi_calculator(70, 1.75)