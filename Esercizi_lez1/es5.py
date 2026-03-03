numero = int(input("Enter a number: "))

def primo(n):
    
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

risultato = primo(numero)

if risultato:
    print(f"{numero} e un numero primo")
else:
    print(f"{numero} non e un numero primo")