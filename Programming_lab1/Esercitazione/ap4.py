import csv

class ExamException(Exception):
    pass


class CSVTimeSeriesFile:

    def __init__(self, name):
        self.name = name

        try:
            with open(self.name, "r") as file:
                pass
        except FileNotFoundError:
            raise ExamException("Errore: impossibile aprire o leggetre il file")
        

    def get_data(self):

        data_list = []

        try:
            with open(self.name, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    if len(row) < 2:
                        continue

                    dt = row[0].strip()
                    tmp = row[1].strip()

                    try:
                        temperatura = float(tmp)
                    except ValueError:
                        continue

                    data_list.append([dt, temperatura])

        except Exception as e:
            raise ExamException(f"Errore: impossibile aprire o leggere il file")
        
        return data_list
    
def compute_anomaly(times_series, baseline_start, baseline_end, year):

    if not isinstance(baseline_start, int):
        raise ExamException("Errore: intervallo di baseline non valido")
    if not isinstance(baseline_end, int):
        raise ExamException("Errore: intervallo di baseline non valido")
    
    if baseline_start >= baseline_end:
        raise ExamException("Errore: intervallo di baseline non valido")
    
    if not isinstance(year, int):
        raise ExamException("Errore: anno non valido")
    
    if year < baseline_start or year > baseline_end:
        raise ExamException("Errore: anno non valido")
    
    anni_temperature = {}

    for entry in times_series:
        year = entry[0].split("/")[0]

        if year not in anni_temperature:
            anni_temperature[year] = []
        anni_temperature[year].append(entry[1])

    medie_annuali = {}

    for anno, temps in anni_temperature.items():
        if len(temps) >= 9:
            media = sum(temps) / len(temps)
            medie_annuali[anno] = media

    anni_validi_baseline = []

    for anno in medie_annuali:
        if baseline_start <= int(anno) <= baseline_end:
            anni_validi_baseline.append(anno)

    if not anni_validi_baseline:
        raise ExamException("Errore: baseline priva di anni validi")
    
    sum_baseline = sum(medie_annuali[anno] for anno in anni_validi_baseline)
    baseline_mean = sum_baseline / len(anni_validi_baseline)

    if year not in medie_annuali:
        raise ExamException("Errore: anno  richiesto privo di dati sufficienti")
    
    anomalia = medie_annuali[year] - baseline_mean

    return anomalia

time_series_file = CSVTimeSeriesFile("Programming_lab1/Esercitazione/file/GlobalTemperatures.csv")
data = time_series_file.get_data()
        
        # Calcolo anomalia per l'anno 2015 rispetto alla baseline 1950-1980
anomalia = compute_anomaly(data, 1950, 1980, 1960)
print(f"Anomalia di temperatura per il 1960: {anomalia:.4f}°C")