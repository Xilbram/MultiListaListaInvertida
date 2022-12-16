from Servicos.LimpadorDiretorios import *
from Servicos.ProcessadorFiles import *
from Servicos.GeradorDados import *
import os
class DataBase:
    def __init__(self):
        self.nomes = None
        self.times = None
        self.cursos = None
        self.matriculas = None
        self.vontadeDeViver: int = None
        self.animalFavorito = None
        self.geradorDeDados = GeradorDeDados()
        self.limpadorDiretorio = LimpadorDiretorio()

    def preencherDataBase(self):
        path_base = self.limpadorDiretorio.GetDiretorioArquivos(os.getcwd())

        self.nomes = self.geradorDeDados.get100Generico(path_base + "/Nomes")
        self.times = self.geradorDeDados.get100Generico(path_base + "/Animal")
        self.cursos = self.geradorDeDados.get100Generico(path_base + "/Cursos")
        self.animalFavorito = self.geradorDeDados.get100Generico(path_base + "/Times")
        self.matriculas = self.geradorDeDados.Get100Matriculas()
        self.vontadeDeViver = self.geradorDeDados.get100VontadeDeViver()

    def mostrarTodosDados(self):
        msg = ""
        for i in range(len(self.nomes)):
            msg += self.nomes[i] + "/"
            msg += self.cursos[i] + "/"
            msg += str(self.vontadeDeViver[i]) + "/"
            msg += self.animalFavorito[i] + "/"
            msg += self.times[i]
            msg += "\n"

        print(msg)


db = DataBase()
db.preencherDataBase()
db.mostrarTodosDados()
