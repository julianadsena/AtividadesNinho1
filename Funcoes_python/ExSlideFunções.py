"""Escreva uma função que, dado o valor da conta de um 
restaurante, calcule e exiba a gorjeta do garçom, 
considerando 10% do valor da conta."""
def g_garcom(valor_conta):    
    print('O valor da gorjeta é:',valor_conta*0.1)
repetir = True
while (repetir == True):
    repetir= False
    valorConta=input('O valor da conta é:')
    if(valorConta.isnumeric()):
        valorConta=float(valorConta)
        g_garcom(valorConta)
    else:
        repetir = True
        print('O usuário não digitou um número!')
