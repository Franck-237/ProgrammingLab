
class Poligono:

    def __init__(self, numero_lati):
        self.numero_lati = numero_lati

    def __str__(self):
        return f"Sono un poligono con {self.numero_lati} lati"
    
class Quadrilatero(Poligono):

    def __init__(self, numero_lati):
        super().__init__(numero_lati)

    def __str__(self):
        return f"Sono un quadrilatero"
    
class Rettangolo(Quadrilatero):

    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def __str__(self):
        return f"Sono un quadrilatero piu precisamente un rettangolo di base {self.base} e di altezza {self.altezza}"
    
    def perimetro(self):
        return {self.base} + {self.altezza} * 2
    
    def area(self):
        return {self.base} * {self.altezza}
    
class Triangolo(Poligono):

    def __init__(self):
        self.lunghezza = []
        self.lati = 1

    def __str__(self):

        while self.lati <= 3:

            lunghezza = float(input("Enter la lunghezza: "))
            self.lunghezza.append(lunghezza)

            if len(self.lunghezza <= 3):
                break

            self.lati += 1
    
        for i in self.lunghezza:
            print(f"La lunghezza e {i}")
   
    
    def perimetro(self):
        sum = 0
        for i in self.lunghezza:
            sum += i
        return sum

    def is_equilatero(self):

        n = len(self.lunghezza)
        for i in self.lunghezza:
            for n - 1- i in self.lunghezza:
                if i == n -1 -i:
                    return True
                else:
                    return False

