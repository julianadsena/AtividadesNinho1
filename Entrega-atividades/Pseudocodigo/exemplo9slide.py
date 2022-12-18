#algoritmo multiplos de 10
n = 1
lista = [] 
while n <= 100:
    n = n + 1
    if (n%10) == 0:        
        lista.append(n)        
print(lista)
