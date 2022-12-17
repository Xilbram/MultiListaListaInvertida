from Servicos import ProcessadorFiles
from Servicos import DiretorioManager
import os

processadorFiles = ProcessadorFiles.ProcessadorFiles()
dirManager = DiretorioManager.DiretorioManager()
pathArquivos = dirManager.GetDiretorioArquivos(os.getcwd())

class MultilistaTimes:
    def __init__(self):
        self.times = 0


class MultilistaCursos:
    def __init__(self):
        self.algo = 0


class ListaInvertidaAnimaisFavoritos:
    def __init__(self):
        self.diretorioAnimais = {}
        #self.animais = processador.returnFileAsArr(pathArquivos + "/Animal")

    def inserir(self, pAnimal, pIndex):
        if pAnimal in self.diretorioAnimais.keys():
            self.diretorioAnimais[pAnimal] = self.diretorioAnimais[pAnimal] + f',{pIndex}'

        self.diretorioAnimais[pAnimal] = pIndex






