"""Escreva um programa que recebe um número inteiro e usa uma função para determinar se é um número inteiro ou 
não se o texto inserido não for um número inteiro peça para o usuario digitar novamente"""
"""dica: isnumeric() repetir=true while (repetir) terá varivel global"""
def var(num):
    if num.isnumeric():        
        print('É um número inteiro')
        global repetir
        repetir = False
    else:        
        print('Não é um numero inteiro')        
repetir = True
while repetir:
    x = input('Digite um número:')
    var(x)
    


