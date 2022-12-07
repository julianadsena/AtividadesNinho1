#Escreva um codigo de ate 4 digitos e determine quantas unidades,dezenas,centenas e milhares o numero tem
####SOLUCAO 1####
# numero = input('Digite um numero:')
# if numero.isnumeric():
#     if len(numero) <= 4:
#         numero = int(numero)
#         m = numero//1000
#         c = (numero - (1000*m))//100
#         d = (numero - (100*c) - (1000*m))//10
#         u = (numero - (10*d) - (100*c) - (1000*m))
# print(f"""
#         Milhares: {m}
#         Centenas: {c}
#         Dezenas:{d}
#         Unidades:{u}
#         """)
####SOLUCAO 2####
# unidades =('unidade','centena','dezena','milhar')
# numeroInvertido = []
# while (True):
#     numero = input('Digite um número de até 4 digitos:')
#     if (numero.isnumeric()):
#         if(len(numero)<=4):
#             for i in range(len(numero)):
#                 numeroInvertido.append(numero[i])
#             for x in range(len(numeroInvertido)):
#                 print(f"{unidades[x]} = {numeroInvertido[x]}")
                
#         else:
#             print('Você deve escrever um número de até 4 digitos')
#     else:
#         print('Você digitou um caractere que não é um número')

numero = int(input('Insira um número:'))
resposta = numero
m = 0
c = 0
d = 0
u = 0
while (resposta != 0):
    if (resposta>=1000):
        resposta -= 1000
        m += 1
    elif (resposta>=100):
        resposta -= 100
        c += 1
    elif (resposta>=10):
        resposta -= 10
        d +=1
    elif (resposta>=1):
        resposta -= 1
        u +=1
    else: break
print(f'A quantidade de milhares é: {m}')
print(f'A quantidade de centenas é: {c}')
print(f'A quantidade de dezenas é: {d}')
print(f'A quantidade de unidades é: {u}')










