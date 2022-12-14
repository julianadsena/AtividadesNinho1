# Classe Funcionário: Implemente a classe Funcionário. Um funcionário tem um
# nome e um salário. Escreva um construtor com dois parâmetros (nome e salário) e
# o método aumentarSalario (porcentualDeAumento) que aumente o salário do
# funcionário em uma certa porcentagem. Exemplo de uso: harry = f u n c i o n á r i o
# ( " H a r r y " , 2 5 0 0 0 ) harry.aumentarSalario(10) Faca um programa que teste o
# método da classe. 
class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def porcentualDeAumento(self,aumentarSalario):
        porcentual = self.salario * (1+(aumentarSalario/100))
        return porcentual
x = input('Nome do funcionário:')
y = float(input('Salario do funcionario:'))
z = float(input('Porcentagem de aumento:'))
funcionario1 = Funcionario(x,y)
print(funcionario1.porcentualDeAumento(z))
