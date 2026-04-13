class ExamException(Exception):
    pass

class MovingAverage():

    def __init__(self, lunghezza):
        if not isinstance(lunghezza, int) or lunghezza <= 0:
            raise ExamException("Errore: la lunghezza deve essere un intero positivo!")
        self.lunghezza = lunghezza

    def compute(self, lista):
        
        if not isinstance(lista, list):
            raise ExamException(f"Errore: {lista} non e una lista")
        
        for x in lista:
            if not isinstance(x, (int, float)):
                raise ExamException(f"Errore: '{x}' non e un numero")
            
        if len(lista) < self.lunghezza:
            raise ExamException("La lista deve essere almeno lunga quanto la finestra")
        
        lista_returned = []

        for i in range(len(lista) - self.lunghezza + 1):
            finestra = lista[i:i+self.lunghezza]
            media = sum(finestra) / self.lunghezza
            lista_returned.append(media)

        return lista_returned

moving_average = MovingAverage(2)
result = moving_average.compute([2, 4, 8, 16])
print(result)