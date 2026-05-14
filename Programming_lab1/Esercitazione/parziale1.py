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
            raise ExamException("File non esistente!!")

    def get_data(self):

        data = []
        last_date = None

        with open(self.name, 'r') as file:
            reader = csv.reader(file)
            next(reader)

        
            for row in reader:

                if len(row) < 2:
                    print("Riga ignorata")
                    continue

                date = row[0].strip()
                raw_value = row[1].strip()

                parts = date.split("/")

                if len(parts) != 2 and not (parts[0].isdigit() and parts[1].isdigit()):
                    print("Riga ignorata la data non ha il formato corretto")
                    continue

                if last_date is not None:
                    if date <= last_date:
                        print("Riga ignorata!")

                last_date = date
                date = str(date)

                if not raw_value.isdigit():
                    continue

                try:
                    value = float(raw_value)
                    if value <= 0:
                        print("Riga ignorata")
                        continue
                except ValueError:
                    raise ExamException("I valori devono essere dei float!")
                

                data.append([date, value])

            return data

def compute_annual_mean(times_series, first_year, last_year):

    if not isinstance(first_year, int) and not isinstance(last_year, int):
        raise ExamException("Anni devono essere interi")
    
    if first_year >= last_year:
        raise ExamException(f"{first_year} deve essere precedente di {last_year}.")
    
    passengers_per_year = {}

    for entry in times_series:

        year = entry[0].split("/")[1]

        if year not in passengers_per_year:
            passengers_per_year[year] = []
        passengers_per_year[year].append(entry[1])

    all_years = sorted(passengers_per_year.keys())

    medie = {}

    years_in_range = [y for y in all_years if first_year <= int(y) <= last_year]

    for year in years_in_range:
        values = passengers_per_year[year]
        medie[year] = round(sum(values) / len(values), 2)

    return medie

times_series_file = CSVTimeSeriesFile(name= "Programming_lab1/Esercitazione/file/electricity.csv")
times_series = times_series_file.get_data()

print(times_series)

print(compute_annual_mean(times_series, 2019, 2021))