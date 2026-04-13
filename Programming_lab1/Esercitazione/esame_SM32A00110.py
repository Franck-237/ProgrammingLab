import csv

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self, name):
        self.name = name

    def get_data(self):
        data = []
        last_date = None #Serve per rilevare ordine e duplicati

        try:
            with open(self.name, "r") as file:
                reader = csv.reader(file)
                next(reader) #salta la riga "date, passengers"

                for row in reader:

                    if len(row) < 2:
                        print("Riga ignorata")
                        continue

                    date = row[0].strip()
                    raw_value = row[1].strip()

                    parts = date.split("-")

                    if len(parts) != 2 or not (parts[0].isdigit() and parts[1].isdigit()):
                        print("Riga ignorata non e sul formato YYYY-MM")
                        continue

                    if last_date is not None:
                        if date <= last_date:
                            raise ExamException("Timestamp fuori ordine o duplicato")
                        
                    last_date = date

                    try:
                        value = int(raw_value)
                        if value <= 0:
                            print("Riga ignorata")
                            continue
                    except ValueError:
                        print(f"Riga ignorata")
                        continue

                    data.append([date, value])

        except FileNotFoundError:
            raise ExamException("File non trovato o non leggibile.")
        

        return data

def compute_variations(times_series, first_year, last_year):

    if not isinstance(first_year, str) or not isinstance(last_year, str):
        raise ExamException("fisrt_year e last_year devono essere stringhe.")
    
    if first_year >= last_year:
        raise ExamException("first_year deve essere precedente a last_year.")
    
    # Dizionario: {"1949": [112, 118, 132, .....], "1950": [.....], ....}
    passengers_per_yer = {}

    for entry in times_series:
        year = entry[0].split("-")[0] # "1949-01" -> "1949"

        if year not in passengers_per_yer:
            passengers_per_yer[year] = []
        passengers_per_yer[year].append(entry[1])

    if first_year not in passengers_per_yer:
        raise ExamException("Anno non presente nei dati.")
    if last_year not in passengers_per_yer:
        raise ExamException("Anno non presente nei dati.")
    
    all_years = sorted(passengers_per_yer.keys())
    # print(all_years)

    years_in_range = [y for y in all_years if first_year <= y <= last_year]
    # print(years_in_range)

    medie = {}

    for year in years_in_range:
        values = passengers_per_yer[year]
        if values:
            medie[year] = sum(values) / len(values)

    years_in_range = []
    for y in all_years:
        if first_year <= y <= last_year:
            years_in_range.append(y)

        years_with_data = sorted(medie.keys())
        result = {}

        for i in range(1, len(years_with_data)):
            prev_year = years_with_data[i-1]
            curr_year = years_with_data[i]

            key = f"{prev_year}-{curr_year}"
            result[key] = round(medie[curr_year] - medie[prev_year], 2)

        return result
    
times_series_file = CSVTimeSeriesFile(name="Programming_lab1/Esercitazione/file/data.csv")
times_series = times_series_file.get_data()

print(times_series)

variations = compute_variations(times_series, "1949", "1951")
print(variations)