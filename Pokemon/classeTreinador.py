import random 
class Treinador:
    def __init__(self,nome,pokemons):
        self._nome = nome
        self._pokemons = pokemons
    def escolherPokemon(self):
        return random.choice(self._pokemons)
class Jogador(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)
    def escolherPokemon(self):
        while True:
            print(f"Escolha seu pokemon:")
            for i in range(len(self._pokemons)):
                print(f"{i+1}.{self._pokemons[i].nome}")
            pokemonEscolhido = input("Digite o número do pokemon escolhido:")
            return self._pokemons[int(pokemonEscolhido)-1]
    def capturarPokemon(self,pokemonCapturado):
        self._pokemons.append(pokemonCapturado)
        print(f"Você capturou o {pokemonCapturado.nome}")
    def listaPokemons(self):
        print("Aqui está sua lista de pokemons:")
        for i in range(len(self._pokemons)):
            print(f"{i+1}.{self._pokemons[i].nome}")
class Inimigo(Treinador):
    def __init__(self, nome, pokemons):
        super().__init__(nome, pokemons)