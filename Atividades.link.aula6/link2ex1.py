#Write a Python program to find those numbers 
# which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
n=1500
lista = []
while n<=2700:
    n = n + 1
    if ((n%7)==0) and ((n%5)==0):
        lista.append(n)
print(lista)
