#sum

def somma(my_list):
    sum = 0
    for i in my_list:
        sum += i
    return f"The sum is {sum}"

numbers = [1, 2, 3]

print(somma(numbers))