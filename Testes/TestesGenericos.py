import os

import Servicos.LimpadorDiretorios
from Servicos.ProcessadorFiles import *


def TesteProcessador():
    processador = ProcessFiles()
    arr = processador.returnFileAsArr("Arquivos/")
    for i in range(len(arr)):
        print(arr[i])
    print(arr)


def TesteFiles():
    teste = Servicos.LimpadorDiretorios.LimpadorDiretorio()
    ok = teste.GetDiretorioArquivos(os.getcwd())

    print(ok)






teste = TesteFiles()