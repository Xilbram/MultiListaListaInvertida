from Servicos import *
from Servicos.DataBase import *
from ArquivosMemoriaPrincipal.Multilista import *

class SistemaMatriculas:
    def __init__(self):
        self.database = DataBase()
        self.multilistas = MultilistaAnimalFavorito()
    def Iniciar(self):
        self.database.preencherDataBase()
        self.database.salvarDados()


