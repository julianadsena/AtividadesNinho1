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
                if funcionario.getLogin() == login:
                    if funcionario.getSenha() == senha:    
                        self.setFuncionarioLogado (funcionario)
                        print(f"Logado com {self.getFuncionarioLogado().getNome()}")
                        break
    def imprimirFuncionarios(self): #visualizar lista de funcionario 
        print("Método de impressão com contador")
        for i in range(len(self._listaFuncionarios)):
            print(f"{i+1} - {self._listaFuncionarios[i]._nome}")
        print("Método percorrendo lista")
        for func in self._listaFuncionarios:
            print(f"{func._id} - {func._nome}")
    def visualizarFuncionario(self,idFuncionario):
        for func in self._listaFuncionarios:
            if str(func._id) == idFuncionario:
                func.mostrarFuncionario()
                return "Funcionario encontrado"
        else: 
            print("O id não existe na lista de funcionário")



