from Servicos.ProcessadorFiles import *
from random import *
from DTO.CadastroDTO import *
from Servicos.DiretorioManager import *
import os
class GeradorDeDados:
    def __init__(self):
        self.__dirManager = DiretorioManager()
        self.__processadorDeFiles = ProcessadorFiles()


#index, nome, matricula curso, vontadeDeViver, time, animal, indexNextCurso = -1, indexNextAnimal = -1, indexNextTime = -1

    def gerarCadastros(self, pQuantidade: int) -> []:
        cont = 0
        self.__pathArquivos = self.__dirManager.GetDiretorioArquivos(os.getcwd())
        arrNomes = self.__processadorDeFiles.getFileAsArr(self.__pathArquivos + "/Nomes")
        arrCursos = self.__processadorDeFiles.getFileAsArr(self.__pathArquivos + "/Cursos")
        arrAnimais = self.__processadorDeFiles.getFileAsArr(self.__pathArquivos + "/Animal")
        arrTimes = self.__processadorDeFiles.getFileAsArr(self.__pathArquivos + "/Times")
        arrCadastros = []

        for i in range(pQuantidade):
            nomeAleatorio = arrNomes[randint(0, len(arrNomes) - 1)]
            matriculaAleatorio = self.getMatricula()
            cursoAleatorio = arrCursos[randint(0, len(arrCursos) - 1)]
            vontadeDeViverAleatorio = randint(0, 100)
            timeAleatorio = arrTimes[randint(0, len(arrTimes) - 1)]
            animalAleatorio = arrAnimais[randint(0, len(arrAnimais) - 1)]

            cadastroAleatorio = CadastroDTO(cont, nomeAleatorio, matriculaAleatorio,cursoAleatorio,
                                            vontadeDeViverAleatorio, timeAleatorio, animalAleatorio)
            arrCadastros.append(cadastroAleatorio)
            cont += 1

        return arrCadastros

    def get100Generico(self, FileName):
        arrBase = self.__processadorDeFiles.getFileAsArr(FileName)
        arr100Generic = []

        if len(arrBase) == 0:
            return "Arquivo vazio"

        for _ in range(100):
            numeroAleatorio = randint(0, len(arrBase) - 1)
            arr100Generic.append(arrBase[numeroAleatorio])

        return arr100Generic

    def getMatricula(self) -> str:
        numeroGerado = ""
        for _ in range(8):
            numeroAleatorio = randint(0,10)
            numeroGerado += str(numeroAleatorio)

        return numeroGerado

    def get100VontadeDeViver(self):
        arrVontadesDeViver = []
        for _ in range(100):
            arrVontadesDeViver.append(randint(0, 100))

        return arrVontadesDeViver
