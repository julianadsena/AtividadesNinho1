#Aula 06-02
#Conteúdo: Revisão Geral de Implementação de Banco de Dados com Python
#Programa: Sistema de Gerenciamento de Biblioteca
#Objetivos:
#   - Criar modelo físico de dados
#   - Entidades: Livros e Clientes Relacionamentos: Aluguel
#   - Criar banco de dados e tabelas
#   - Integrar banco com Python e criar funções de manipulação das tabelas
#   - Ver Clientes, Livros e Alugueis
#   - Inserir Clientes
#   - Registrar Aluguel
import psycopg2
from Modelo.classCliente import Cliente 
from Controle.ClassConexao import Conexao
from Modelo.classCliente import Lic
def criarBancoDados(conexao):
    conexao.manipularBanco('''
    DROP DATABASE IF EXISTS "Biblioteca";
    CREATE DATABASE "Biblioteca";
    ''')
def criarTabelaCliente(conexao):
    conexao.manipularBanco('''
    DROP TABLE IF EXISTS "Cliente";
    CREATE TABLE "Cliente"(
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "Nome" varchar(255) NOT NULL,
        "Autor" varchar(255) NOT NULL, 
        Primary Key("ID")
    );
    ''')
def criarTabelaAluguel(conexao):
    conexao.manipularBanco('''
    DROP TABLE IF EXISTS "Aluguel";
    CREATE TABLE "Aluguel"(
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "ID_Cliente" int NOT NULL, 
        "ID_Livro" int NOT NULL,
        "Data_Aluguel" timestamp default current_timestamp,
        PRIMARY KEY ("ID"),
        CONSTRAINT fk_cliente
            Foreign Key ("ID_Cliente")
            Reference "Cliente"("ID")
            ON DELETE CASCADE 
            ON UPDATE NO ACTION
            ,
        CONSTRAINT fk_livro
            Foreign Key ("ID_Livro")
            References "Livro"("ID")
            ON DELETE SET NULL
            ON UPDATE NO ACTION
    );
    ''')
def menuClientes(conexao):
    print("Lista de clientes:")
    resultado = conexao.consultarBanco('''
    SELECT * FROM "Cliente"
    ORDER BY "ID" ASC''')
    print("ID | NOMES")
    for cliente in resultado:
        print(f"{cliente[0]} | {cliente[1]} ")
    print(f'''
    Escolha uma das opcoes:
    1. Ver cliente específico 
    2. Inserir novo cliente
    0. Voltar para o menu principal''')
    opcoes = input("Digite o número da opcao desejada:")
    match opcoes:
        case "1":
            while True:
                clienteID = input("Digite o ID do cliente:")
                clienteEscolhido = Cliente(clienteID, None, None)
                resultado = conexao.consultarBanco(clienteEscolhido.consultarClienteporID())
                if resultado != []:
                    clienteEscolhido._nome = resultado [0][1]
                    clienteEscolhido._cpf = resultado[0][2]
                    clienteEscolhido.imprimirCliente()
                    while True:
                        print(f'''
                        Escolha uma das opcoes:
                        1. Ver alugueis
                        0. Voltar para o menu principal''')
                        opcoes = input("Digite o numero da opcao:")
                        match opcoes:
                            case "1":
                                print(f"Alugueis do cliente {clienteEscolhido._nome}")
                                resultado = conexao.consultarBanco(clienteEscolhido.consultarAlugueis())
                                if resultado != []:
                                    print("ID| Livro | Data")
                                    for aluguel in resultado:
                                        print(f"{aluguel[0] | {aluguel[3]}}")
                                else: 
                                    print("Esse usuario não possui alugueis")
                                input("Tecle ENTER para continuar")
                            case "0":
                                print("Saindo do menu cliente")
                                break
                            case _:
                                print("Você escolheu uma opcao invalida")
                        break
                    else: 
                        print("Voce escolheu um ID invalido")
        case  "2":
            novoCliente = Cliente(None,None,None)
            novoCliente._nome = input("Digite o nome do cliente:")
            novoCliente._cpf = input("Digite o cpf do cliente:")
            conexao.manipularBanco(novoCliente.inserirCliente())
            print("Novo cliente inserido")
def menuLivros(conexao):
    print("Lista de Livros:")
    resultado = conexao.consultarBanco ('''
    SELECT * FROM "Livro"
    ORDER BY "ID" ASC''')
    print("ID | NOME")
    for livro in resultado:
        print(f'''{livro[0]} | {livro[1]}''')
    print(f'''
    Escolha uma das opcoes 
    1 Ver livro especifico
    2 Inserir novo livro
    0 Voltar para o menu principal
    ''')
    opcoes = input("Digite o numero da opcao desejada:")
    match opcoes:
        case "1":
            while True:
                livroID = input("Digite o ID do livro:")
                livroEscolhido = Livro(livroID, None, None)
                resultado = conexao.consultarBanco(livroEscolhido.consultarLivroPorID())
                if resultado != []:
                    livroEscolhido._nome = resultado[0][1]
                    livroEscolhido._autor = resultado [0][2]
                    livroEscolhido.imprimirLivro()
                    while True:
                        print(f'''
                        Escolha uma das opcoes
                        1. ver alugueis
                        0. voltar para o mennu principal''')
                        opcoes = input("Digite o numero da opcao:")
while True:
    try:
        login = "postgres"
        password = "cateq2023"
        con=Conexao("Biblioteca","localhost","5432",login,password)
        break
    except (Exception,psycopg2.Error) as error:
        print("Ocorreu um erro - ", error)
while True:
    try:
        print("Bem vindo a biblioteca 'Biblioteca dos Livros'")
        print(f'''
        Escolha uma das opcoes:
        1. Ver clientes
        2. Ver livros
        3. Ver alugueis
        0. sair''')
        opcoes = input("Digit o numero da opcao do menu:")
        match opcoes:
            case "1":
                menuClientes(con)
            case "2":
                print("Vendo livros:")
            case "3":
                print("Vendo alugueis")
            case "0":
                print("Saindo da aplicacao...")
                break
            case _: 
                print("Voce digitou uma opcao invalida")
        input("Pressione qualquer tecla para continuar")
        con.fechar()
    except(Exception.psycopg2.Error) as error:
        print("Ocorreu um erro - ", error)

    