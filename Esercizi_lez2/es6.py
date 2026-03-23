sum = 0
number = int(input("Enter a number: "))

while number != 0:
    sum += number
    number = int(input("Enter a number: "))

print(f"The total of all the numbers is: {sum}")