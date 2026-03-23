
def number_letter(letter1, speaking):
    count = 0
    for i in speaking:
        if i == letter1:
            count += 1
    return count

letter2 = "a"
speak = input("Enter a speaking: ")
number = number_letter(letter2, speak)
print(number)