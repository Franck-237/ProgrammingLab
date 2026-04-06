
import csv

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():

    def __init__(self, name):
        self.name = name

    def get_data(self):
        data = []
        last_data = None

        try:
            with open(self.name, "r") as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    if len(row) < 2:
                        print(f"Riga ignorata (incompleta): {row}")
                        continue
                    
                    date = row[0].strip()
                    raw_value = row[1].strip()

                    parts = date.split("-")

                    if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
                        print(f"Riga ignorata (data non valida): {row}")
                        continue

                    if last_data is not None:
                        if date <= last_data:
                            raise ExamException(f"Errore: timestamp fuori ordine o duplicato: {date}")
                        
                    try:
                        value = int(raw_value)
                        if value <= 0:
                            print(f"Riga igmorata (valore non positivo): {row}")

                    except ValueError:
                        print(f"Riga ignorata (valore non numerico): {row}")
                        continue
        except FileNotFoundError:
            raise ExamException(f"Errore: il file '{self.name}' non esiste o non e leggibile")
        
        return data
    
def compute_variations(time_series, first_year, last_year):

    if not isinstance(first_year, str) or not isinstance(last_year, str):
        raise ExamException("Errore: fisrt year e last year devono essere stringhe.")
    

    passengers_per_year = {}
    for entry in time_series:
        year = entry[0].split("-")[0]

        if year not in passengers_per_year:
            passengers_per_year[year] = []
        passengers_per_year[year].append(entry[1])

    if first_year not in passengers_per_year:
        raise ExamException(f"Errore: l'anno {first_year} non è presente nei dati.")
    
    if last_year not in passengers_per_year:
        raise ExamException(f"Errore: l'anno {last_year} non è presente nei dati.")

    if first_year >= last_year:
        raise ExamException(f"Errore: first year deve essere precedente a last year")
    
    all_years = sorted(passengers_per_year.keys())
    years_in_range = [y for y in all_years if first_year <= y <= last_year]

    medie = {}

    for year in years_in_range:
        values = passengers_per_year[year]
        if values:
            medie[year] = sum(values) / len(values)

    years_with_data = sorted(medie.keys())
    result = {}

    for i in range(1, len(years_with_data)):
        prev_year = years_with_data[i - 1]
        curr_year = years_with_data[i]

        key = f"{prev_year} - {curr_year}"
        result[key] = round(medie[curr_year] - medie[prev_year], 2)

    return result


times_series_file = CSVTimeSeriesFile(name="Esercitazione/file/data.csv")
time_series = times_series_file.get_data()

print(time_series)

# varazioni = compute_variations(time_series, "1949", "1951")
# print(varazioni)