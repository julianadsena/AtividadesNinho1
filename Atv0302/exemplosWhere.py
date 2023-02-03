if __name__ == "__main__": #boa pratica - só é acessível se tiver com esse arquivo aberto 
    import psycopg2
    from Controle.classConexao import Conexao
    try:
        con = Conexao("Empresa","localhost","5432","postgres","cateq2023")

        #Consulta básica
        funcionarios = con.consultarBanco('''
            SELECT * FROM "Funcionarios"
            ORDER BY "ID" ASC''')
        for funcionario in funcionarios:
            print(f"\n{funcionario[0]} - {funcionario[1]} - {funcionario[2]} - {funcionario[3]} - {funcionario[4]} ")
        #consulta operador =, usando o ID
        funcionario = con.consultarBanco('''
        SELECT * FROM "Funcionarios"
        WHERE "ID" = 2''')
        print(funcionario)
        nomePesquisa = input("Digite o nome do funcionario:")
        funcionario = con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" = '{nomePesquisa}'
        ''')
        print(funcionario)
        #consultar operador > usando o salario
        print("Pesquisa por salario:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salario" != '15000'
        ORDER BY "ID"'''))
        #consultar operador < usando o salario
        print("Pesquisa por salario:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salario" < '3000'
        ORDER BY "ID"'''))
        #consultar operador >= usando o salario
        print("Pesquisa por salario:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salario" >= '3000'
        ORDER BY "ID"'''))
        #consultar operador <= usando o salario
        print("Pesquisa por salario:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salario" <= '3000'
        ORDER BY "ID"'''))
        #consultar operador between 
        print("Pesquisar por salario entre valor:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salario" BETWEEN '2000' AND '5000'
        '''))
        #consultar operador in 
        print("Pesquisa por nome",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" IN ('Marcos','fulano')'''))
        #consultar operador like 
        busca = input('Digite o que deseja buscar:')
        print("Pesquisa por nome", con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" LIKE '%{busca[0] + busca[1] + busca[2]}%'
        ''')) #não liga para o case
        #consultar operador not like
        print("Pesquisa por nome:",con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" NOT LIKE ('Marco')
        '''))


    except(Exception,psycopg2.Error) as error:
        print("Ocorreu um erro",error)
