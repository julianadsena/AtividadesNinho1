from tkinter import *
import ttkthemes
from tkinter import ttk,messagebox
import psycopg2
class Paciente:
    def __init__(self,id,nome,contato,dataNasc,dtAgend,horario,tipo,medico,confirmacao):
        self._id = id
        self._nome = nome
        self._dataNasc = dataNasc
        self._dtAgend=dtAgend
        self._horario = horario
        self._tipo=tipo
        self._medico = medico
        self._confirmacao = confirmacao
    def adicionarPaciente(self):       
        sql = f'''
        INSERT INTO "Clinica"
        VALUES(default,{self._nome},{self._dataNasc},{self._dtAgend},{self._horario},{self._tipo},{self._medico},{self._confirmacao})'''
        return sql
    def consultarPaciente(self):
        sql=f'''
        SELECT * FROM "Pacientes"
        WHERE "DataAgendamento"='{self._dtAgend}'
        '''
        return sql
    def deletarPaciente(self):
        sql=f'''
        SELECT * FROM "Paciente"'''
                 