"""calculadora"""
def soma(numero1,numero2):
    return float(numero1)+float(numero2)
def sub(numero1,numero2):
    return float(numero1)-float(numero2)
def mult(numero1,numero2):
    return float(numero1)*float(numero2)
def div(numero1,numero2):
    return float(numero1)/float(numero2)
def calculadora(n1,n2,op):   
    if (op == '+'):
        print(soma(n1,n2))
    elif (op == '-'):
        print(sub(n1,n2))
    elif (op == '*'):
        print(mult(n1,n2))
    elif (op == '/'):
        if n2 == '0':
            return 'O número 2 não pode ser 0'
        else:
            return div(n1,n2)
    else:
        print('Digite um operador inválido')
        global repetir
        repetir == False
repetir = True
while repetir == True:        
    num1 = input('Escreva o número 1: ')
    num2 = input('Escreva o número 2: ')
    operador = input('Escreva o op (+,-,/,*):')
    if num1.isnumeric() and num2.isnumeric():
        repetir == False
        print(calculadora(num1,num2,operador))
    else:
        repetir == True
        print('Você digitou um número inválido')
        