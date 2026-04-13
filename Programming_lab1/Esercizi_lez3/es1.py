#sum

def somma(lista):
    somma = 0 

    for i in lista:
        somma += i
    return somma

lista = [2, 3, 5, 9, 0]

print(somma(lista))
