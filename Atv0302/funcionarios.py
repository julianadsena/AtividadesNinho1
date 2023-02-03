import psycopg2
# import psycopg2
# try:
#     con = psycopg2.connect(database="Empresa",user="postgres",password="cateq2023",host="localhost",port="5432")
#     cursor = con.cursor()
# except(Exception,psycopg2.Error) as error:
#     print("Ocorreu um erro:",error)
#TAREFA:
#CRIAR TABELA AUTOR DO LIVRO
def createTableFuncionarios(cur,conexao):
    cur.execute('''
        DROP TABLE IF EXISTS "Funcionarios";
        CREATE TABLE "Funcionarios"(
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "Nome" varchar(255) NOT NULL,
        "CPF" char(11),
        "Salario" money,
        "IDdep" int,
        CONSTRAINT fk_departamento
            FOREIGN KEY ("IDdep")
            REFERENCES "Departamentos"("IDdep")
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
        PRIMARY KEY ("ID")); ''')
    print("Tabela criada")
    conexao.commit()
    conexao.close()
def createTableDep(cur,conexao):
    cur.execute('''
        DROP TABLE IF EXISTS "Departamentos";
        CREATE TABLE "Departamentos"(
        "IDdep" int GENERATED ALWAYS AS IDENTITY,
        "Nome" varchar(255),
        PRIMARY KEY ("IDdep"));''')
    print("Tabela criada")
    conexao.commit()
    conexao.close()
def verFuncionario(cur,conexao): 
    id = int(input("Digite o id do funcionario que deseja visualizar"))   
    cur.execute(f'''
        SELECT * FROM "Funcionarios"
        WHERE "ID" = {id} ''')
    funcionarios = cur.fetchall()
    for funcionario in funcionarios:
        print("------------------------------------------")
        print(f"ID:{funcionario[0]},\nNOME:{funcionario[1]},\nCPF:{funcionario[2]},\nSALARIO:{funcionario[3]},\nID DEPARTAMENTO:{funcionario[4]}")
        print("------------------------------------------")
def verFuncionarioMelhor(cur,conexao):
    idFunc=input("Digite o id do funcionario:")

def verDepartamento(cur,conexao):
    verFuncionario(cur,conexao)
    dep = int(input("Digite o id do depart do funcionario:"))
    cur.execute(f'''
        SELECT * FROM "Departamentos"
        WHERE "IDdep" = {dep} 
        ''')
    print(cur.fetchall())
def inserirFuncionario(cur,conexao):
    novoNome = input("Inserir nome do funcionario:")
    novoCpf = input("Inserir o novo cpf do funcionario:")
    novoSalario = input("Inserir o salario do funcionario:")
    novoId = int(input("Numero do departamento:"))
    cur.execute(f'''
        INSERT INTO public."Funcionarios"("ID","Nome","CPF","Salario","IDdep")
        VALUES (default,'{novoNome}','{novoCpf}',{novoSalario},{novoId})''')
    conexao.commit()
def inserirDepartamento(cur,conexao):
    verDepartamento(cur,conexao)
    novoId = input("Inserir o id do departamento:")
    novoNome = input("Inserir o nome do departamento:")
    cur.execute(f'''
        INSERT INTO public."Departamentos"("IDdep","Nome")
        VALUES (default,'{novoNome}')''')
    conexao.commit()
con = psycopg2.connect(database="Empresa",user="postgres",password="cateq2023",host="localhost",port="5432")
cursor = con.cursor() #varre o banco de dados atraves do con
# inserirDepartamento(cursor,con)
# inserirFuncionario(cursor,con) 
verFuncionario(cursor,con)
verDepartamento(cursor,con)