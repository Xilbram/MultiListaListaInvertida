from ProcessadorFiles import *
from random import *
class GeradorDeDados:
    def __init__(self):
        self.processadorDeFiles = ProcessFiles()

    def get100Generico(self, FileName: str):
        try:
            self.processadorDeFiles.returnFileAsArr(FileName)
        except Exception:

    def Get100Nomes(self):
        return self.processadorDeFiles.returnFileAsArr("Nomes")

    def Get100Matriculas(self):
        string_vazia = ""
        arrMatriculas = []
        for _ in range(8):
            numeroAleatorio = randint(0,10)
            string_vazia += str(numeroAleatorio)

        numeroGerado = int(string_vazia)
        arrMatriculas.append(numeroGerado)
        return arrMatriculas

    def Get100Cursos(self):
        arrCursosBase = processador.returnFileAsArr("Cursos")
        arr100Cursos = []
        for _ in range(100):
            numeroAleatorio = randint(0,len(arrCursosBase))
            arr100Cursos.append(arrCursosBase[numeroAleatorio])

        return arr100Cursos

    def get100Times(self):
        arrTimesBase = processador.returnFileAsArr("Times")
        arr100Times = []
        for _ in range(100):
            numeroAleatorio = randint(0, len(arrTimesBase))
            arr100Times.append(arrTimesBase[numeroAleatorio])

        return arr100Times

    def get100VontadeDeViver(self):
        arrVontadesDeViver = []
        for _ in range(100):
            arrVontadesDeViver.append(randint(-50,50))

        return arrVontadesDeViver

    def get100Cigarros(self):
        arrTimesBase = processador.returnFileAsArr("Times")
        arr100Times = []
        for _ in range(100):
            numeroAleatorio = randint(0, len(arrTimesBase))
            arr100Times.append(arrTimesBase[numeroAleatorio])

        return arr100Times