a = (int(input ()))
b = (int(input ()))
c = (int(input ()))
 
def controllo_somma (a,b,c):
    errore=0
    if a>b+c:
        errore=errore+1
    if b>a+c:
        errore=errore+1
    if c>b+a:
        errore=errore+1
    return errore
 
 
def controllo_differenza (a,b,c):
    errore=0
    if a<b-c:
        errore=errore+1
    if b<a-c:
        errore=errore+1
    if c<b-a:
        errore=errore+1
    return errore
 
def tipo_triangolo (a,b,c):
   
    if (a==b or b==c or c==a):
        if (a==b==c):
            print ("è un triangolo equilatero")
        else:
            print ("è un triangolo isoscele")
    if ((a^2 + b^2 == c^2) or (c^2 + b^2 == a^2) or (a^2 + c^2 == b^2)):
        print ("è un triangolo rettangolo")
    else:
        print ("è un triangolo scaleno")
 
if (controllo_somma (a,b,c) +controllo_differenza (a,b,c) ==0):
    print ("questo puo essere un triangolo")
    tipo_triangolo (a,b,c)
else:
    print ("questo NON puo essere un triangolo")