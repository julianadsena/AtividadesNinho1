import psycopg2 #para instalar > pip install psycopg2
def createTableFuncionario(cur,conexao):
    cur.execute('''
    CREATE TABLE "Funcionarios"(
        "ID" serial,
        "Nome" varchar(255),
        "CPF" char(11) UNIQUE NOT NULL,
        "Salario" money DEFAULT 0.00,
        PRIMARY KEY ("ID")

    );
    ''')
    conexao.commit()
def listarFuncionario(cur,conexao):
    cur.execute('''
    SELECT * FROM "Funcionarios"''')
    print(cur.fetchall())

def removerFuncionario (cur,conexao):
    idFunc = int(input('Digite o id do funcionario que deseja remover:'))
    cur.execute(f'''
    DELETE FROM "Funcionarios"
    WHERE "ID" = {idFunc}''')

def inserirFuncionario(cur,conexao):
    novoNome = input("Insira o novo nome do funcionario:")
    while True:
        novoCpf = input("Insira o novo cpf:")
        if len(novoCpf) != 11:
            print("Tamanho inválido, o cpf precisa conter 11 digitos")
        else:
            break
    novoSal = float(input("Insira o novo salario:"))
    cur.execute(f'''
        INSERT INTO "Funcionarios"
        VALUES(default,'{novoNome}','{novoCpf}',{novoSal})
        ''')
    conexao.commit()
def atualizarFuncionario(cur,conexao):
    listarFuncionario(cur,conexao)  

    idFunc = int(input('Digite o id do funcionario que deseja modificar:'))
    novoNome = input('Digite o novo nome do funcionario:')
    novoCpf = input('Digite o novo CPF:')
    novoSal = float(input('Digite o novo salario:'))
    cur.execute(f'''
        UPDATE "Funcionarios"
        SET "Nome" = '{novoNome}', "CPF" = '{novoCpf}', "Salario" = {novoSal}       
        WHERE "ID" = {idFunc}''')
    conexao.commit()
while True:    
    try:
        con = psycopg2.connect(database="Empresa",user="postgres",password="cateq2023",host="localhost",port="5432")
        cursor = con.cursor()
        print('Conectado')
        print('''
        1. Ver funcionarios
        2. Inserir funcionario
        3. Modificar funcionario
        4. Remover funcionario
        0. Sair do Programa''')
        opcaoMenu = input ("Escolha o que deseja fazer:")
        match opcaoMenu:
            case "1":
                listarFuncionario(cursor,con)
            case "2":
                inserirFuncionario(cursor,con)
            case "3":
                atualizarFuncionario(cursor,con)
            case "4":
                removerFuncionario(cursor,con)
            case "0":
                print("Você escolheu sair da aplicação. Até mais!")
                break
            case _:
                print("Você inseriu algum valor inválido")
        input("Tecle Enter para prosseguir")
        con.close()
    except(Exception,psycopg2.Error) as error:
        print("Ocorreu um erro!",error)



