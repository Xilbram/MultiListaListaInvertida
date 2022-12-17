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


class MultilistaAnimalFavorito:
    def __init__(self):
        self.diretorioAnimais = {}
        #self.animais = processador.returnFileAsArr(pathArquivos + "/Animal")

    def acessarESetarProximoAnimal(self, pAnimal:str, pIndex):
        if pAnimal in self.diretorioAnimais.keys():
            indexPrimeiroAnimal = self.diretorioAnimais[pAnimal]
            contVirgulas = 0

            #Pega uma linha do file como array
            #Itera até após a 7 virgula (posicao de index do proximo animal)
            #Acessa o próximo index, se -1 encerra
            while True:
                linha = processadorFiles.getLinhaFileAsString(pathArquivos + "/Cadastros", indexPrimeiroAnimal)
                arrLinha = list(linha)

                for j in range(len(linha)):
                    if linha[j] == ',':
                        contVirgulas += 1
                        if contVirgulas == 8:
                            numeroLinhaSubstituir = linha[0]
                            indexProximoAnimal = linha[j + 1]
                            posicaoIndexProximoAnimal = j + 1
                            break

                if indexProximoAnimal == "*":
                    arrLinha[posicaoIndexProximoAnimal] = pIndex
                    processadorFiles.substituirLinha(pathArquivos + "/Cadastros", int(numeroLinhaSubstituir), str(arrLinha))
                    return

                indexProximoAnimal = indexProximoAnimal


        else:
            self.diretorioAnimais[pAnimal] = pIndex







