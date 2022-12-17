from ArquivosMemoriaPrincipal.Multilista import MultilistaAnimalFavorito
from Servicos.ProcessadorFiles import *
from Servicos.DiretorioManager import *
import os

class SvcCadastros:
    def __init__(self):
        self.__diretorioManager = DiretorioManager()
        self.__pathArquivos = self.__diretorioManager.GetDiretorioArquivos(os.getcwd())
        self.__processadorFiles = ProcessadorFiles()
        self.__multilista = MultilistaAnimalFavorito()

    def getCadastros(self) -> []:
        return self.__processadorFiles.getFileAsArr(self.__pathArquivos + "/Cadastros")

    def getCadastrosAsString(self) -> str:
        return self.__processadorFiles.getFileContent(self.__pathArquivos + "/Cadastros")

    def limparCadastros(self):
        self.__processadorFiles.limparFile(self.__pathArquivos + "/Cadastros")

    def salvarCadastros(self, pCadastros: []):
        msg = ""
        for i in range(len(pCadastros)):
            msg += str(pCadastros[i].index) + ","
            msg += pCadastros[i].nome + ","
            msg += pCadastros[i].matricula + ","
            msg += pCadastros[i].curso + ","
            msg += str(pCadastros[i].vontadeDeViver) + ","
            msg += pCadastros[i].time + ","
            msg += pCadastros[i].animalFavorito + ","
            msg += str(pCadastros[i].indexNextCurso) + ","
            msg += str(pCadastros[i].indexNextAnimal) + ","
            msg += str(pCadastros[i].indexNextTime)
            msg += "\n"

        self.__processadorFiles.inserirDataEmFile(self.__pathArquivos + "/Cadastros", msg)

    def salvarEIndexarCadastros(self, pCadastros: []):
        msg = ""
        for i in range(len(pCadastros)):
            msg += str(pCadastros[i].index) + ","
            msg += pCadastros[i].nome + ","
            msg += pCadastros[i].matricula + ","
            msg += pCadastros[i].curso + ","
            msg += str(pCadastros[i].vontadeDeViver) + ","
            msg += pCadastros[i].time + ","
            msg += pCadastros[i].animalFavorito + ","

            self.__multilista.acessarESetarProximoAnimal(pCadastros[i].animalFavorito, i)

            msg += pCadastros[i].indexNextCurso + ","
            msg += pCadastros[i].indexNextAnimal + ","
            msg += pCadastros[i].indexNextTime
            msg += "\n"

        self.__processadorFiles.inserirDataEmFile(self.__pathArquivos + "/Cadastros", msg)



