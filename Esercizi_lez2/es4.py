
def conta_lettera(l, p):
    count = 0

    for x in p:
        if x == l:
            count += 1
    return count

lettera = "a"
parola = "Sono informatica"

resulto = conta_lettera(lettera, parola)
print(resulto)
