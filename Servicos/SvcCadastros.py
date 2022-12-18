import DTO.CadastroDTO
from ArquivosMemoriaPrincipal.ListaInvertida import *
from Servicos.DiretorioManager import *
from Servicos.ProcessadorFiles import *
from DTO.CadastroDTO import *
import os

class SvcCadastros:
    def __init__(self):
        self.__diretorioManager = DiretorioManager()
        self.__pathArquivos = self.__diretorioManager.GetDiretorioArquivos(os.getcwd())
        self.__processadorFiles = ProcessadorFiles()

    def buscarCadastroPorIndexListaInvertida(self, pIndex) -> str:
        indexLinha = int(pIndex)
        linha = self.__processadorFiles.getLinhaFileAsString(self.__pathArquivos + "/Cadastros", indexLinha + 1)
        return linha

    def getCadastrosAsARR(self) -> []:
        return self.__processadorFiles.getFileAsArr(self.__pathArquivos + "/Cadastros")

    def getCadastrosAsString(self) -> str:
        return self.__processadorFiles.getFileContent(self.__pathArquivos + "/Cadastros")

    def getCadastrosAsDTO(self) -> [CadastroDTO]:
        msg = self.getCadastrosAsString()
        countSeparadores = 0
        DTOS = []
        index = ""
        nome = ""
        matricula = ""
        curso = ""
        vontadeDeViver = ""
        time = ""
        animal = ""
        indexNextCurso = ""
        indexNextAnimal = ""
        indexNextTime = ""
        indexNextVontadeViver = ""

        #Isso aqui podia ser bem melhor elaborado mas to sem ideias
        for char in msg:
            if char == ";":
                countSeparadores += 1

            if countSeparadores == 0:
                index += char
            if countSeparadores == 1:
                nome += char
            if countSeparadores == 2:
                matricula += char
            if countSeparadores == 3:
                curso += char
            if countSeparadores == 4:
                vontadeDeViver += char
            if countSeparadores == 5:
                time += char
            if countSeparadores == 6:
                animal += char
            if countSeparadores == 7:
                indexNextCurso += char
            if countSeparadores == 8:
                indexNextAnimal += char
            if countSeparadores == 9:
                indexNextTime += char
            if countSeparadores == 10:
                indexNextVontadeViver += char

            if char == "\n":
                DTOS.append(CadastroDTO(index, nome, matricula, curso, vontadeDeViver, time, animal, indexNextCurso,
                                        indexNextAnimal, indexNextTime, indexNextVontadeViver))
                countSeparadores = 0
                index = ""
                nome = ""
                matricula = ""
                curso = ""
                vontadeDeViver = ""
                time = ""
                animal = ""
                indexNextCurso = ""
                indexNextAnimal = ""
                indexNextTime = ""
                indexNextVontadeViver = ""

        return DTOS



    def salvarCadastros(self, pCadastros: []):
        msg = ""
        for i in range(len(pCadastros)):
            msg += str(pCadastros[i].index) + ";"
            msg += pCadastros[i].nome + ";"
            msg += pCadastros[i].matricula + ";"
            msg += pCadastros[i].curso + ";"
            msg += str(pCadastros[i].vontadeDeViver) + ";"
            msg += pCadastros[i].time + ";"
            msg += pCadastros[i].animalFavorito + ";"
            msg += str(pCadastros[i].indexNextCurso) + ";"
            msg += str(pCadastros[i].indexNextAnimal) + ";"
            msg += str(pCadastros[i].indexNextTime) + ";"
            msg += str(pCadastros[i].indexNextVontadeDeViver)
            msg += "\n"

        self.__processadorFiles.inserirDataEmFile(self.__pathArquivos + "/Cadastros", msg)

    def indexarDados(self,  pCadastros: [], pListasInvertidas: []):
        for i in range(len(pCadastros)):
            pListasInvertidas[0].inserir(pCadastros[i].animalFavorito, pCadastros[i].index)
            pListasInvertidas[1].inserir(pCadastros[i].curso, pCadastros[i].index)
            pListasInvertidas[2].inserir(pCadastros[i].time, pCadastros[i].index)
            pListasInvertidas[3].inserir(pCadastros[i].vontadeDeViver, pCadastros[i].index)

        return pListasInvertidas

    def limparCadastros(self):
        self.__processadorFiles.limparFile(self.__pathArquivos + "/Cadastros")

    def salvarEIndexarCadastros(self, pCadastros: [], pListasInvertidas: []):
        msg = ""
        for i in range(len(pCadastros)):
            msg += str(pCadastros[i].index) + ";"
            msg += pCadastros[i].nome + ";"
            msg += pCadastros[i].matricula + ";"
            msg += pCadastros[i].curso + ";"
            msg += str(pCadastros[i].vontadeDeViver) + ";"
            msg += pCadastros[i].time + ";"
            msg += pCadastros[i].animalFavorito + ";"
            msg += pCadastros[i].indexNextCurso + ";"
            msg += pCadastros[i].indexNextAnimal + ";"
            msg += pCadastros[i].indexNextTime + ";"
            msg += pCadastros[i].indexNextVontadeDeViver
            msg += "\n"

            #indexa ListaInvertida
            pListasInvertidas[0].inserir(pCadastros[i].animalFavorito, pCadastros[i].index)
            pListasInvertidas[1].inserir(pCadastros[i].curso, pCadastros[i].index)
            pListasInvertidas[2].inserir(pCadastros[i].time, pCadastros[i].index)
            pListasInvertidas[3].inserir(pCadastros[i].vontadeDeViver, pCadastros[i].index)


        self.__processadorFiles.inserirDataEmFile(self.__pathArquivos + "/Cadastros", msg)



