

class CadastroDTO:
    def __init__(self, index, nome, matricula, curso, vontadeDeViver, time, animal, indexNextCurso = "*", indexNextAnimal = "*", indexNextTime = "*"):
        self.index = index
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.vontadeDeViver = vontadeDeViver
        self.time = time
        self.animalFavorito = animal
        self.indexNextCurso = indexNextCurso
        self.indexNextAnimal = indexNextAnimal
        self.indexNextTime = indexNextTime
