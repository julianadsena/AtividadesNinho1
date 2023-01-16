class Pokemon:                      
    def __init__(self,nome,tipo,movimento,ataque,defesa,hp):
        self.nome = nome
        self.tipo = tipo
        self.movimento = movimento
        self.ataque = ataque
        self.defesa = defesa 
        self.hp = hp
class Aquatico(Pokemon):
    def __init__(self, nome, tipo,movimento, ataque, defesa, hp):
        super().__init__(nome, tipo,movimento, ataque, defesa, hp)
        self.tipo = "Aquatico"
class Fogo(Pokemon):
    def __init__(self, nome, tipo,movimento, ataque, defesa, hp):
        super().__init__(nome, tipo, movimento, ataque, defesa, hp)
        self.tipo = "Fogo"
class Grama(Pokemon):
    def __init__(self, nome, tipo, movimento, ataque, defesa, hp):
        super().__init__(nome, tipo, movimento, ataque, defesa, hp)
        self.tipo = "Grama"       
