import os

import Servicos.DiretorioManager
from Servicos.ProcessadorFiles import *


def TesteProcessador():
    processador = ProcessFiles()
    arr = processador.returnFileAsArr("Arquivos/")
    for i in range(len(arr)):
        print(arr[i])
    print(arr)


def TesteFiles():
    teste = Servicos.DiretorioManager.DiretorioManager()
    ok = teste.GetDiretorioArquivos(os.getcwd())

    print(ok)


def TesteLimparFile():
    dir = Servicos.DiretorioManager.DiretorioManager()
    path = dir.GetDiretorioArquivos(os.getcwd())

    teste = ProcessFiles()
    teste.limparFile(path + "/Matriculas")
    print("ok")
    print(path)


def TesteRemoverWhitespace():
    dir = Servicos.DiretorioManager.DiretorioManager()
    path = dir.GetDiretorioArquivos(os.getcwd())

    teste = ProcessFiles()
    teste.removerEspacosEmBranco(path + "/NomeBackup")


def TestePegarLinha():
    dir = Servicos.DiretorioManager.DiretorioManager()
    path = dir.GetDiretorioArquivos(os.getcwd())

    teste = ProcessFiles()
    msg = teste.getLinhaFileAsString(path + "/NomeBackup", 5)
    print(msg)

def TesteSubstituirLinha():
    dir = Servicos.DiretorioManager.DiretorioManager()
    path = dir.GetDiretorioArquivos(os.getcwd())

    teste = ProcessFiles()
    teste.SubstituirLinha(path + "/MatriculasIndexadas", 2, "msg")

#TesteLimparFile()

#TesteRemoverWhitespace()
#TestePegarLinha()
TesteSubstituirLinha()