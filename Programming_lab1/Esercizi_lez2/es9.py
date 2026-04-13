def count_vowells(vowels, speaking):
    count = 0
    for i in vowels:
        for j in speaking:
            if i == j:
                count += 1
    return count

speak = input("Enter a speaking: ")
vowels = "aeiouAEIOU"

print(f"Total vowels {count_vowells(vowels, speak)}")