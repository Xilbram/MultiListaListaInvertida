import os

import Servicos.DiretorioManager
from Servicos.ProcessadorFiles import *


def TesteProcessador():
    processador = ProcessadorFiles()
    arr = processador.getFileAsArr("Arquivos/")
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

    teste = ProcessadorFiles()
    teste.limparFile(path + "/Cadastros")
    print("ok")
    print(path)


def TesteRemoverWhitespace():
    dir = Servicos.DiretorioManager.DiretorioManager()
    path = dir.GetDiretorioArquivos(os.getcwd())

    teste = ProcessadorFiles()
    teste.removerEspacosEmBranco(path + "/NomeBackup")


def TestePegarLinha():
    dir = Servicos.DiretorioManager.DiretorioManager()
    path = dir.GetDiretorioArquivos(os.getcwd())

    teste = ProcessadorFiles()
    msg = teste.getLinhaFileAsString(path + "/NomeBackup", 5)
    print(msg)

def TesteSubstituirLinha():
    dir = Servicos.DiretorioManager.DiretorioManager()
    path = dir.GetDiretorioArquivos(os.getcwd())

    teste = ProcessadorFiles()
    teste.substituirLinha(path + "/MatriculasIndexadas", 2, "msg")

#TesteLimparFile()

#TesteRemoverWhitespace()
#TestePegarLinha()
TesteSubstituirLinha()