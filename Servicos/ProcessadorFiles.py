from Arquivos import *


class ProcessadorFiles:

    def getFileContent(self, file) -> str:
        try:
            names_file = open(file, "r")
            msg = names_file.read()
            names_file.close()

            return msg

        except FileNotFoundError:
            return FileNotFoundError

        except IsADirectoryError:
            return IsADirectoryError

    def getLinhaFileAsString(self, file, numLinha) -> str:
        try:
            names_file = open(file, "r")
            lines = names_file.readlines()
            msg = lines[numLinha]
            names_file.close()

            return msg

        except FileNotFoundError:
            return FileNotFoundError

        except IsADirectoryError:
            return IsADirectoryError

    def removerEspacosEmBranco(self, file):
        try:
            names_file = open(file, "r")
            lines = names_file.readlines()
            msg = ""

            for line in lines:
                newline = line.replace(" ", "")
                msg += newline

            names_file.close()

            names_file = open(file, "w")
            names_file.write(msg)

        except FileNotFoundError:
            return FileNotFoundError

        except IsADirectoryError:
            return IsADirectoryError


    def inserirDataEmFile(self, file, data):
        try:
            names_file = open(file, "a")
            names_file.write(data)
            names_file.close()

        except FileNotFoundError:
            return FileNotFoundError

        except IsADirectoryError:
            return IsADirectoryError


    def getFileAsArr(self, file):
        try:
            names_file = open(file, "r")
            lines = names_file.readlines()
            arr = []
            for line in lines:
                line = line.replace("\n", "")
                arr.append(line)

            names_file.close()
            return arr

        except FileNotFoundError:
            return FileNotFoundError

        except IsADirectoryError:
            return IsADirectoryError

    def limparFile(self, file):
        try:
            names_file = open(file, "w")
            names_file.write("")
            names_file.close()


        except FileNotFoundError:
            return FileNotFoundError

        except IsADirectoryError:
            return IsADirectoryError


    def substituirLinha(self, pFile, pIndexLinha, pLinhaNova):
        try:
            names_file = open(pFile, "r")
            lines = names_file.readlines()
            lines[pIndexLinha] = pLinhaNova

            names_file = open(pFile, "w")
            names_file.writelines(lines)

            names_file.close()


        except FileNotFoundError:
            return FileNotFoundError

        except IsADirectoryError:
            return IsADirectoryError


