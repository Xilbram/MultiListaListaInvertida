from Servicos.ProcessadorFiles import *
class DataSource:
    def __init__(self):
        self.nomes = None
        self.times = None
        self.cursos = None
        self.matriculas = None
        self.vontadeDeViver: int = None
        self.animalFavorito = None

    def preencherDataPool(self):
        self.nomes = ProcessFiles()