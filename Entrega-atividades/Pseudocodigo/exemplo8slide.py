#algoritmo maior numero
maior = 0
while True:    
    n = int(input('Digite um numero positivo maior que zero:'))
    if n > maior:
        maior = n
    elif n == 0:
        break 
print(f'O maior numero é {maior}')



