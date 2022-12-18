import os
import sys

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
                self.__database.indexarDados()
                escolha_coluna = input('''
                Colunas disponiveis para realizar buscar:
                1 - Animais
                2 - Cursos
                3 - Times
                4 - Vontade de viver
                ''')

                self.__database.getKeysMultilista(escolha_coluna)

                escolha_parametro = input("Escolha um dos parametros acima: ")
                self.__database.getIndexadosPorMultilista(escolha_coluna, escolha_parametro)

            if usr_input == "3":
                self.__database.indexarDados()
                escolha_primeira_coluna =   input('''
                                Colunas disponiveis para realizar buscar:
                                1 - Animais
                                2 - Cursos
                                3 - Times
                                4 - Vontade de viver
                                ''')

                self.__database.getKeysMultilista(escolha_primeira_coluna)
                escolha_parametro_primeira = input("Escolha um dos parametros acima: ")

                escolha_segunda_coluna = input('''
                Colunas disponiveis para realizar buscar:
                1 - Animais
                2 - Cursos
                3 - Times
                4 - Vontade de viver
                ''')

                self.__database.getKeysMultilista(escolha_segunda_coluna)
                escolha_parametro_segunda = input("Escolha um dos parametros acima: ")

                self.__database.getResultadosPorDuasColunas(escolha_primeira_coluna,escolha_parametro_primeira,
                                                            escolha_segunda_coluna,escolha_parametro_segunda)

            if usr_input == "4":
                nome_input = input("Insira o nome ")
                matricula_input = input("Insira uma matricula (8 digitos)")
                if(len(matricula_input) != 8):
                    matricula_input = input("Insira outro valor para a matricula, por favor")
                curso_input = input("Insira um curso ")
                vontade_input = input("Insira a vontade de viver do seu cadastro (0 a 100)")
                if(int(vontade_input) > 100) or (int(vontade_input) < 0):
                    vontade_input = input("Insira outro valor para a vontade de viver, por favor ")
                time_input = input("Insira o time ")
                animal_input = input("Insira o animal favorito ")

                data = []
                data.append(nome_input)
                data.append(matricula_input)
                data.append(curso_input.upper())
                data.append(vontade_input)
                data.append(time_input.capitalize())
                data.append(animal_input.capitalize())
                self.__database.inserirCadastro(data)

            if usr_input == "5":
                remover = input("Insira o index da linha que você deseja remover ")
                self.__database.removerCadastro(int(remover))

            if usr_input == "6":
                self.__database.exibirDadosMemoriaPrincipal()

            if usr_input == "7":
                self.__database.exibirDadosMemoriaSecundaria()





            if usr_input == "8":
                resp = input("Tem certeza? [S/N]")

                if resp.upper() == "S":
                    self.__database.limparDataBaseMemPrincipal()
                    self.__database.limparDataBaseMemSecundaria()

            if usr_input == "9":
                sys.exit()


print(os.getcwd())
var = SistemaMatriculas()
var.Iniciar()



