""""Faça uma função que retorne o reverso de um número inteiro
informado. Por exemplo: 127 -> 721.
def inverso(numero):
    return numero[::-1]
x = input('Digite um número:')
inverso(x)"""
def inverter(n):
    inverso = ''
    for i in range (len(n)):
        inverso += n[(len(n)-1)-i]
        print(inverso)
    print('O número invertido é ', inverso)
x = input('Digite um número:')
inverter(x)