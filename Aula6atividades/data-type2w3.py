"""Write a Python program to sum all the items in a list."""
list = []
for i in range(6):
    n = int(input('Digite um número:'))
    list.append(n)
print(sum(list))