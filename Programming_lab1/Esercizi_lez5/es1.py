
class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print(f"Ciao sono {self.ruolo},  {self.nome} {self.cognome}.")

class Studente(Persona):
    def __init__(self, nome, cognome):
        super().__init__("Studente UNITS", nome, cognome)
        self.corso = ["Analisi I", "Analisi II", "Calcolo delle probabilita", "Programmazione e laboratorio", "Algebra lineare", "Architettura e sistemi operativi"]

    def saluta(self):
        presentazione = Persona.saluta(self)
        print(f"{presentazione}\n Corsi frequentati: {self.corso}")


class Docente(Persona):
    def __init__(self, nome, cognome):
        super().__init__("Docente UNITS", nome, cognome)
        self.corso = ["Analisi I", "Analisi II"]

    def saluta(self):
        presentazione = Persona.saluta(self)
        print(f"{presentazione}\n Corsi insegnati: {self.corso}")

obj_Irene = Studente("Irene", "Rossi")
obj_Irene.saluta()