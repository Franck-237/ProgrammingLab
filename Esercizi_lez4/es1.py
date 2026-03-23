
class Veicolo:
    
    def __init__(self, anno, modello, marca):
        self.anno = anno
        self.modello = modello
        self.marca = marca
        self.speed = 0

    def __str__(self):
        return f"Il veicolo {self.marca} del modello {self.modello} dell'anno {self.anno} a una velocita' {self.speed} km/h"
    

    def accellerare(self):
        self.speed += 5
        return self.speed

    def frenare(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0
        return self.speed

    def get_speed(self):
        return self.speed

    
veicolo1 = Veicolo(2026, "Sport", "Mustang")

veicolo1.accellerare()
veicolo1.accellerare()
print(f"Velocità dopo 2 accelerate: {veicolo1.get_speed()}")

veicolo1.frenare()
print(veicolo1)