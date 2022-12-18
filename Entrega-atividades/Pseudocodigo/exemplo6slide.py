#algoritmo media e comparacao
notas = []
soma = 0
maior = []
for i in range(5):
    n = float(input('Digite uma nota:'))
    notas.append(n)
    soma += n 
media = soma/len(notas)
for i in notas:
    if i >= media:
        maior.append(i)
print(f'Os valores maiores que as medias são {maior}')
print(f'A soma das notas é {soma}')
print(f'A média das notas é {media}')



