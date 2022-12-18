from Servicos import ProcessadorFiles
from Servicos import DiretorioManager
import os

class Multilista():
    def __init__(self):
        self.__diretorioAnimais = {}
        self.__diretorioTimes = {}
        self.__diretorioCursos = {}
        self.__diretorioVontadeViver = {}
        self.__dicts = [self.__diretorioAnimais,self.__diretorioTimes,self.__diretorioCursos,self.__diretorioVontadeViver]
        self.__dirManager = DiretorioManager.DiretorioManager()
        self.__pathArquivos = self.__dirManager.GetDiretorioArquivos(os.getcwd())
        self.__processadorFiles = ProcessadorFiles.ProcessadorFiles()

    def indexarPorListaInvertida(self, pListaInvertidas: list):
        tipoIndexacao = 0

        for listaInvertida in pListaInvertidas:
            dict: dict = listaInvertida.getIndexados()
            cont = 0

            for key in dict.keys():
                arrIndexar = dict[key]
                if tipoIndexacao == 0:
                    self.__diretorioAnimais[key] = arrIndexar[0]
                if tipoIndexacao == 1:
                    self.__diretorioCursos[key] = arrIndexar[0]
                if tipoIndexacao == 2:
                    self.__diretorioTimes[key] = arrIndexar[0]
                if tipoIndexacao == 3:
                    self.__diretorioVontadeViver[key] = arrIndexar[0]

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

        for char in linha:
            if char == ';':
                contVirgulas += 1

            if contVirgulas == totalVirgulas:
                alvoAlteracao += char

            if char == "\n":
                break

        alvoAlteracao = alvoAlteracao[1:]
        return alvoAlteracao

    def getKeys(self, pTipoIndexacao) -> []:
        num = int(pTipoIndexacao)
        dictEscolhido = self.__dicts[num -1]
        keyArr = []

        for key in dictEscolhido.keys():
            keyArr.append(key)

        return keyArr

    def getIndexados(self, pTipoIndexacao, pEscolha):
        num = int(pTipoIndexacao)
        dictEscolhido = self.__dicts[num -1]
        arrIndex = []
        keyEscolhida = str(pEscolha)
        keyEscolhida = keyEscolhida.capitalize()
        keyEscolhida = ";" + keyEscolhida

        primeiroAlvo = dictEscolhido[keyEscolhida]
        alvo = primeiroAlvo

        while True:
            nextIndex = self.acessarLinhaEPegarProxIndex(int(alvo), pTipoIndexacao)
            alvo = nextIndex
            arrIndex.append(nextIndex)

            if nextIndex == "-1":
                break

        for i in range(len(arrIndex)):
            print(self.__processadorFiles.getLinhaFileAsString(self.__pathArquivos + "/Cadastros", arrIndex[i]))














