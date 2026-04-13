
def rest_dic(my_list):

    count = 0
    dictionnary = {}

    for i in my_list:
        dictionnary[i] = i
        count += 1
    
    return f"The new dictionnary is {dictionnary} with {count} occurence(s)"

my_list = [1, 2, 3, 4, 5]

print(rest_dic(my_list))