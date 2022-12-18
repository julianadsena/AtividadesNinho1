#algoritmo peso ideal
s = input('Digite o seu gênero F ou M:')
a = input('Digite a sua altura:')
if s == 'F' or s == 'f':
    p = (62.1 * float(a)) - 44.7
    print(f'Seu peso ideal é {p}')
elif s == 'M' or s == 'm':
    p = (72.7 * float(a)) - 58
    print(f'Seu peso ideal é {p}')
else:
    print('Digite um gênero válido')


