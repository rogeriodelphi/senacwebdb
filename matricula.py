from conexao import ConexaoDB
import os

conexao = ConexaoDB().conectar()
cursor = conexao.cursor()


class Matricula:

    def listar_matriculas(self):

        sql = '''select m.id as matricula, a.nome as aluno, c.nome as curso, m.data_matricula as data_matricula
                from matricula as m left join aluno as a on m.aluno_id = a.id
                left join curso as c on m.curso_id = c.id;'''
        cursor.execute(sql)
        resultado = cursor.fetchall()

        os.system('cls' if os.name == 'nt' else 'clear')
        print('---------------------------')
        print('-- Lista das Matrículas----')
        print('---------------------------\n')
        for r in resultado:
            print('ID: ', r[0])
            print('Curso: ', r[1])
            print('Aluno: ', r[2])
            print('Data da Matrícula: ', r[3].strftime("%d/%m/%Y"))
            print('')

    def cadastrar_matricula(self):
        curso_id = int(input('\nDigite o Id do curso: '))
        aluno_id = int(input('Digite valor do curso: '))
        dados = (curso_id, aluno_id)
        try:
            sql = "insert into matricula (curso_id, aluno_id) values(%s, %s);"
            cursor.execute(sql, dados)
            conexao.commit()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("O matrícula foi realizada com sucesso!")
        except:
            print('Não foi possível cadastrar uma nova matrícula!')
