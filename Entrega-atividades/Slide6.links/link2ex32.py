#Write a Python program to check whether an alphabet is a vowel or consonant.
letra = input('Digite uma letra:')
if letra in ('a','e','i','o','u'):
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} é uma consonante')