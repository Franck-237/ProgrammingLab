
def remove(file1, file2):
    count = 0

    with open(file1, "r") as file:
        content = file.read()
        line = content.split()

        unique_words = set(line)

    with open(file2, "w") as file:
        file.write("\n".join(unique_words))

file_path = "Esercizi_lez3/files/words.txt"
new_file = "Esercizi_lez3/files/unique.txt"

risult = remove(file_path, new_file)

print(risult)