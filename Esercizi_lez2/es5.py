number = int(input("Enter a number: "))

for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        print(f"{number} it's not a prime number!")
        break
    else:
        print(f"{number} it's a prime number")
