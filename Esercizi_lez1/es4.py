def conta_lettera(parola, lettera):
    # count = 0

    # for carattere in parola:
    #     if carattere == lettera:
    #         count += 1
        
    # return count
    return parola.count(lettera) #modo piu esperto e avanzato


risultato = conta_lettera("Programmazione", "r")
print(f"La lettera 'r' compare {risultato} volte.")
