def contavocali(parola):
    count=0
    for carattere in parola:
        if carattere in my_varvocali:
            count+=1
 
    return count
 
my_varvocali={'a','e','i','o','u'}
 
parola=input("Inserisci una parola: ")
print(contavocali(parola))