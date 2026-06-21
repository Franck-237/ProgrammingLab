import csv 

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self, name):
        self.name = name

    def get_data(self, City):

        data_list = []
        city_found = False

        try:
            with open(self.name, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    if len(row) < 3:
                        continue

                    dt = row[0].strip()
                    temperatura = row[1].strip()
                    city = row[3].strip()

                    if city != City:
                        continue

                    city_found = True

                    try:
                        tmp = float(temperatura)
                    except ValueError:
                        continue

                    data_list.append([dt, tmp])

                if not city_found:
                    raise ExamException("Errore: il nome della citta non e' presente nel file.")
                
            return data_list
        
        except FileNotFoundError:
            raise ExamException("Errore: impossibile aprire il file")


def compute_slope(times_series, first_year, last_year):

    if not isinstance(first_year, int):
        raise ExamException("Errore: l'anno inserito non e' un intero")
    if not isinstance(last_year, int):
        raise ExamException("Errore: l'anno inserito non e' un intero")
    
    if first_year > last_year:
        first_year, last_year = last_year, first_year

    if first_year == last_year:
        pass

    anni_temp = {}

    for data_str, temp in times_series:

        try:
            anno = int(data_str.split("-")[0])
        except (IndexError, ValueError):
            continue

        if anno < first_year or anno > last_year:
            continue

        if anno not in anni_temp:
            anni_temp[anno] = []
        anni_temp[anno].append(temp)

    anni_validi = {}

    for anno, temps in anni_temp.items():
        if len(temps) >= 6:
            media_annuale = sum(temps) / len(temps)
            anni_validi[anno] = media_annuale

    if not anni_validi:
        raise ExamException("Errore: l'intervallo selezionato non contiene valori validi")
    

    n = len(anni_validi)

    x_values = list(anni_validi.keys())
    y_values = list(anni_validi.values())

    x_mean = sum(x_values) / n
    y_mean = sum(y_values) / n

    numeratore = 0
    denominatore = 0

    for i in range(n):
        xi = x_values[i]
        yi = y_values[i]

        numeratore += (xi - x_mean) * (yi - y_mean)
        denominatore += (xi - x_mean) ** 2

    if denominatore == 0:
        raise ExamException("Errore: denominatore zero nel calcolo del cefficiente angolare")
    
    m = numeratore / denominatore

    return m

time_series_file = CSVTimeSeriesFile(name="Programming_lab1/Esercitazione/file/GlobalLandTemperaturesByMajorCity.csv") 
time_series_italy = time_series_file.get_data(City="Rome")

slope = compute_slope(time_series_italy, 2000, 2010)
print(f"Coefficiente angolare per Roma (2000-2010): {slope:.6f}")

# print(time_series_italy)
