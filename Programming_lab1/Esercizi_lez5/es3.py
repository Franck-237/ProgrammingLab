

class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print(f"Ciao sono {self.ruolo},  {self.nome} {self.cognome}.\n")

class Studente(Persona):
    def __init__(self, nome, cognome):
        super().__init__("Studente UNITS", nome, cognome)
        self.corso = ["Analisi I", "Analisi II", "Calcolo delle probabilita", "Programmazione e laboratorio", "Algebra lineare", "Architettura e sistemi operativi"]

    def saluta(self):
        Persona.saluta(self)
        print(f"Corsi frequentati: {self.corso}")

    def calcolo(self, docente):
        set_studente = set(self.corso)
        set_docente = set(docente.corso)

        if set_docente == set_studente:
            print(f"{docente.nome} insegna tutti i corsi dello studente {self.cognome}")
        else:
            print(f"{docente.cognome} non insegna tutti i corsi dello studente {self.cognome}")



class Docente(Persona):
    def __init__(self, nome, cognome):
        super().__init__("Docente UNITS", nome, cognome)
        self.corso = []

    def aggiungi_corso(self):
        
        while True:
            scelta = input("inserisci il nome del corso (o digita 'q' per uscire): ")

            if scelta.lower() == "q":
                break

            if not scelta:
                print("Errore: il nome del corso non puo essere vuoto.")
                continue
            
            if scelta in self.corso:
                print("Questo corso e gia presente nel registro")
            else:
                self.corso.append(scelta)
                print(f"{scelta} aggiunto con successo!")

        return self.corso

    def saluta(self):
        Persona.saluta(self)
        print(f"Corsi insegnati: {self.corso}")

docente1 = Docente("Fabris", "Del Santo")
docente1.aggiungi_corso()

docente2 = Docente("Matteo", "Gallet")
docente2.aggiungi_corso()


print(docente1.saluta())
print(docente2.saluta())

obj_Irene = Studente("Irene", "Rossi")
obj_Irene.saluta()

obj_Irene.calcolo(docente1)
obj_Irene.calcolo(docente2)