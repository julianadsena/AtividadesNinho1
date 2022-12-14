# Classe Triangulo: Crie uma classe que modele um triangulo:
# – Atributos: LadoA, LadoB, LadoC
# – Métodos: calcular Perímetro, getMaiorLado;
# Crie um programa que uFlize esta classe. Ele deve pedir ao usuário que informe as
# medidas de um triangulo. Depois, deve criar um objeto com as medidas e imprimir
# sua área e maior lado. 

class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC        
    def per(self):
        perimetro = float(self.ladoA) + float(self.ladoB) + float(self.ladoC)
        return perimetro
    def Lado(self):
        if (self.ladoA > self.ladoB) and (self.ladoA >self.ladoC):
            Lado = self.ladoA
            return Lado
        elif (self.ladoB > self.ladoA) and (self.ladoB >self.ladoC):
            Lado = self.ladoB
            return Lado
        elif (self.ladoC > self.ladoA) and (self.ladoC >self.ladoB):
            Lado = self.ladoC
            return Lado
x = input('Insira o lado A:')
y = input('Insira o lado B:')
z = input('Insira o lado C:')
triangulo1 = Triangulo(x,y,z)
print(triangulo1.per())
print(triangulo1.Lado())


        
