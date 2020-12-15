from conexao import ConexaoDB
import os

conexao = ConexaoDB().conectar()
cursor = conexao.cursor()


class Curso:

    def listar_cursos(self):
        sql = 'select * from curso order by nome'
        cursor.execute(sql)
        resultado = cursor.fetchall()

        os.system('cls' if os.name == 'nt' else 'clear')
        print('---------------------------')
        print('----- Lista dos Cursos ----')
        print('---------------------------\n')
        for r in resultado:
            print('ID: ', r[0])
            print('Nome: ', r[1])
            print('Valor: ', r[2])
            print('Descrição: ', r[3])
            print('')

    def cadastrar_curso(self):
        nome = input('\nDigite o nome do curso: ')
        valor = float(input('Digite valor do curso: '))
        descricao = input('Digite a descriçao do curso: ')
        dados = (nome, valor, descricao)
        try:
            sql = "insert into curso (nome, valor, descricao) values(%s, %s, %s);"
            cursor.execute(sql, dados)
            conexao.commit()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("O curso {} foi cadastrado com sucesso!".format(nome))
        except:
            print('Não foi possível cadastrar um novo curso!')
