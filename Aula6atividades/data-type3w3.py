"""Write a Python program to multiplies all the items in a list"""
import math
list = []
for i in range(6):
    n = int(input('Digite um número:'))
    list.append(n)
resultado = math.prod(list)
print(resultado)