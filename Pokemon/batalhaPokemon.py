import random
from classeTreinador import *
from classePokemon import *
import time
import sys
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
def batalharPokemons(treinador1,treinador2):
    p1 = treinador1.escolherPokemon()
    p2 = treinador2.escolherPokemon()

    p1Valor = (p1.ataque+p1.defesa+p1.hp)*2.22
    p2Valor = (p2.ataque+p2.defesa+p2.hp)*2.22

    delay_print("---------Batalha de Pokemon---------")
    print(f"\n{p1.nome}")
    print(f"tipo/{p1.tipo}")
    print(f"ataque/{p1.ataque}")
    print(f"defesa/{p1.defesa}")
    print(f"avaliação/",{p1Valor})
    print("\nVS")
    print(f"\n{p2.nome}")
    print(f"tipo/{p2.tipo}")
    print(f"ataque/{p2.ataque}")
    print(f"defesa/{p2.defesa}")
    print(f"avaliação/",{p2Valor})

    time.sleep(2)
    while (p1Valor > 0) and (p2Valor > 0):
        if p1Valor > p2Valor:
            p1Valor =- p2Valor
            print(f'O vencedor da partida é {p1.nome}')
        elif p2Valor > p1Valor:
            p2Valor =- p1Valor
            print(f'O vencedor da partida é {p2.nome}')
        

        

pokemonDisponiveis = [
    Fogo('Charizard', 'Fogo', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'],12, 8,10),
    Aquatico('Blastoise', 'Aquatico', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],10, 10,8),
    Grama('Venusaur', 'Grama', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],8,12,13),
    Fogo('Charmander', 'Fogo', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],4, 2,6),
    Aquatico('Squirtle', 'Aquatico', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'], 3,3,4),
    Grama('Bulbasaur', 'Grama', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],2,4,8),
    Fogo('Charmeleon', 'Fogo', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],6,5,9),
    Aquatico('Wartortle', 'Aquatico', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],5,5,7),
    Grama('Ivysaur', 'Grama', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],4,6,8)]

delay_print("Bem vindo a Batalha de Pokemons!")
nomeJogador = input("\nDigite seu nome para iniciar: ")

delay_print("Escolha seu Pokemon inicial: ")

for i in range(len(pokemonDisponiveis)-2):
    print(f"{i+1}. {pokemonDisponiveis[i].nome}")

pokemonInicial = pokemonDisponiveis[int(input("Digite o pokemon escolhido: "))-1]
print(f"O pokemon escolhido foi o {pokemonInicial.nome}")

jogador = Jogador(nomeJogador,[pokemonInicial])
inimigo = Inimigo("Adv1",pokemonDisponiveis)
inimigo2 = Inimigo("Adv2",pokemonDisponiveis)
inimigo3 = Inimigo("Adv3",pokemonDisponiveis)
Inimigos =[inimigo,inimigo2,inimigo3]
while True:
    print("""
    Escolha umas das opções:
    1. Ver seus Pokemons
    2. Capturar um novo Pokemon
    3.Batalhar contra um oponente
    0. Sair do Jogo
    """)

    menu = input("Digite a opção escolhida: ")

    if menu == "0":
        print("Você saiu do jogo.")
        break
    elif menu == "1":
        jogador.listaPokemons()

    elif menu == "2":
        print("Escolha um pokemon para capturar: ")

        for i in range(len(pokemonDisponiveis)):
            print(f"{i+1}. {pokemonDisponiveis[i].nome}")

        capturado = pokemonDisponiveis[int(input("Digite o pokemon escolhido: "))-1]
        jogador.capturarPokemon(capturado)
    elif menu == "3":
        batalharPokemons(jogador,random.choice(Inimigos))

    else:
        print("Você digitou algo inválido,tente novamente.")


