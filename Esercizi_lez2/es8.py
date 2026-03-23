def is_triangle(number1, number2, number3):
    if number1 > 0 and number2 > 0 and number3 > 0:
        print("It's possible doing triangle with this numbers")
        if number1 == number2 == number3:
            print("This triangle is equilateral")
        elif number1 == number2 or number2 == number3 or number1 == number3:
            print("This triangle is isocele")
        else:
            print("This triangle have different measures")
    else:
        print("It's not possible doing a triangle!!!")

# num1 = int(input("Enter the 1st number: "))
# num2 = int(input("Enter the 2nd number: "))
# num3 = int(input("Enter the 3rd number: "))

# result = is_triangle(num1, num2, num3)