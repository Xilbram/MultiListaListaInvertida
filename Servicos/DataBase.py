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
        self.__foiIndexado = False


    def preencherDataBase(self, pQuantidade):
        self.__cadastros = self.__geradorDeDados.gerarCadastros(pQuantidade)

    def limparDataBaseMemPrincipal(self):
        self.__cadastros = None

    def limparDataBaseMemSecundaria(self):
        self.__servicosCadastros.limparCadastros()

    def exibirDadosMemoriaPrincipal(self):
        if(self.__cadastros != None):
            print("Index, Nome, Matrícula, Curso, Vontade de viver, Time, Animal Favorito")
            for i in range(len(self.__cadastros)):
                print(self.__cadastros[i].returnAllData())
        else:
            print("Não há dados na memória principal")

    def exibirDadosMemoriaSecundaria(self):
        cadastros = self.__servicosCadastros.getCadastrosAsString()
        print(cadastros)

    def salvarDados(self):
        self.__servicosCadastros.salvarCadastros(self.__cadastros)
    def indexarDados(self):
        if self.__foiIndexado == False:
            self.__cadastros = self.__servicosCadastros.getCadastrosAsDTO()
            self.__listasInvertidas = self.__servicosCadastros.indexarDados(self.__cadastros, self.__listasInvertidas)
            self.__multiListas.indexarPorListaInvertida(self.__listasInvertidas)




    def salvarEIndexarDados(self):
        self.__servicosCadastros.salvarEIndexarCadastros(self.__cadastros, self.__listasInvertidas)
        self.__multiListas.indexarPorListaInvertida(self.__listasInvertidas)

    def retornarListasInvertidas(self):
        for i in range(3):
            print(self.__listasInvertidas[i].getIndexados())

    def getKeysDisponiveisListaInvertida(self, pColuna):
        self.indexarDados()
        if pColuna == "1":
            dictAnimais =  self.__listaInvertidaAnimais.getIndexados()
            for key in dictAnimais.keys():
                msg = str(key)
                print(msg)
        if pColuna == "2":
            dictTimes = self.__listaInvertidaTimes.getIndexados()
            for key in dictTimes.keys():
                msg = str(key)
                print(msg)
        if pColuna == "3":
            dictCursos = self.__listaInvertidaCursos.getIndexados()
            for key in dictCursos.keys():
                msg = str(key)
                print(msg)
        if pColuna == "4":
            dictVontadeViver = self.__listaInvertidaVontadeDeViver.getIndexados()
            for key in dictVontadeViver.keys():
                msg = str(key)
                print(msg)

    def getKeysMultilista(self, pColuna):
        self.indexarDados()
        arr = self.__multiListas.getKeys(pColuna)
        for item in arr:
            item = str(item)
            print(item)
    def getIndexadosPorMultilista(self, pColuna, pEspecificacao):
        self.__multiListas.getIndexados(pColuna, pEspecificacao)

    def atualizarListaInvertida(self):
        self.__cadastros = None
        self.__cadastros = self.__servicosCadastros.getCadastrosAsDTO()
        self.__listaInvertidaTimes = ListaInvertida()
        self.__listaInvertidaCursos = ListaInvertida()
        self.__listaInvertidaVontadeDeViver = ListaInvertida()
        self.__listaInvertidaAnimais = ListaInvertida()
        self.__listasInvertidas = self.__servicosCadastros.indexarDados(self.__cadastros, self.__listasInvertidas)

    def getResultadosPorDuasColunas(self, pColuna1, pEspecificacao1, pColuna2, pEspecificacao2):
        self.atualizarListaInvertida()
        dict1 = self.__listasInvertidas[int(pColuna1) - 1].getIndexados()
        dict2 = self.__listasInvertidas[int(pColuna2) - 1].getIndexados()

        arr1 = dict1[pEspecificacao1]
        arr2 = dict2[pEspecificacao2]

        result = list(set(filter(lambda x: x in arr1, arr2)))


        if(len(result) == 0):
            print("Não há dados com tais compartibilidades")
        else:
            for i in range(len(result)):
                print(self.__servicosCadastros.getLinhaAsStr(result[i]))

    def inserirCadastro(self, data):
        self.__servicosCadastros.inserirCadastro(data)

    def removerCadastro(self, pIndex):
        self.__servicosCadastros.removerCadastro(pIndex)

    def buscarCadastroPorListaInvertida(self, pColuna, pEspecificacao: str):
        if pColuna == "1":
            dictAnimais = self.__listaInvertidaAnimais.getIndexados()

            chaveEntrada = ";" + pEspecificacao.capitalize()
            arrAnimais = dictAnimais[chaveEntrada]

            for i in range(len(arrAnimais)):
                print(self.__servicosCadastros.buscarCadastroPorIndexListaInvertida(arrAnimais[i]))

        if pColuna == "2":
            dictTimes = self.__listaInvertidaTimes.getIndexados()

            arr = dictTimes[pEspecificacao]

            for i in range(len(arr)):
                print(self.__servicosCadastros.buscarCadastroPorIndexListaInvertida(arr[i]))


        if pColuna == "3":
            dictCursos = self.__listaInvertidaCursos.getIndexados()

            arr = dictCursos[pEspecificacao]

            for i in range(len(arr)):
                print(self.__servicosCadastros.buscarCadastroPorIndexListaInvertida(arr[i]))


        if pColuna == "4":
            dictVontadeViver = self.__listaInvertidaVontadeDeViver.getIndexados()

            arr = dictVontadeViver[pEspecificacao]

            for i in range(len(arr)):
                print(self.__servicosCadastros.buscarCadastroPorIndexListaInvertida(arr[i]))





