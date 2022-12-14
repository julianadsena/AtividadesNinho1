# . Crie uma classe Livro que possui os atributos nome, qtdPaginas, autor e preço.
# – Crie os métodos getPreco para obter o valor do preco e o método setPreco para
# setar um novo valor do preco.
# Crie um codigo de teste

class Livro:
    def __init__(self, nome, qtdPaginas,autor,preco):
        self.nome = nome
        self.qtdPaginas = qtdPaginas
        self.autor = autor
        self.preco = preco
    def getPreco(self):
        preco = self.preco
        return preco
    def setPreco(self,novoPreco):
        self.preco = novoPreco        
x = input('Nome do livro:')
y = int(input('Quantidade de paginas:'))
z = input('Nome do autor:')
w = float(input('Preco do Livro:'))
u = float(input('Insira o novo preco do livro:'))
livro1 = (Livro(x,y,z,w))
livro1.setPreco(u)
print('O novo preco do livro é',livro1.getPreco())
        
        