#Write a Python program to create the multiplication table (from 1 to 10) of a number.
n = int(input('Digite um número:'))
for i in range(1,11):
    mult = n * i
    print(f'{n} x {i} = {mult}')
