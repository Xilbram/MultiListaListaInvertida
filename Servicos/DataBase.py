from Servicos.DiretorioManager import *
from Servicos.ProcessadorFiles import *
from Servicos.GeradorDados import *
import os
from ArquivosMemoriaPrincipal.Multilista import *

class DataBase:
    def __init__(self):
        self.__nomes = None
        self.__times = None
        self.__cursos = None
        self.__matriculas = None
        self.__vontadeDeViver: int = None
        self.__animalFavorito = None
        self.__processadorFiles = ProcessFiles()
        self.__geradorDeDados = GeradorDeDados()
        self.__limpadorDiretorio = DiretorioManager()
        self.__pathArquivos = self.__limpadorDiretorio.GetDiretorioArquivos(os.getcwd())
        self.__indexador = 1
        self.__multilista = MultilistaAnimalFavorito()

    def preencherDataBase(self):
        self.__nomes = self.__geradorDeDados.get100Generico(self.__pathArquivos + "/Nomes")
        self.__times = self.__geradorDeDados.get100Generico(self.__pathArquivos + "/Animal")
        self.__cursos = self.__geradorDeDados.get100Generico(self.__pathArquivos + "/Cursos")
        self.__animalFavorito = self.__geradorDeDados.get100Generico(self.__pathArquivos + "/Times")
        self.__matriculas = self.__geradorDeDados.Get100Matriculas()
        self.__vontadeDeViver = self.__geradorDeDados.get100VontadeDeViver()

    def limparDataBaseMemPrincipal(self):
        self.____nomes = None
        self.__times = None
        self.__cursos = None
        self.__matriculas = None
        self.__vontadeDeViver: int = None
        self.__animalFavorito = None
        self.__indexador = 1
    def limparDataBaseMemSecundaria(self):
        self.__processadorFiles.limparFile(self.__pathArquivos + "/Matriculas")

    def mostrarTodosDados(self):
        msg = ""
        for i in range(len(self.__nomes)):
            msg += str(self.__indexador) + ", "
            msg += self.__nomes[i] + ", "
            msg += self.__cursos[i] + ", "
            msg += str(self.__vontadeDeViver[i]) + ", "
            msg += self.__animalFavorito[i] + ", "
            msg += self.__times[i] + ", "
            msg += str(-1) + ", "
            msg += str(-1) + ", "
            msg += str(-1)
            msg += "\n"

            self.__indexador += 1

        print(msg)
        self.__indexador = 1

    def salvarDados(self):
        msg = ""
        cabecalho = "Index, Nome, Curso, Vontade de viver, Animal Favorito, Time, NextCurso, NextAnimal, NextTime" + "\n"
        for i in range(len(self.__nomes)):
            self.__indexador += 1

            msg += str(self.__indexador) + ","
            msg += self.__nomes[i] + ", "
            msg += self.__cursos[i] + ", "
            msg += str(self.__vontadeDeViver[i]) + ", "
            msg += self.__animalFavorito[i] + ", "
            msg += self.__times[i] + ", "
            msg += str(-1) + ", "
            msg += self.__multilista.adicionarProximoAnimal()+ ", "
            msg += str(-1)

            msg += "\n"


        self.__processadorFiles.inserirDataEmFile(self.__pathArquivos + "/Matriculas", cabecalho)
        self.__processadorFiles.inserirDataEmFile(self.__pathArquivos + "/Matriculas", msg)
        self.__indexador = 1



db = DataBase()
db.preencherDataBase()
db.mostrarTodosDados()
db.salvarDados()

db.limparDataBaseMemPrincipal()
#db.limparDataBaseMemSecundaria()

