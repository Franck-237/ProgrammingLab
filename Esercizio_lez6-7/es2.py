
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
    
class NumericalCSVFile(CSVFile):

    def get_data(self):
        raw_data = super().get_data()
        
        if isinstance(raw_data, str):
            return raw_data
        
        data = []

        for row in raw_data:
            try:
                converted_row = [row[0]] + [float(val) for val in row[1:]]
                data.append(converted_row)
           
            
            except ValueError as e:
                return f"Errore nella riga {row}: {e}."



file_path = "Esercizi_lez3/files/shampoo_sales.csv"
with open(file_path, "a") as file:
    file.write("01-01-2015,\n01-02-2015,ciao")


mio_file = CSVFile(file_path)
mio_file1 = NumericalCSVFile(file_path)

print(f"Nome del file: {mio_file.name}")

dati = mio_file.get_data()
dati1 = mio_file1.get_data()
print("Dati estratti: ")
print(dati)
print(dati1)