from Servicos.SvcCadastros import *
from Servicos.GeradorDados import *
from Servicos.ProcessadorFiles import *
import os
from ArquivosMemoriaPrincipal.Multilista import *
import DiretorioManager

class DataBase:
    def __init__(self):
        self.__cadastros: [CadastroDTO] or None = None
        self.__geradorDeDados = GeradorDeDados()
        self.__servicosCadastros = SvcCadastros()


    def preencherDataBase(self, pQuantidade):
        self.__cadastros = self.__geradorDeDados.gerarCadastros(pQuantidade)

    def limparDataBaseMemPrincipal(self):
        self.__cadastros = None

    def limparDataBaseMemSecundaria(self):
        self.__servicosCadastros.limparCadastros()

    def mostrarTodosDados(self):
        cadastros = self.__servicosCadastros.getCadastrosAsString()
        print(cadastros)

    def salvarDados(self):
        self.__servicosCadastros.salvarCadastros(self.__cadastros)

    def salvarEIndexarDados(self):
        self.__servicosCadastros.salvarEIndexarCadastros(self.__cadastros)


db = DataBase()
db.preencherDataBase(100)
#db.mostrarTodosDados()
#db.salvarDados()
db.salvarEIndexarDados()

#db.limparDataBaseMemPrincipal()
#db.limparDataBaseMemSecundaria()
