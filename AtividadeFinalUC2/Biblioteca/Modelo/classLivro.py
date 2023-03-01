# Crie uma banco de dados de uma Biblioteca que deverá conter a seguinte tabela:
# Livros:
# Livro_id
# Livro_nome
# Livro_paginas
# Livro_anoLançamento
# Livro_autor
# - Especificar os tipos de cada atributo e criar função no python createTableLivros
# - Usar o código abaixo para criar um CRUD, sistema de gerenciamento da tabela
# CRUD significa Create, Read, Update, Delete e se refere as operações básicas que podemos realizar
# com os campos de um tabela de um banco de dados.
# Create - Inserir um novo campo. Exemplo: Inserir um novo funcionário na tabela Funcionários
# Read - Relacionado ao comando Select, é o ato de ler e imprimir todos os campos ou campos específicos de uma tabela
# Update - Atualizar um campo da tabela
# Delete - Remover uma entrada da tabela. Ex: Remover um funcionário
class Livros:
    def __init__(self,id,nome,paginas,anoLancamento,autor,edicao):
        self.id = id
        self.nome = nome
        self.paginas = paginas
        self.anoLancamento = anoLancamento
        self.autor = autor
        self.edicao = edicao
    def imprimirLivros (self):
        print(f'''
        Informações do Livro:
        ID - {self.id}
        Nome - {self.nome}
        Paginas - {self.paginas}
        Ano Lancamento - {self.anoLancamento}
        Autor - {self.autor}''')
    def inserirLivros(self):
        sql = print(f'''
        INSERT INTO "Livros"
        VALUES(default,'{self.nome}','{self.paginas}','{self.anoLancamento}','{self.autor}','{self.edicao}')''')
        return sql
    def atualizarLivros(self):
        sql = print(f'''
        UPDATE "Livros"
        SET "Nome" = '{self.nome}', "Paginas" = {self.paginas}, "Ano Lancamento" = {self.anoLancamento},"Autor" = {self.autor} 
        Where "ID" = '{self.id}' ''')
        return sql
    def consultarAlugueis(self):
        sql = print(f'''
        SELECT * FROM "Aluguel"
        WHERE "ID_Livro" = '{self._id}'
        ''')
        return sql 