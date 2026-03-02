number = int(input("Give me a number: "))

def prime(number):
    for i in range (2, number):
        if(number % i == 0):
            print("The number is not prime!!")
            return
        print("The number is not prime!!")
            
prime(number)