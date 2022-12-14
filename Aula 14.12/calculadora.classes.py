class Calculadora:
    def __init__(self):
        self.valor = ""
    def calcular(self,numero2,operador):
        try:    
            if(operador == "+"):
                print(self.somar(numero2))
            elif(operador == "-"):
                print(self.subtrair(numero2))
            elif(operador == "/"):
                print(self.dividir(numero2))
            elif(operador == "*"):
                print(self.multiplicar(numero2))
            else:
                print('O usuário digitou um número inválido, tente novamente')
        except ValueError:
            print('Você digitou um valor invalido!')
            return "ERROR"        
    def somar(self, numero2):
        resultado = self.valor + numero2
        self.valor = resultado
        return resultado
    def subtrair(self,numero2):
        resultado = self.valor - numero2
        self.valor = resultado
        return resultado
    def dividir(self,numero2):
        if (numero2 != 0):
            resultado = self.valor / numero2
            self.valor = resultado
        else:
            print('Você tentou dividir por 0, tente novamente')

        return resultado
    def multiplicar(self,numero2):
        resultado = self.valor * numero2
        self.valor = resultado
        return resultado
    
calculadora = Calculadora()
while(True):
    if(calculadora.valor == ""):
        calculadora.valor=int(input("Insira o numero 1:"))
    operador = input("Insira o operador:")
    n2 = int(input('Insira o número 2:'))
    calculadora.calcular(n2,operador)


    