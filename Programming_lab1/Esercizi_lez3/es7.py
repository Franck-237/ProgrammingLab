
import csv

file_path = "Esercizi_lez3/files/shampoo_sales.csv"

def summ(file):
    sum = 0

    with open(file, "r") as file:
        content = csv.reader(file)

        next(content)
        for line in content:
            vendita = float(line[1])
            sum += vendita
    
    return sum

risult = summ(file_path)
    
print(f"The totale is: {risult:.2f}")
