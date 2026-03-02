def fattoriale(number):
    if(number == 0 | number == 1):
        return 1
    else:
        for i in range(number-1, 0,-1):
            number *= i 
              
    return number

 
print(fattoriale(5))