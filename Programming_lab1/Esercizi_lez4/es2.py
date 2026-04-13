
import csv

class CSVFile:

    def __init__(self, name):
        self.name = name

    def get_data(self):
        data = []

        try:
            with open(self.name, "r") as file:
                reader = csv.reader(file)

                next(reader)

                for row in reader:
                    data.append(row)

        except FileNotFoundError:
            return f"Errore: il file {self.name} non esiste."
        
        return data
    
file_path = "Esercizi_lez4/file.csv"
mio_file = CSVFile(file_path)

print(f"Nome del file: {mio_file.name}")

dati = mio_file.get_data()
print("Dati estratti: ")
print(dati[:3])