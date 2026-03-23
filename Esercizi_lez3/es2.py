
def palindrome(speaking):
    word = speaking.lower()

    n = len(word)
    for i in range(n // 2):
        if word[i] != word[n - 1 - i]:
            return f"{speaking} isn't a palindrome"
    
    return f"{speaking} is a palindrome"

speak = input("Enter a word: ")

print(palindrome(speak))