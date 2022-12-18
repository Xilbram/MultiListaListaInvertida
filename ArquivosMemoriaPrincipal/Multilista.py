from Servicos import ProcessadorFiles
from Servicos import DiretorioManager
import os

class Multilista():
    def __init__(self):
        self.__diretorioAnimais = {}
        self.__dirManager = DiretorioManager.DiretorioManager()
        self.__pathArquivos = self.__dirManager.GetDiretorioArquivos(os.getcwd())
        self.__processadorFiles = ProcessadorFiles.ProcessadorFiles()

    def indexarPorListaInvertida(self, pListaInvertidas: list):
        tipoIndexacao = 0

        for listaInvertida in pListaInvertidas:
            dict: dict = listaInvertida.mostrarIndexados()

            for key in dict.keys():
                arrIndexar = dict[key]
                for i in range(len(arrIndexar)):
                    try:
                        nextItem = arrIndexar[i + 1]
                    except IndexError:
                        nextItem = '-1'

                    self.acessarLinhaESettarProxIndex(arrIndexar[i], tipoIndexacao, nextItem)


            tipoIndexacao += 1


    def acessarLinhaESettarProxIndex(self, pIndexLinha,pTipoIndexacao,pProximoIndex):
        # animal
        totalVirgulas = 7
        # Curso
        if pTipoIndexacao == 1:
            totalVirgulas = 8
        # Time
        if pTipoIndexacao == 2:
            totalVirgulas = 9

        if pTipoIndexacao == 3:
            totalVirgulas = 10

        contVirgulas = 0
        linha = self.__processadorFiles.getLinhaFileAsString(self.__pathArquivos + "/Cadastros", pIndexLinha)
        numeroFoiAlterado = False
        novaLinha = ""


        for char in linha:

            if contVirgulas != totalVirgulas:
                novaLinha += char

            if (numeroFoiAlterado == False) and (contVirgulas == totalVirgulas):
                novaLinha += str(pProximoIndex)
                if (pTipoIndexacao != 3):
                    novaLinha += ";"
                else:
                    novaLinha += "\n"
                numeroFoiAlterado = True

            if char == ";":
                contVirgulas += 1

        self.__processadorFiles.substituirLinha(self.__pathArquivos + "/Cadastros", pIndexLinha, novaLinha)


    def acessarLinhaEPegarProxIndex(self, pIndexLinha, pTipoIndexacao) -> str:
        #animal
        totalVirgulas = 7
        #Curso
        if pTipoIndexacao == 1:
            totalVirgulas = 8
        #Time
        if pTipoIndexacao == 2:
            totalVirgulas = 9

        contVirgulas = 0
        linha = self.__processadorFiles.getLinhaFileAsString(self.__pathArquivos + "/Cadastros", pIndexLinha)
        alvoAlteracao = ""

        for char in linha():
            if char == ',':
                contVirgulas += 1
                if contVirgulas == totalVirgulas:
                    alvoAlteracao += char

        return alvoAlteracao











