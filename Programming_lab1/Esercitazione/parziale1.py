#FRANCK CHRISTY KAMDEM WADJOUNUE SM32A00110

import csv

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self, name):
        self.name = name

        try:
            with open(self.name, 'r') as file:
                pass
        except FileNotFoundError:
            raise ExamException("File non esistente o non leggibile!")
        

    def get_data(self):

        data = []
        last_date = None

        with open(self.name, 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if len(row) < 2:
                    print("Riga ignorata!")
                    continue

                date = row[0].strip()
                raw_value = row[1].strip()

                if not raw_value.isdigit():
                    print("Riga ignorata!")
                    continue

                parts = date.split("/")

                if len(parts) != 2 and not (parts[0].isdigit() and parts[1].isdigit()):
                    print("Riga ignorata, la data non e' sul formato corretto")

                if last_date is not None:
                    if date <= last_date:
                        print("Riga ignorata")

                last_date = date 
                date = str(date)

                try:
                    value = float(raw_value)
                    if value <= 0:
                        print("I dati di consumption devono essere positivo")
                except:
                    raise ExamException("I valori devono essere dei float")

                data.append([date, value])

            return data   

def compute_annual_mean(times_series, first_year, last_year):

    if not isinstance(first_year, int) and not isinstance(last_year, int):
        raise ExamException("Gli anni devono essere dei numeri interi")

    if first_year >= last_year:
        raise ExamException(f"The first year '{first_year}' deve essere precedente del last year '{last_year}'")
    
    passengers_per_year = {}

    for entry in times_series:
        year = entry[0].split("/")[1]

        if year not in passengers_per_year:
            passengers_per_year[year] = []

        passengers_per_year[year].append(entry[1])

    all_years = sorted(passengers_per_year.keys())

    years_in_range = [y for y in all_years if first_year <= int(y) <= last_year]

    medie = {}

    for year in years_in_range:
        values = passengers_per_year[year]
        if values:
            medie[year] = round(sum(values) / len(values), 2)

    return medie

times_series_file = CSVTimeSeriesFile(name='Programming_lab1/Esercitazione/file/electricity.csv')
times_series = times_series_file.get_data()

print(times_series)

print(compute_annual_mean(times_series, 2019, 2021))