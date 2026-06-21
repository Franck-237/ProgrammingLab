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
            raise ExamException("File non esistente o non leggibile")

    def get_data(self, country):

        data_list = []
        country_found = False

        try:
            with open(self.name, 'r') as file:
                reader = csv.reader(file)
                next(reader)

                for row in reader:
                    if len(row) < 4:
                        continue

                    dt = row[0].strip()
                    tmp = row[1].strip()
                    inct = row[2].strip()
                    country_name = row[3].strip()

                    if country_name != country:
                        continue

                    country_found = True

                    try:
                        temperatura = float(tmp)
                    except ValueError:
                        continue
                    
                    try:
                        incertezza = float(inct)
                    except ValueError:
                        continue

                    if incertezza >= 5:
                        continue

                    data_list.append([dt, temperatura, incertezza])
            
        except Exception as e:
            raise ExamException(f"Errore: {e}")
        
        if not country_found:
            raise ExamException("Errore: il paese richiesto non e' presente nel file")
        
        return data_list

def compute_cons_variation_compare(times_series1, times_series2, year):

    if not isinstance(year, int):
        raise ExamException("Errore: anno non valido, deve essere intero")
    
    def extract_year_data(time_series, year):

        monthly_data = {}

        for data_str, temp, uncertainty in time_series:
            try:
                parts = data_str.split("/")
                if len(parts) != 2:
                    continue

                mese = int(parts[0])
                anno = int(parts[1])
            except (ValueError, AttributeError):
                continue

            if anno != year:
                continue

            monthly_data[mese] = [temp, uncertainty]

        return monthly_data
    
    data1 = extract_year_data(times_series1, year)
    data2 = extract_year_data(times_series2, year)

    anni_possibili = set()

    for time_series in [times_series1, times_series2]:
        for data_str, _, _ in time_series:
            try:
                parts = data_str.split('/')
                if len(parts) == 2:
                    anno = int(parts[1])
                    anni_possibili.add(anno)
            except (ValueError, AttributeError):
                continue

    if not anni_possibili:
        if year not in data1 and year not in data2:
            raise ExamException("Errore: l'anno indicato non rientra nella copertura del dataset")
    else:
        if year not in anni_possibili:
            raise ExamException("Errore: l'anno indicato non rientra nella copertura del dataset")
        

    if not data1 and not data2:
        raise ExamException("Errore: l'anno indicato npon rientra nella copertura del dataset")
    

    result = {}

    for m in range(1, 12):
        m_plus = m + 1

        if m not in data1 or m_plus not in data1:
            continue
        if m not in data2 or m_plus not in data2:
            continue

        t1_m , u1_m = data1[m]
        t1_mp, u1_mp = data1[m_plus]

        t2_m, u2_m = data2[m]
        t2_mp, u2_mp = data2[m_plus]

        delta1 = t1_mp - t1_m
        uncertainty1 = u1_m + u1_mp

        delta2 = t2_mp - t2_m
        uncertainty2 = u2_m + u2_mp

        diff_delta = delta2 - delta1

        total_uncertainty = uncertainty1 + uncertainty2

        result[m] = [diff_delta, total_uncertainty]

    if not result:
        raise ExamException("Errore: nessuna coppia di mesi valida per il confronto tra gli anni indicati")
    
    return result

ts_file = CSVTimeSeriesFile(name="Programming_lab1/Esercitazione/file/GlobalLandTemperaturesByCountry.csv") 
time_series_italy = ts_file.get_data(country="Italy")
time_series_france = ts_file.get_data(country="France")
        
result = compute_cons_variation_compare(time_series_italy, time_series_france, 2000)
        
print("Confronto variazioni mensili consecutive (Italia vs Francia) per il 2000:")
for mese, (diff, incertezza) in result.items():
    print(f"Mese {mese}->{mese+1}: differenza = {diff:.4f}°C, incertezza = {incertezza:.4f}")