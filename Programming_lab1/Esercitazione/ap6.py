import csv

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name
        
        # Controllo esistenza e leggibilità del file (richiesto nell'init)
        try:
            with open(self.name, 'r') as file:
                # Verifica che il file non sia vuoto
                first_line = file.readline()
                if not first_line:
                    raise ExamException("Errore: impossibile aprire il file")
        except (FileNotFoundError, PermissionError, IOError):
            raise ExamException("Errore: impossibile aprire il file")

    def get_data(self):
        data_list = []

        try:
            with open(self.name, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)  # salta l'intestazione
                
                # Trovo gli indici delle colonne
                dt_idx = -1
                temp_idx = -1
                
                for i, col in enumerate(header):
                    col_clean = col.strip().lower()
                    if 'dt' in col_clean:
                        dt_idx = i
                    elif 'temperature' in col_clean or 'avg' in col_clean:
                        temp_idx = i
                
                # Se non trovo le colonne, uso le prime due (fallback)
                if dt_idx == -1:
                    dt_idx = 0
                if temp_idx == -1:
                    temp_idx = 1

                for row in reader:
                    # Controllo che la riga abbia almeno 2 colonne
                    if len(row) < 2:
                        continue

                    dt = row[dt_idx].strip()
                    temp_str = row[temp_idx].strip()

                    # Se la data è vuota, ignoro la riga
                    if not dt:
                        continue

                    # Se la temperatura è vuota, ignoro la riga
                    if not temp_str:
                        continue

                    # Conversione temperatura a float
                    try:
                        temperatura = float(temp_str)
                    except ValueError:
                        # Valore non numerico: ignoro la riga (senza eccezioni)
                        continue

                    # Se la temperatura è negativa, ignoro la riga
                    if temperatura < 0:
                        continue

                    # Aggiungo la coppia [data, temperatura]
                    data_list.append([dt, temperatura])

        except Exception as e:
            # Gestione di eventuali errori di lettura
            raise ExamException(f"Errore: impossibile aprire il file")

        return data_list

def compute_variations(time_series, first_year, last_year, N):
    
    # Validazione: first_year e last_year devono essere interi
    if not isinstance(first_year, int):
        raise ExamException("Errore: l'anno inserito non è un intero")
    if not isinstance(last_year, int):
        raise ExamException("Errore: l'anno inserito non è un intero")
    
    # Validazione: first_year deve essere minore o uguale a last_year
    if first_year > last_year:
        raise ExamException("Errore: l'intervallo non è valido")
    
    # Validazione: N deve essere intero positivo
    if not isinstance(N, int):
        raise ExamException("Errore: N deve essere un intero")
    if N <= 0:
        raise ExamException("Errore: N deve essere maggiore di 0")
    
    # Calcolo la lunghezza dell'intervallo
    interval_length = last_year - first_year + 1
    
    # Validazione: N deve essere minore della lunghezza dell'intervallo
    if N >= interval_length:
        raise ExamException("Errore: N deve essere minore della lunghezza dell'intervallo")
    
    # Raggruppamento temperature per anno
    anni_temperature = {}
    
    for data_str, temp in time_series:
        # Estraggo l'anno dalla stringa "YYYY-MM-DD"
        try:
            # Divido per '-' e prendo il primo elemento
            anno = int(data_str.split('-')[0])
        except (ValueError, AttributeError, IndexError):
            # Formato data non valido: ignoro questa riga
            continue
        
        # Se l'anno è fuori dall'intervallo richiesto, salta
        if anno < first_year or anno > last_year:
            continue
        
        # Aggiungo temperatura all'anno corrispondente
        if anno not in anni_temperature:
            anni_temperature[anno] = []
        anni_temperature[anno].append(temp)
    
    # Calcolo la media annuale per ogni anno
    # Nota: se mancano misurazioni per alcuni mesi, la media viene calcolata
    # sul numero di mesi disponibili (come richiesto)
    medie_annuali = {}
    
    for anno, temps in anni_temperature.items():
        if temps:  # Se ho almeno una temperatura
            media = sum(temps) / len(temps)
            medie_annuali[anno] = media
    
    # Ordino gli anni per avere una lista sequenziale
    anni_ordinati = sorted(medie_annuali.keys())
    
    # Se non ci sono anni validi, sollevo eccezione
    if not anni_ordinati:
        raise ExamException("Errore: nessun dato valido nell'intervallo")
    
    # Calcolo le differenze usando la media mobile degli N anni precedenti
    result = {}
    
    # Devo partire da first_year + N (perché devo avere almeno N anni precedenti)
    for anno in anni_ordinati:
        # Calcolo l'anno di partenza per la media mobile
        start_year = anno - N
        
        # Se start_year è minore di first_year, non ho abbastanza anni precedenti
        # all'interno dell'intervallo considerato
        if start_year < first_year:
            continue
        
        # Raccogli le medie degli N anni precedenti (anno-N, ..., anno-1)
        # che devono essere all'interno dell'intervallo e disponibili
        prev_medias = []
        for prev_year in range(anno - N, anno):
            if prev_year in medie_annuali:
                prev_medias.append(medie_annuali[prev_year])
        
        # Se non ho tutti gli N anni precedenti, salto questo anno
        if len(prev_medias) < N:
            continue
        
        # Calcolo la media mobile degli N anni precedenti
        media_mobile = sum(prev_medias) / N
        
        # Calcolo la differenza: media annuale - media mobile
        differenza = medie_annuali[anno] - media_mobile
        
        # Salvo il risultato
        result[anno] = differenza
    
    return result

if __name__ == "__main__":
    try:
        # Lettura dati
        time_series_file = CSVTimeSeriesFile(name='GlobalTemperatures.csv')
        time_series = time_series_file.get_data()
        
        # Calcolo variazioni per l'intervallo 1900-1904 con N=3
        variazioni = compute_variations(time_series, 1900, 1904, 3)
        
        print("Variazioni rispetto alla media mobile degli ultimi 3 anni:")
        for anno, valore in variazioni.items():
            print(f"Anno {anno}: {valore:.4f}°C")
        
    except ExamException as e:
        print(f"Errore: {e}")