"""Atividade
Crie uma banco de dados de uma Biblioteca que deverá conter 
a seguinte tabela:
Livros:
Livro_id
Livro_nome
Livro_paginas
Livro_anoLançamento
Livro_autor
- Especificar os tipos de cada atributo e criar função no python createTableLivros
- Usar o código abaixo para criar um CRUD, sistema de gerenciamento da tabela"""
import psycopg2
def createTableLivros(cur,conexao):
    cur.execute('''
        CREATE TABLE "Livros"(
        "ID" serial,
        "Nome" varchar(255),
        "Paginas" integer,
        "anoLancamento" integer,
        "Autor" varchar(255),
        "Edicao" integer,
        PRIMARY KEY ("ID"));
        ''')
    print("Tabela criada")
    conexao.commit()
    conexao.close()
# con = psycopg2.connect(database = "Livraria",user="postgres",password = "cateq2023",host="localhost",port="5433")
# cursor = con.cursor()
# createTableLivros(cursor,con)

def atualizarLivro(cur,conexao):
    listarLivros(cur,conexao)
    idLivro = int(input("Insira o id do livro que deseja modificar:"))
    cur.execute(f'''
        SELECT * FROM "Livros"
        WHERE "ID" = {idLivro}''')
    print("Livro escolhido:",cur.fetchone())
    while True:
        print("""O que você deseja alterar:
            1 - Alterar nome do livro
            2 - Alterar edição do livro
            3 - Alterar ano do Livro
            4 - Alterar número de páginas do livro
            5 - Alterar o autor do livro
            6 - Alterar todas as informações do livro
            0 - Sair do menu""")
        esc = input('Digite a opção escolhida:')
        match esc:
            case "1":
                novoNome = input("Digite o novo nome do livro")
                cur.execute(f'''
                UPDATE "Livros"
                SET "Nome" = '{novoNome}'
                WHERE "ID" = {idLivro}''')
                conexao.commit()
            case "2":
                novoEd = int(input("Digite o novo nome do livro"))
                cur.execute(f'''
                UPDATE "Livros"
                SET "Edicao" = {novoEd}
                WHERE "ID" = {idLivro}''')
                conexao.commit()
            case "3":
                novoAno = int(input("Digite o ano do livro:"))
                cur.execute(f'''
                UPDATE "Livros"
                SET "anoLancamento" = {novoAno}
                WHERE "ID" = {idLivro}''')
                conexao.commit()
            case "4":
                novoPag = int(input("Digite o numero paginas do livro:"))
                cur.execute(f'''
                UPDATE "Livros"
                SET "Paginas" = {novoPag}
                WHERE "ID" = {idLivro}''')
                conexao.commit()
            case "5":            
                novoAutor = input("Digite o ano do livro:")
                cur.execute(f'''
                UPDATE "Livros"
                SET "Autor" = '{novoAutor}'
                WHERE "ID" = {idLivro}''')
                conexao.commit()
            case "6":
                novoNome = input("Digite o novo nome do livro")
                novoEd = int(input("Digite o nova edição do livro"))
                novoAno = int(input("Digite o ano do livro:"))
                novoPag = int(input("Digite o numero paginas do livro:"))
                novoAutor = input("Digite o novo autor do livro:")
                cur.execute(f'''
                UPDATE "Livros"
                SET "Nome" = '{novoNome}',"Edicao" = {novoEd},"anoLancamento" = {novoAno},"Paginas" = {novoPag},"Autor" = '{novoAutor}'
                WHERE "ID" = {idLivro}''')
                conexao.commit()
            case "0":
                print("Você escolheu sair")
                break                
            case _:
                print("Você inseriu algum valor inválido")
            
        input("Tecle enter para prosseguir")
        cursor.close()
        con.close()
def inserirLivro(cur,conexao):
    novoNome = input("Insira o nome do livro:")
    novoPag = int(input("Insira o número da página de livros:"))
    novoAno = int(input("Insira o ano do livro:"))
    novoAutor = input("Insira o nome do autor do livro:")
    novoEdicao = int(input("Insira a edicao do livro:"))
    cur.execute(f'''
    INSERT INTO public."Livros"("ID", "Nome", "Paginas", "anoLancamento", "Autor", "Edicao")
    VALUES(default,'{novoNome}',{novoPag},{novoAno},'{novoAutor}',{novoEdicao})''')
    conexao.commit()

def listarLivros(cur,conexao):
    cur.execute('''
        SELECT * FROM "Livros"''')
    print(cur.fetchall())
    livros = cur.fetchall()
def removerLivro(cur,conexao):
    listarLivros(cur,conexao)
    idLivro = int(input("Digite o id do Livro:"))
    cur.execute(f'''
    DELETE FROM "Livros"
    WHERE "ID" = {idLivro}''')
    conexao.commit()
while True:
    try: 
        con = psycopg2.connect(database = "Livraria",user="postgres",password = "cateq2023",host="localhost",port="5433")
        cursor = con.cursor()
        print('Conectado')
        print('''
            1. Ver livros
            2. Inserir livro
            3. Modificar livro
            4. Remover Livro
            0. Sair do Programa''')
        opcaoMenu = input("Escolhe o que deseja fazer:")
        match opcaoMenu:
            case "1":
                listarLivros(cursor,con)
            case "2":
                inserirLivro(cursor,con)
            case "3":
                atualizarLivro(cursor,con)
            case "4":
                removerLivro(cursor,con)
            case "0":
                print("Você escolheu sair da aplicação. Até mais!")
                break
            case _:
                print("Você inseriu algum valor inválido")
        input("Tecle enter para prosseguir")
        cursor.close()
        con.close()
    except(Exception,psycopg2.Error) as error:
        print("Ocorreu um erro -",error)
