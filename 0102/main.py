from Controle.classConexao import Conexao
from Modelo.classFuncionario import Funcionario
import psycopg2
def mostrarFuncionario(conexao):
    listaFuncionarios = conexao.consultarBanco('''
    SELECT * FROM "Funcionarios"
    ORDER BY "ID" ASC''')
    print ("ID | Nome")
    for func in listaFuncionarios:
        print(f"{func[0]} - {func[1]} \n")
try:
    con = Conexao("Empresa","localhost","5432","postgres","cateq2023")
    mostrarFuncionario(con)
    funcionarioEscolhido = input("Escolha o id do funcionario que deseja alterar:")
    funcionarioConsulta = con.consultarBanco(f'''
    SELECT * FROM "Funcionarios"
    WHERE "ID" = '{funcionarioEscolhido}' ''')
    funcionario = Funcionario(funcionarioConsulta[0][0],funcionarioConsulta[0][1],funcionarioConsulta[0][2],funcionarioConsulta[0][3],funcionarioConsulta[0][4])
    print(f"Funcionario escolhido foi:")
    print(funcionario.imprimirFuncionario())
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
    print(funcionario.imprimirFuncionario())
    mostrarFuncionario(con)
    

    con._db.close()
except(Exception,psycopg2.Error) as error:
    print("Ocorreu um erro",error)