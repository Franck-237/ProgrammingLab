
def conteggio(file):

    dict_returned = {}
    count = 0

    with open(file, "r") as file:

        content = file.read()
        line = content.split()

        for i in line:
            if i in dict_returned:
                dict_returned[i] += 1
            else:
                dict_returned[i] = 1

    return dict_returned

file_path = "Esercizi_lez3/files/words.txt"

risult = conteggio(file_path)

print(risult)