
def palindromo(stringa):
    
    word = stringa.lower()
    n = len(word)

    for i in range(n//2):
        if word[i] != word[n-1-i]:
            return f"{stringa} non e un palindromo"

    return f"{stringa} e un palindromo"
                


stringa1 = "omo"
stringa2 = "franck"
stringa3 = "ekitike"

print(palindromo(stringa1))
print(palindromo(stringa2))
print(palindromo(stringa3))
