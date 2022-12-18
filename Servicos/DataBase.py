from Servicos.SvcCadastros import SvcCadastros
from Servicos.GeradorDados import *
from ArquivosMemoriaPrincipal.ListaInvertida import *
from ArquivosMemoriaPrincipal.Multilista import *

class DataBase:
    def __init__(self):
        self.__cadastros: [CadastroDTO] or None = None
        self.__geradorDeDados = GeradorDeDados()
        self.__servicosCadastros = SvcCadastros()
        self.__listaInvertidaAnimais = ListaInvertida()
        self.__listaInvertidaCursos = ListaInvertida()
        self.__listaInvertidaTimes = ListaInvertida()
        self.__listaInvertidaVontadeDeViver = ListaInvertida()
        self.__listasInvertidas = [self.__listaInvertidaAnimais,self.__listaInvertidaCursos,
                                   self.__listaInvertidaTimes, self.__listaInvertidaVontadeDeViver]
        self.__multiListas = Multilista()


    def preencherDataBase(self, pQuantidade):
        self.__cadastros = self.__geradorDeDados.gerarCadastros(pQuantidade)

    def limparDataBaseMemPrincipal(self):
        self.__cadastros = None

    def limparDataBaseMemSecundaria(self):
        self.__servicosCadastros.limparCadastros()

    def mostrarTodosDadosMemoriaSecundaria(self):
        cadastros = self.__servicosCadastros.getCadastrosAsString()
        print(cadastros)

    def salvarDados(self):
        self.__servicosCadastros.salvarCadastros(self.__cadastros)

    def salvarEIndexarDados(self):
        self.__servicosCadastros.salvarEIndexarCadastros(self.__cadastros, self.__listasInvertidas)

    def retornarListasInvertidas(self):
        for i in range(3):
            print(self.__listasInvertidas[i].mostrarIndexados())

    def indexarMultilistas(self):
        self.__multiListas.indexarPorListaInvertida(self.__listasInvertidas)

    def teste(self):
        self.preencherDataBase(100)
        self.salvarEIndexarDados()
        self.indexarMultilistas()



#db = DataBase()
#db.teste()
#db.limparDataBaseMemSecundaria()
#db.mostrarTodosDados()
#db.salvarDados()
#db.limparDataBaseMemPrincipal()
#db.limparDataBaseMemSecundaria()
