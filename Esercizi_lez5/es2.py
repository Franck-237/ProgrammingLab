
class Veicolo:

    def __init__(self, modello, anno, marca):
        self.modello = modello
        self.anno = anno
        self.marca = marca

    def __str__(self):
        return f"Il veicolo {self.marca} dell'anno {self.anno} e del modello {self.modello}"
    

class Auto(Veicolo):

    def __init__(self, modello, anno, marca, numero_porte):
        super().__init__(modello, anno, marca)
        self.numero_porte = numero_porte

    def __str__(self):
        return f"Il veicolo {self.marca} dell'anno {self.anno} e del modello {self.modello} ha {self.numero_porte} porte(s)"
    
class Moto(Veicolo):

    def __init__(self, modello, anno, marca, tipo):
        super().__init__(modello, anno, marca)
        self.tipo = tipo

    def __str__(self):
        return f"Il veicolo {self.marca} dell'anno {self.anno} , del modello {self.modello} e del tipo {self.tipo}"
    
auto1 = Auto("Ghost", 2026, "Mustang", 4)
moto1 = Moto("Fire", 1998, "Kawasaki", "Sportiva")

print(auto1.__str__())
print(moto1.__str__())