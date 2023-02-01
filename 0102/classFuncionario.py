class Funcionario:
    def __init__(self,id,nome,cpf,salario,idDep):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.idDep = idDep
    def imprimirFuncionario(self):
        print(f'''
            Informações do funcionario
            ID = {self.id}
            Nome = {self.nome}
            CPF = {self.cpf}
            Salario = {self.salario}
            Departamento = {self.idDep}''')
    def inserirFuncionario(self,tabela):
        query = (f'''
            INSERT INTO "{tabela}"
            VALUES (default,'{self.nome}','{self.cpf}','{self.salario}','{self.idDep}') ''')
        return query
    def atualizarFuncionario(self,tabela):
        codigoSql = f'''
        UPDATE "{tabela}"
        SET "Nome"='{self.nome}',"CPF" = '{self.cpf}',"Salario" = '{self.salario}',"IDdep" = '{self.idDep}'
        WHERE "ID" = {self.id}'''
        return codigoSql
    def atualizarDepFuncionario(self,tabela):
        codigoSql = f'''
        UPDATE "{tabela}"
        SET "IDdep" = '{self.idDep}'
        WHERE "ID" = {self.id}'''
        return codigoSql