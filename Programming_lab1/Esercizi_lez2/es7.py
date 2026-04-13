def fat(number):
    fat = 1
    if number < 0:
        print("The factorial is not negative!")
    elif number == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, number + 1):
            fat  = fat * i 
        print(f"The factorial of {number} is {fat}!!!")

num = int(input("Enter a number: "))
fatt = fat(num)

