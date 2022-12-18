class DiretorioManager():
    def getDiretorioFonte(self, pCwd) -> str:
        path = pCwd
        slashArr = []
        strAsArr = []

        for i in range(len(path)):
            strAsArr.append(path[i])
            if path[i] == "/":
                slashArr.append(i)

        newpath = ""
        for j in range(len(path) - slashArr[-1]):
            strAsArr.pop()

        for data in strAsArr:
            newpath += data

        return newpath

    def GetDiretorioArquivos(self, pCwd) -> str:
        newpath = pCwd + "/Arquivos"
        return newpath

    def getDiretorioArquivosCortado(self, pCwd) -> str:
        dirBase = self.getDiretorioFonte(pCwd)
        newpath = dirBase + "/Arquivos"

        return newpath
