import os

from Servicos import *
from Servicos.DataBase import *
from ArquivosMemoriaPrincipal.Multilista import *

class SistemaMatriculas:
    def __init__(self):
        self.__database = DataBase()
    def Iniciar(self):
        print("Bem vindo ao sistema de Cadastros!")
        while True:
            usr_input = input('''
            Pressione 1 para gerar novos cadastros e exibi-los
            Pressione 2 para buscar cadastros através de uma das colunas
            Pressione 3 para buscar cadastros através de multiplas colunas
            Pressione 4 para inserir um cadastro
            Pressione 5 para remover um cadastro       
            Pressione 6 para exibir todos cadastros em memória principal
            Pressione 7 para exibir todos cadastros salvos em memória secundária
            Pressione 8 para limpar todos os dados em memória secundária
            Pressione 9 para sair do programa
            Valor: 
            ''')

            if usr_input == "1":
                quantidade = input("Digite a quantidade de cadastros que você deseja gerar: ")

                try:
                    quantidade = int(quantidade)
                    self.__database.preencherDataBase(quantidade)

                    self.__database.exibirDadosMemoriaPrincipal()

                    self.__database.salvarDados()
                    self.__database.indexarDados()

                except ValueError:
                    print("Por favor, insira um número")

            if usr_input == "2":
                escolha_coluna = input('''
                Colunas disponiveis para realizar buscar:
                1 - Animais
                2 - Times
                3 - Cursos
                4 - Vontade de viver
                ''')

                self.__database.getKeysMultilista(escolha_coluna)

                escolha_parametro = input("Escolha um dos parametros acima: ")
                self.__database.getIndexadosPorMultilista(escolha_coluna, escolha_parametro)




            if usr_input == "5":
                self.__database.exibirDadosMemoriaPrincipal()





            if usr_input == "8":
                resp = input("Tem certeza? [S/N]")

                if resp.upper() == "S":
                    self.__database.limparDataBaseMemPrincipal()
                    self.__database.limparDataBaseMemSecundaria()


print(os.getcwd())
var = SistemaMatriculas()
var.Iniciar()



