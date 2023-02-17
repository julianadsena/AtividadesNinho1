# ''Atividade para casa:
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
# Autores:
# Autor_id (PK)
# Autor_nome
# Conecte as duas tabelas usando a chave Livro_autor como chave estrangeira.]
# Dica: Se você já tiver criado a tabela Livros, use o comando ALTER
# '''
#Aplicar a estrutura Modelo, Visualização, Controle ao projeto Biblioteca das aulas 27-01 e 30-01
#Criar classe Livro, criar classe Conexão
#Replicar o código abaixo para atualizar Livros no seu banco de dados
import psycopg2
class Conexao:
    def __init__(self, parametroDb,parametroHost, parametroPort, parametroUser,parametroPassword):
        self._db = psycopg2.connect(database = parametroDb, host = parametroHost,port = parametroPort,user = parametroUser,password = parametroPassword)
    def consultarBanco(self,sql):
        cursor = self._db.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    def manipularBanco(self,sql):
        cursor = self._db.cursor()
        cursor.execute(sql)
        self._db.commit()
        cursor.close()