import csv

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
 
        self.name = name
        
        # Controllo esistenza e leggibilità del file (richiesto nell'init)
        try:
            with open(self.name, 'r', encoding='utf-8') as file:
                # Verifica che il file non sia vuoto
                first_line = file.readline()
                if not first_line:
                    raise ExamException("Errore: impossibile aprire o leggere il file")
        except (FileNotFoundError, PermissionError, IOError):
            raise ExamException("Errore: impossibile aprire o leggere il file")

    def get_data(self):

        data_list = []

        try:
            with open(self.name, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                header = next(reader)  # salta l'intestazione
                
                # Trovo gli indici delle colonne
                dt_idx = -1
                max_idx = -1
                min_idx = -1
                
                for i, col in enumerate(header):
                    col_clean = col.strip().lower()
                    if 'dt' in col_clean:
                        dt_idx = i
                    elif 'landmaxtemperature' in col_clean:
                        max_idx = i
                    elif 'landmintemperature' in col_clean:
                        min_idx = i
                
                # Se non trovo le colonne, uso posizioni fisse (fallback)
                if dt_idx == -1:
                    dt_idx = 0
                if max_idx == -1:
                    max_idx = 1
                if min_idx == -1:
                    min_idx = 2

                for row in reader:
                    # Controllo che la riga abbia almeno 3 colonne
                    if len(row) < 3:
                        continue

                    dt = row[dt_idx].strip()
                    max_str = row[max_idx].strip()
                    min_str = row[min_idx].strip()

                    # Se la data è vuota, ignoro la riga
                    if not dt:
                        continue

                    # Se la temperatura massima è vuota, ignoro la riga
                    if not max_str:
                        continue

                    # Se la temperatura minima è vuota, ignoro la riga
                    if not min_str:
                        continue

                    # Conversione temperature a float
                    try:
                        t_max = float(max_str)
                    except ValueError:
                        # Valore non numerico: ignoro la riga (senza eccezioni)
                        continue

                    try:
                        t_min = float(min_str)
                    except ValueError:
                        # Valore non numerico: ignoro la riga (senza eccezioni)
                        continue

                    # Scarto temperature fuori range
                    # t_min < -50°C o t_max > 50°C (senza stampa)
                    if t_min < -50 or t_max > 50:
                        continue

                    # Scarto righe con t_min > t_max (con stampa)
                    if t_min > t_max:
                        print(f"Valori scartati: data={dt}, t_min={t_min}, t_max={t_max}")
                        continue

                    # Aggiungo la lista [data, t_min, t_max]
                    data_list.append([dt, t_min, t_max])

        except Exception as e:
            # Gestione di eventuali errori di lettura
            raise ExamException(f"Errore: impossibile aprire o leggere il file")

        return data_list

def compute_monthly_spread_diff(time_series, first_year, second_year):
    
    # Validazione: first_year e second_year devono essere interi
    if not isinstance(first_year, int):
        raise ExamException("Errore: anni non validi (devono essere interi e in ordine crescente)")
    if not isinstance(second_year, int):
        raise ExamException("Errore: anni non validi (devono essere interi e in ordine crescente)")
    
    # Validazione: first_year < second_year
    if first_year >= second_year:
        raise ExamException("Errore: anni non validi (devono essere interi e in ordine crescente)")
    
    # Determinare l'intervallo di anni coperti dai dati
    anni_presenti = set()
    for data_str, _, _ in time_series:
        try:
            anno = int(data_str.split('-')[0])
            anni_presenti.add(anno)
        except (ValueError, AttributeError, IndexError):
            continue
    
    # Se non ci sono anni, sollevo eccezione
    if not anni_presenti:
        raise ExamException("Errore: gli anni indicati non rientrano nella copertura del dataset")
    
    # Validazione: first_year e second_year devono essere nella copertura
    if first_year not in anni_presenti:
        raise ExamException("Errore: gli anni indicati non rientrano nella copertura del dataset")
    if second_year not in anni_presenti:
        raise ExamException("Errore: gli anni indicati non rientrano nella copertura del dataset")
    
    # Funzione helper per estrarre gli spread per un anno specifico
    def extract_spreads_for_year(time_series, year):

        monthly_spreads = {}
        
        for data_str, t_min, t_max in time_series:
            # Estraggo anno e mese dalla stringa "YYYY-MM-DD"
            try:
                parts = data_str.split('-')
                if len(parts) != 3:
                    continue
                anno = int(parts[0])
                mese = int(parts[1])
            except (ValueError, AttributeError, IndexError):
                # Formato non valido: ignoro
                continue
            
            # Se l'anno non corrisponde, salto
            if anno != year:
                continue
            
            # Calcolo lo spread: T_max - T_min
            spread = t_max - t_min
            
            # Salvo lo spread per questo mese (se duplicato, sovrascrivo)
            monthly_spreads[mese] = spread
        
        return monthly_spreads
    
    # Estraggo gli spread per entrambi gli anni
    spreads_first = extract_spreads_for_year(time_series, first_year)
    spreads_second = extract_spreads_for_year(time_series, second_year)
    
    # Trovo i mesi presenti in entrambi gli anni
    mesi_first = set(spreads_first.keys())
    mesi_second = set(spreads_second.keys())
    
    # Stampo messaggi per i mesi non presenti in uno o entrambi gli anni
    for mese in range(1, 13):
        if mese not in mesi_first or mese not in mesi_second:
            print(f"La variazione per il mese {mese} non può essere calcolata")
    
    # Trovo i mesi presenti in entrambi gli anni
    mesi_comuni = mesi_first.intersection(mesi_second)
    
    # Se non ci sono mesi comuni, sollevo eccezione
    if not mesi_comuni:
        raise ExamException("Errore: nessun mese confrontabile tra gli anni indicati")
    
    # Calcolo le differenze per i mesi comuni
    result = {}
    for mese in mesi_comuni:
        spread1 = spreads_first[mese]
        spread2 = spreads_second[mese]
        differenza = spread2 - spread1
        result[mese] = differenza
    
    return result

if __name__ == "__main__":
    try:
        # Lettura dati
        ts_file = CSVTimeSeriesFile(name="GlobalTemperaturesMaxMin.csv")
        time_series = ts_file.get_data()
        
        # Calcolo differenza spread tra 1900 e 2000
        diff_spread = compute_monthly_spread_diff(time_series, 1900, 2000)
        
        print("\nDifferenza spread mensile (2000 - 1900):")
        for mese, differenza in sorted(diff_spread.items()):
            print(f"Mese {mese}: {differenza:.4f}°C")
        
    except ExamException as e:
        print(f"Errore: {e}")