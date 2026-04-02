

def occurence(file, world):
    count = 0

    with open(file, "r") as file:

        content = file.read()
        line = content.lower().split()
        print(line)

        for i in line:
            if i == world.lower():
                count += 1
            else:
                pass
    return count

file_path = "Esercizi_lez3/files/words.txt"

word = "I"

risult = occurence(file_path, word)

print(f"We have {risult} occurence(s)")

