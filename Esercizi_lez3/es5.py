
def assign(my_list):

    list_letters = ["zero", "uno", "due", "tre", "quatro", "cinque", "sei", "sette", "otto", "nove"]
    list_returned = []

    for i in my_list:
        letter = list_letters[i]
        list_returned.append(letter)

    return list_returned

        
my_list = [1, 0, 7, 9, 8]

print(assign(my_list))
