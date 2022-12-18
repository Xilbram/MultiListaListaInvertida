class ListaInvertida:
    def __init__(self):
        self.__diretorio = {}
    def inserir(self, pData, pIndex):
        pData = pData[1:]
        pData = pData.lower()
        if pData in self.__diretorio.keys():
            self.__diretorio[pData].append(pIndex)
            return


        self.__diretorio[pData] = [pIndex]

    def getIndexados(self):
        return self.__diretorio








