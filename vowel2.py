vowel = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
found = []
for letter in word:
    if letter in vowel:
        if letter not in found:
            found.append(letter)
for letter in found:
    print(letter)
