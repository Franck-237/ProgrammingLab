somma = 0

while True:
    numero = int(input("Inserire un numero (Scrive 0 per fermarsi.): "))
    if numero == 0:
        break
    else:
        somma += numero

print(somma)
