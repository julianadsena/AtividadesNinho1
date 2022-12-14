class Pessoa:
    def __init__(self,nome,sexo,cpf,ativo):
        self.nome = nome
        self.sexo = sexo
        self.ativo = ativo
    def desativar(self):
        self.ativo = False
        print('A pessoa foi desativada com sucesso')
if __name__ == "__main__": #codigo que deseja ser executado
    pessoa1 = Pessoa ("João","M","123456",True)
    pessoa1.desativar()
if pessoa1.ativo == False:
    print('A pessoa está desativada')
else:
    print(pessoa1.nome,pessoa1.sexo,pessoa1.ativo)