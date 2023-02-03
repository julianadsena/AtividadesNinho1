from Controle.classConexao import Conexao
from Modelo.classFuncionario import Funcionario
import psycopg2
def mostrarFuncionario(conexao):
    listaFuncionarios = conexao.consultarBanco('''
    SELECT * FROM "Funcionarios"
    ORDER BY "ID" ASC''')
    print ("ID | Nome")
    for func in listaFuncionarios:
        print(f"{func} - {func[1]} \n")
def inserirFuncionario(conexao):
    funcionario = Funcionario(None,None,None,None,None)
    funcionario.nome = input("Digite o nome do funcionario:")
    while(funcionario.setcpf(input("Digite o cpf do funcionario:")) == True):
        print("Tente novamente")
    funcionario.salario = input("Digite o salario do funcionario:")
    funcionario.idDep = input("Digite o id do departamento:")
    print("Funcionario válido")
    conexao.manipularBanco(funcionario.inserirFuncionario("Funcionarios"))
def menuAlterarFuncionario(conexao):
    print('''
    Escolha o que deseja fazer:
    1. Atualizar Funcionario
    2. Remover Funcionario''')
    opcoes = input('Digite o nro da opcao escolhida:')
    match opcoes:
        case "1":
            funcionarioEscolhido = input("Digite o id do funcionario que deseja atualizar:")
            funcionarioConsulta = conexao.consultaBanco(f'''
            SELECT * FROM "Funcionarios"
            WHERE "ID" == {funcionarioEscolhido}''')
            funcionario = Funcionario(funcionarioEscolhido[0],funcionarioEscolhido[1],funcionarioEscolhido[2],funcionarioEscolhido[3])
            opcoes = input("Você deseja alterar informações básicas(1) ou o Departamento(2):")
            match opcoes:
                case "1":
                    novoNome = input ("Digite o novo nome do funcionario")
                    novoCpf = 
        case "2":
            funcionarioEscolhido
            conexao.manipularBanco(f'''
            DELETE FROM "Funcionarios"
            WHERE "ID" = '{funcionarioEscolhido}
            ''')
def pesquisarFuncionario(conexao):
    print('''
    Menu de pesquisa:
    1. Nome
    2. Primeiro nome
    3. Salario
    4. Salario maior escolhido''')
    opcoes = input ('Digite a opçao escolhida:')
    match opcoes:
        case "1":
            nomeEscolhido = input("Digite o noem que deseja pesquisar:")
            print(conexao.consultarBanco(f'''
            SELECT * FROM "Funcionarios"
            WHERE "Nome" = {nomeEscolhido}'''))
        case "2":
            nomeEscolhido = input("Digite o noem que deseja pesquisar:")
            print(conexao.consultarBanco(f'''
            SELECT * FROM "Funcionarios"
            WHERE "Nome" LIKE '{nomeEscolhido}%'
            '''))
        case "3":
            salarioEscolhido = input("Digite o salario que deseja pesquisar:")
            print(conexao.consultarBanco(f'''
            SELECT * FROM "Funcionarios"
            WHERE "Salario" = {salarioEscolhido}
            '''))
        case "4":
            salarioEscolhido = input("Digite o noem que deseja pesquisar:")
            print(conexao.consultarBanco(f'''
            SELECT * FROM "Funcionarios"
            WHERE "Salario" > {salarioEscolhido}
            '''))
               
try:
    con = Conexao("Empresa","localhost","5432","postgres","cateq2023")
    print('''
    BEM VINDO EMPRESA "Empresa"
    
    Menu:
    1. Ver Funcionarios
    2. Inserir Funcionarios
    3. Ver Departamento 
    4. Inserir Departamento
    0. Sair''')
    opcoes = input ('Digite o nome da opção escolhida:')
    match opcoes:
        case "1":
            mostrarFuncionario(con)
        case "2":
            inserirFuncionario(con)
    funcionarioEscolhido = input("Escolha o id do funcionario que deseja alterar:")
    funcionarioConsulta = con.consultarBanco(f'''
    SELECT * FROM "Funcionarios"
    WHERE "ID" = '{funcionarioEscolhido}' ''')[0]
    funcionario = Funcionario(funcionarioConsulta[0],funcionarioConsulta[1],funcionarioConsulta[2],funcionarioConsulta[3],funcionarioConsulta[4])
    #primeiro funcionario primeira informação dele
    print(f"Funcionario escolhido foi:")
    funcionario.imprimirFuncionario()
    opcao = input ('Voce deseja alterar as info basica (1) ou departamento(2)?')
    match opcao:
        case "1":
            funcionario.nome=input("Escreva o novo nome:")
            funcionario.cpf = input("Escreva o novo cpf:")
            funcionario.salario = input("Escreva o novo salario:")
            con.manipularBanco(funcionario.atualizarFuncionario("Funcionarios"))
        case "2":
            funcionario.idDep = input("Insira o id do novo departamento:")
            con.manipularBanco(funcionario.atualizarDepFuncionario("Funcionarios"))
    funcionario.imprimirFuncionario()
    mostrarFuncionario(con)
    

    con._db.close()
except(Exception,psycopg2.Error) as error:
    print("Ocorreu um erro",error)