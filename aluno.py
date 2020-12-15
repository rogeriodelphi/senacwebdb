from conexao import ConexaoDB
import os

conexao = ConexaoDB().conectar()
cursor = conexao.cursor()


class Aluno:

    def listar_alunos(self):
        sql = 'select * from aluno order by nome'
        cursor.execute(sql)
        resultado = cursor.fetchall()

        os.system('cls' if os.name == 'nt' else 'clear')
        print('---------------------------')
        print('----- Lista dos Alunos ----')
        print('---------------------------\n')
        for r in resultado:
            print('ID: ', r[0])
            print('Nome: ', r[1])
            print('Data Nascimento: ', r[2].strftime("%d/%m/%Y"))
            print('CPF: ', r[3])
            print('')

    def cadastrar_aluno(self):
        nome = input('\nDigite o nome do aluno: ')
        nascimento = input(
            'Digite a data de nascimento do aluno(AAAA-MM-DD): ')
        cpf = input('Digite o cpf do aluno: ')
        try:
            dados = (nome, nascimento, cpf)
            sql = 'insert into aluno (nome, nascimento, cpf) values(%s, %s, %s);'
            cursor.execute(sql, dados)
            conexao.commit()
            os.system('cls' if os.name == 'nt' else 'clear')
            print('O aluno {} foi cadastrado com sucesso!'.format(nome))
        except:
            print('Não foi possível cadastrar um novo aluno!')
#        conexao.close()
