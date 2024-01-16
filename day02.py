letter = input('Input alphabet : ')
# vowels = {'a','e','i','o','u'}
vowels = "aeiou"
print(type(vowels))
if letter in vowels:
    print(f'{letter} is a vowel')
else :
    print(f'{letter} is a consonant')



