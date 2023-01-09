import random
from typing import Self #biblioteca aleatoriedade  
class Pokemon: #Requisito 1 -modelar a classe do pokemon
    def __init__(self,nome,especie,tipo,ataque,defesa,hp):
        self._nome = nome
        self._tipo = tipo
        self._especie = especie
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp
        self._movimento = "Ataque rápido"
#Requisito 2 - criar 3 subclasses de pokemon com base em seu tipo
class Aquatico(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "aquatico"
        self._movimento = "jato d'água"
class Fogo(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "fogo"
        self._movimento = "Lança chamas"
class Grama(Pokemon):
    def __init__(self, nome, especie, tipo, ataque, defesa, hp):
        super().__init__(nome, especie, tipo, ataque, defesa, hp)
        self._tipo = "grama"
        self._movimento = "Chicote de cipó"
#Requisito 3 - Modelar classe treinador
class Treinador:
    def __init__(self, nome, pokemons):
        self._nome = nome
        self._pokemons = pokemons 
    def escolherPokemon(self):
        return random.choice(self._pokemons)                    
#Requisito 4 - Modelar subclasses do treinador (Jogador e Inimigo)
class Jogador(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)
    def escolherPokemon (self):
        while True:
            print(f"Escolha seu pokemon:")
            for i in range (len(self._pokemons)):
                print(f"{i+1}.{self._pokemons[i]._nome}")
            pokemonEscolhido = input("Digite o número do pokemon escolhido:")
            return self._pokemons[int(pokemonEscolhido)-1]
    def capturarPokemon(self, pokemonCapturado):
        self._pokemons.append(pokemonCapturado)
        print(f"Você capturou o {pokemonCapturado._nome}")
    def listarPokemons(self):
        print("Sua lista de pokemons:")
        for i in range(len(self._pokemons)):
            print(f"{i+1}.{self._pokemons[i]._nome}")
               
class Inimigo(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)
        
#Requisito 5 - Criar método de batalha onde dois pokemons, lutam e é determinado o vencedor.
def batalhaPokemon(treinador1,treinador2):
    p1 = treinador1.escolherPokemon()
    p2 = treinador2.escolherPokemon()
    p1Forca = (p1._ataque + p1._defesa + p1._hp)*random.randint(1,3)
    p2Forca = (p2._ataque + p2._defesa + p2._hp)*random.randint(1,3)
    print(f"{p1._nome} atacou com {p1._movimento} e força {p1Forca}")
    print(f"{p2._nome} atacou com {p2._movimento} e força {p2Forca}")    
    if (p1Forca > p2Forca):
        print(f"O vencedor foi {p1._nome} com força {p1Forca} do treinador {p1}")
    elif (p1Forca < p2Forca):
        print(f"O vencedor foi {p2._nome} com força {p2Forca} do treinador {p2}")
    else:
        print("Deu empate")
    
pokemon1 = Fogo("Betinho","Charmander","Fogo",50,50,50)
pokemon2 = Grama("Verdinho","Bulbassauro","Grama",50,50,50)
pokemon3 = Aquatico("Tortuguita","Squirtle","Aquatico",300,50,50)
x  = Jogador('Fulano',[pokemon1,pokemon2,pokemon3])
y = Inimigo('Ciclano',[pokemon1,pokemon2,pokemon3])
batalhaPokemon(x,y)
Jogador.listarPokemons()
Jogador.capturarPokemon(pokemonsDisponiveis[3])

