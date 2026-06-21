import csv
from datetime import datetime

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name

        try:
            with open(self.name, "r")  as file:
                pass
        except FileNotFoundError:
            raise ExamException("Errore: impossibile aprire il file")
        
    def get_data(self):

        data_list = []

        try:
            with open(self.name, "r") as file:
                reader = csv.reader(file)
                header = next(reader)

                dt_idx = -1
                temp_idx = -1
                uncertainty_idx = -1

                for i, col in enumerate(header):
                    col_clean = col.strip()
                    if "dt" in col_clean.lower():
                        dt_idx = i
                    elif "LandAverageTemperature" in col_clean and "Uncertainty" not in col_clean:
                        temp_idx = i
                    elif "LanAverageTemperatureUncertainty" in col_clean:
                        uncertainty_idx = i

                
                if dt_idx == -1:
                    dt_idx = 0
                if temp_idx == -1:
                    temp_idx = 1
                if uncertainty_idx == -1:
                    uncertainty_idx = 2

                for row in reader:
                    if len(row) < 3:
                        continue

                    dt = row[dt_idx].strip()
                    temp_str = row[temp_idx].strip()
                    uncertainty_str = row[uncertainty_idx].strip()

                    try:
                        temperatura = float(temp_str)
                    except ValueError:
                        continue

                    try:
                        incertezza = float(uncertainty_str)
                    except ValueError:
                        continue

                    if incertezza >= 5:
                        print("Data saltata perche il valore troppo incerto")
                        continue

                    data_list.append([dt, temperatura])

        except Exception as e:
            raise ExamException(f"Errore durante la lettura del file: {e}")
        
def compute_month_variation(times_series, first_year, second_year):

    if not isinstance(first_year, int):
        raise ExamException("Errore: gli anni inseriti devono essere di tipo intero.")
    if not isinstance(second_year, int):
        raise ExamException("Errore: gli anni inseriti devono essere di tipo intero.")

    if second_year <= first_year:
        raise ExamException("Errore: il secondo anno deve essere maggiore del primo.")
    
    anni_mesi = {}

    for data_str, temp in times_series:

        try:
            data_obj = datetime.strptime(data_str, '%d/%m/%y')
            anno = data_obj.year
            mese = data_obj.month
        except (ValueError, TypeError):
            continue

        if anno != first_year and anno != second_year:
            continue

        if anno not in anni_mesi:
            anni_mesi[anno] = {}
        if mese not in anni_mesi[anno]:
            anni_mesi[anno][mese] = []

        anni_mesi[anno][mese].append(temp)

    medie_mensili = {}

    for anno, mesi in anni_mesi.items():
        medie_mensili[anno] = {}

        for mese, temps in mesi.items():
            if temps:
                media = sum(temps) / len(temps)
                medie_mensili[anno][mese] = media

    if first_year not in medie_mensili:
        medie_mensili[first_year] = {}

    if second_year not in medie_mensili:
        medie_mensili[second_year] = {}

    mesi_primo = set(medie_mensili[first_year].keys())
    mesi_secondo = set(medie_mensili[second_year].keys())
    mesi_comuni = mesi_primo.intersection(mesi_secondo)


    if not mesi_comuni:
        raise ExamException("Gli anni considerati non hanno mesi validi")
    
    variazioni = {}

    for mese in mesi_comuni:
        if mese not in mesi_primo:
            print(f"La variazione per il mese {mese} non può essere calcolata")
            continue
        if mese not in mesi_secondo:
            print(f"La variazione per il mese {mese} non può essere calcolata")
            continue
        

        variazione = medie_mensili[second_year][mese] - medie_mensili[first_year][mese]
        variazioni[mese] = variazione
    
    if not variazioni:
        raise ExamException("Gli anni considerati non hanno mesi validi")
    
    return variazioni

time_series_file = CSVTimeSeriesFile("Programming_lab1/Esercitazione/file/Temperatures.csv")
data = time_series_file.get_data()
        
variazioni = compute_month_variation(data, 1900, 2000)
print("Variazioni mensili (1900 -> 2000):")
for mese, variazione in sorted(variazioni.items()):
    print(f"Mese {mese}: {variazione:.4f}°C")