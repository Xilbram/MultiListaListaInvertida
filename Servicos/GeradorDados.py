from ProcessadorFiles import *
from random import *
class GeradorDeDados:
    def __init__(self):
        self.__processadorDeFiles = ProcessFiles()

    def get100Generico(self, FileName):
        arrBase = self.__processadorDeFiles.returnFileAsArr(FileName)
        arr100Generic = []

        if len(arrBase) == 0:
            return "Arquivo vazio"

        for _ in range(100):
            numeroAleatorio = randint(0, len(arrBase) - 1)
            arr100Generic.append(arrBase[numeroAleatorio])

        return arr100Generic

    def Get100Matriculas(self):
        string_vazia = ""
        arrMatriculas = []
        for _ in range(8):
            numeroAleatorio = randint(0,10)
            string_vazia += str(numeroAleatorio)

        numeroGerado = int(string_vazia)
        arrMatriculas.append(numeroGerado)
        return arrMatriculas

    def get100VontadeDeViver(self):
        arrVontadesDeViver = []
        for _ in range(100):
            arrVontadesDeViver.append(randint(-50,50))

        return arrVontadesDeViver
