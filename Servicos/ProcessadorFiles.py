from Arquivos import *


class ProcessFiles:
    def returnFileAsArr(self, file):
        try:
            names_file = open(file, "r")
            lines = names_file.readlines()
            arr = []
            for line in lines:
                line = line.replace("\n", "")
                arr.append(line)

            return arr

        except FileNotFoundError:
            return "File not found"




processador = ProcessFiles()
arr = processador.returnFileAsArr("Arquivos/err")
print(len(arr))