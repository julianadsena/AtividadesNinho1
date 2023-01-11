import json
from empresa import Empresa
from funcionario import Funcionario,Gerente
with open("funcionarios.json") as f:
    dados = json.load(f)
funcionarios = []
for func in dados:
    if func["Cargo"] == "Gerente":
        funcionarios.append(Gerente(func["ID"],func["Nome"],func["CPF"],func["Salario"],func["Cargo"],func["Login"],func["Senha"]))
    else:
        funcionarios.append(Funcionario(func["ID"],func["Nome"],func["CPF"],func["Salario"],func["Cargo"]))
empresa = Empresa(funcionarios)
print("Bem vindo a Empresa CATEQ")
print("Faça seu login")
usuarioLogin = input("Escreva seu login:")
usuarioSenha = input("Escreva sua senha:")
empresa.login(usuarioLogin,usuarioSenha)
print(vars(empresa.getFuncionarioLogado()))
empresa.imprimirFuncionarios()