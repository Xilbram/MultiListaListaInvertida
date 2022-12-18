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
            Pressione 2 para salvar os cadastros gerados em memória secundária
            Pressione 3 para buscar cadastros através de uma das colunas
            Pressione 4 para buscar cadastros através de multiplas colunas
            Pressione 5 para inserir um cadastro
            Pressione 6 para remover um cadastro       
            Pressione 7 para exibir todos Cadastros salvos em memória secundária
            Pressione 8 para limpar todos os dados em memória secundária
            Pressione 9 para sair do programa
            Valor: 
            ''')

            if usr_input == "1":
                quantidade = input("Digite a quantidade de cadastros que você deseja gerar: ")

                try:
                    quantidade = int(quantidade)
                    self.__database.preencherDataBase(quantidade)

                    self.__database.mostrarTodosDados()

                except ValueError:
                    print("Por favor, insira um número")

            if usr_input == "2":
                self.__database.salvarEIndexarDados()


            if usr_input == "8":
                resp = input("Tem certeza? [S/N]")

                if resp.upper() == "S":
                    self.__database.limparDataBaseMemPrincipal()
                    self.__database.limparDataBaseMemSecundaria()


print(os.getcwd())
var = SistemaMatriculas()
var.Iniciar()



