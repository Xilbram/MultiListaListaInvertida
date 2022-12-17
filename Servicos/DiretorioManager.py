class DiretorioManager():
    def getDiretorioFonte(self, cwd) -> str:
        path = cwd
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
        dirBase = self.getDiretorioFonte(pCwd)
        newpath = dirBase + "/Arquivos"

        return newpath
