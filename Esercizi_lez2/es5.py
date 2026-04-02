numero = int(input("Scrivere un numero: "))

for i in range(2, numero+1):
    if numero % i == 0 and numero % numero == 0:
        print(f"{numero} non  e primo")
    else:
        print(f"{numero} e primo")
        break
