from Servicos import ProcessadorFiles
from Servicos import DiretorioManager
import os

processadorFiles = ProcessadorFiles.ProcessFiles()
dirManager = DiretorioManager.DiretorioManager()
pathArquivos = dirManager.GetDiretorioArquivos(os.getcwd())

class MultilistaTimes:
    def __init__(self):
        self.times = 0


class MultilistaCursos:
    def __init__(self):
        self.algo = 0


class MultilistaAnimalFavorito:
    def __init__(self):
        self.diretorioAnimais = {}
        #self.animais = processador.returnFileAsArr(pathArquivos + "/Animal")

    def acessarESetarProximoAnimal(self, pAnimal:str, pIndex):
        if pAnimal in self.diretorioAnimais.keys():
            primeiroAnimalIndexado = self.diretorioAnimais[pAnimal]
            indexadorMatricula = primeiroAnimalIndexado
            contVirgulas = 0

            #Pega uma linha do file como array
            #Itera até após a 7 virgula (posicao de index do proximo animal)
            #Acessa o próximo index, se -1 encerra
            while True:
                linhaRetorno = processadorFiles.getLinhaFileAsString(pathArquivos + "/Matriculas", indexadorMatricula)

                for j in range(len(linhaRetorno)):
                    if linhaRetorno[j] == ',':
                        contVirgulas += 1
                        if contVirgulas == 7:
                            linhaSubstituir = linhaRetorno[0]
                            proximoIndexador = linhaRetorno[j + 2]
                            posicaoSubstituir = j + 2
                            break

                if proximoIndexador == -1:
                    linhaRetorno[posicaoSubstituir] = pIndex
                    processadorFiles.SubstituirLinha(pathArquivos + "/Matriculas", linhaSubstituir, linhaRetorno)
                    return

                indexadorMatricula = proximoIndexador


        else:
            self.diretorioAnimais[pAnimal] = pIndex







