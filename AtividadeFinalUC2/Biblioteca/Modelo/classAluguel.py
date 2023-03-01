#   DROP TABLE IF EXISTS "Aluguel";
#     CREATE TABLE "Aluguel"(
#         "ID" int GENERATED ALWAYS AS IDENTITY,
#         "ID_Cliente" int NOT NULL,
#         "ID_Livro" int NOT NULL,
#         "Data_Aluguel" timestamp default current_timestamp,
#         Primary Key("ID"),
#         Constraint fk_cliente
#             Foreign Key ("ID_Cliente")
#             References "Cliente"("ID")
#             ON DELETE CASCADE
#             ON UPDATE NO ACTION
#             ,
#         Constraint fk_livro
#             Foreign Key ("ID_Livro")
#             Refereces "Livro"("ID")
#             ON DELETE SET NULL
#             ON UPDATE NO ACTION
            
#     );
#     ''')
class Aluguel:
    def __init__(self,id,dataAluguel):
        self._id = id
        self._dataAluguel = dataAluguel        
    def imprimirAluguel(self):
        print(f'''
        ID - {self._id}
        Data - {self._dataAluguel}
        ''')

    def consultarClientePorID(self):
        sql = f'''
        SELECT * FROM "Cliente"
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def consultarAlugueis(self):
        sql = f'''
        SELECT * FROM "Aluguel"
        WHERE "ID" = '{self._id}'
        '''
        return sql

    def inserirCliente(self):
        sql = f'''
        INSERT INTO "Cliente"
        VALUES(default, '{self._nome}', '{self._cpf}')
        
        '''

        return sql