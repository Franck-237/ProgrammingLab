import csv

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name

    def get_data(self, building_name):
        data_list = []
        building_found = False

        try:
            with open(self.name, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    if len(row) < 3:
                        continue

                    dt = row[0].strip()
                    consumo_str = row[1].strip()
                    building = row[2].strip()

                    if building != building_name:
                        continue

                    building_found = True

                    try:
                        consumo = float(consumo_str)
                    except ValueError:
                        continue

                    data_list.append([dt, consumo])

        except FileNotFoundError:
            raise ExamException("Error: il file non esiste")
        
        if not building_found:
            raise ExamException("Error: il nome dell'edificio non e' presente nel file")
        
        return data_list
    
def annual_averages(times_series, first_year, last_year):

    anni_dati = {}

    for data_str , consumo in times_series:
        try:
            anno = int(data_str.split("-")[0])
        except (IndexError, ValueError):
            continue

        if anno < first_year or anno > last_year:
            continue

        if anno not in anni_dati:
            anni_dati[anno] = []
        anni_dati[anno].append(consumo)

    medie = {}

    for anno, consumi in anni_dati.items():
        if consumi:
            media = sum(consumi) / len(consumi)
            medie[anno] = round(media, 2)

    return medie


def computes_variations(times_series_1, times_series_2, first_year, last_year):

    if not isinstance(first_year, int):
        raise ExamException("Error: l'anno inserito non e' un intero")
    if not isinstance(last_year, int):
        raise ExamException("Error: l'anno inserito non e' un intero")
    
    if first_year > last_year:
        first_year, last_year = last_year, first_year

    medie_1 = annual_averages(times_series_1, first_year, last_year)
    medie_2 = annual_averages(times_series_2, first_year, last_year)

    if not medie_1 and not medie_2:
        raise ExamException("Error: l'intervallo selezionato non contiene valori validi")
    

    differenze = {}

    for anno in medie_1:
        if anno in medie_2:
            diff =  medie_2[anno] - medie_1[anno]
            differenze[anno] = round(diff, 2)

    return differenze

time_series_file = CSVTimeSeriesFile(name="Programming_lab1/Esercitazione/file/ElectricityByBuilding.csv")
time_series_A = time_series_file.get_data("A")
time_series_B = time_series_file.get_data("B")
print(time_series_A)
print(computes_variations(time_series_A, time_series_B, 2019, 2022))