letter = "a"
frase = input("Give me a frase: ")
 
def contalettere(letter,frase):
 
    l = len(frase)
    k = 0
 
    for item in frase:
        if(item == letter):
            k += 1
 
    return k
 
number = contalettere(letter,frase)
print(number)