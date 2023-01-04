#Utilize o conceito de herança para criar a Classe Pokemon e as subclasses de tipo de Pokemon
# Utilize o conceito de polimorfismo para criar um método checarVantagem na Classe Pokemon
# e modifique esse método nas subclasses de acordo com as vantagens e desvantagens daquele tipo
class Pokemon:
    def __init__(self,level,nome,ataque, hp):
        self.level = level
        self.nome = nome        
        self.ataque = ataque
        self.hp = hp 
        print('Pokemon criado')
    def atacar(self):
        print('O pokemon atacou')
    def checarVantagem (self,pokemonInimigo):
        if(pokemonInimigo.tipo == "Fogo"):
            print(f"O pokemon {self.nome} perdeu para o pokemon tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Água"):
            print(f"O pokemon {self.nome} perdeu para o pokemon tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Elétrico"):
            print(f"O pokemon {self.nome} perdeu para o pokemon tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Grama"):
            print(f"O pokemon {self.nome} perdeu para o pokemon tipo {pokemonInimigo.tipo}")
        else: 
            print('Pokemon inválido')
class PokemonAquatico(Pokemon):
    def __init__(self, level,nome,ataque,hp):
        super().__init__(level)
        self.tipo = "Água"
        print('Pokemon do tipo aquatico criado')
    def atacar(self):
        print(f"O pokemon self.nome usou um jato d'água para atacar")
    def checarVantagem(self, pokemonInimigo):
        if(pokemonInimigo.tipo == "Fogo"):
            print(f"O pokemon {self._nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Água"):
            print(f"O pokemon {self._nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Elétrico"):
            print(f"O pokemon {self._nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Grama"):
            print(f"O pokemon {self._nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        else:
            print('Tipo de pokemon inválido')
class PokemonEletrico(Pokemon):
    def __init__(self, level,nome,ataque,hp):
        super().__init__(level)
        self.tipo = "Elétrico"
        print('Pokemon do tipo elétrico criado')
    def atacar(self):
        print(f"O pokemon self.nome usou choque para atacar")
    def checarVantagem(self, pokemonInimigo):
        if(pokemonInimigo.tipo == "Fogo"):
            print(f"O pokemon {self._nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Elétrico"):
            print(f"O pokemon {self._nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Elétrico"):
            print(f"O pokemon {self._nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Grama"):
            print(f"O pokemon {self._nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        else:
            print('Tipo de pokemon inválido')
class PokemonFogo(Pokemon):
    def __init__(self, level,nome,ataque,hp):
        super().__init__(level)
        self.tipo = "Fogo"
        print('Pokemon do tipo fogo criado')
    def atacar(self):
        print(f"O pokemon {self.nome} usou choque para atacar")
    def checarVantagem(self, pokemonInimigo):
        if(pokemonInimigo.tipo == "Fogo"):
            print(f"O pokemon {self._nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Elétrico"):
            print(f"O pokemon {self._nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Elétrico"):
            print(f"O pokemon {self._nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        elif(pokemonInimigo.tipo == "Grama"):
            print(f"O pokemon {self._nome} ganhou do pokemon de tipo {pokemonInimigo.tipo}")
        else:
            print('Tipo de pokemon inválido')
    
# if __name__ == "__main__":
#     pokemon1 = Pokemon(10)
#     pokemon2 = PokemonAquatico(15)
#     pokemon2.atacar()
