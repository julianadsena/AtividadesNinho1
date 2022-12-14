# Crie uma classe chamada Pokemon. Tente imaginar os
# atributos que um objeto dessa classe teria.
# Faça um programa que instância um objeto da classe
# Pokemon e imprima os atributos desse objeto.
# Bônus: Crie 2 objetos Pokemon e tente criar uma função
# de batalha que recebe os 2 objetos e determine quem sai
# ganhando.
class pokemon:
    def __init__(self,nome,pontos,ataque,defesa):
        self.nome = nome
        self.pontos = pontos
        self.ataque = ataque
        self.defesa = defesa
if __name__ =="__main__":
    pokemon1 = pokemon("jigglypuff","60","45",'20')
    print(pokemon1.nome,pokemon1.pontos,pokemon1.ataque,pokemon1.defesa)    
    pokemon2 = pokemon("pikachu","60","50",'40')    
    print(pokemon2.nome,pokemon2.pontos,pokemon2.ataque,pokemon2.defesa)

    
        