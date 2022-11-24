"""Write a Python program to get the smallest number from a list"""
list = []
for i in range(6):
    x = int(input('Digite um número:'))
    list.append(x)
print(min(list))