#2 Modelar a classe Empresa
class Empresa:
    def __init__(self,listaFuncionarios):
        self._listaFuncionarios = listaFuncionarios
        self._funcionarioLogado = "Nenhum usuário logado"
    def getListaFuncionarios(self):
        return self._listaFuncionarios
    def setListaFuncionarios(self,listaFuncionarios):
        self._listaFuncionarios = listaFuncionarios
    def getFuncionarioLogado(self):
        return self._funcionarioLogado
    def setFuncionarioLogado(self, funcionarioLogado):
        self._funcionarioLogado = funcionarioLogado
    def login(self,login,senha):
        for funcionario in self._listaFuncionarios:
            if funcionario.getCargo() == "Gerente":
                if funcionario.getLogin() == login:
                    if funcionario.getSenha() == senha:    
                        self.setFuncionarioLogado (funcionario)
                        print(f"Logado com {self.getFuncionarioLogado().getNome()}")
                        break
    def imprimirFuncionarios(self):
        print(self._listaFuncionarios)
        


