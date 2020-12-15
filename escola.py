from aluno import Aluno
from curso import Curso
from matricula import Matricula

aluno = Aluno()
curso = Curso()
matricula = Matricula()

print('SISESCOLA - Sistema Administrativo Escolar\n\n')
print(('Menu de Opções\n'
       '1 - Listar Alunos\n'
       '2 - Cadastrar Aluno\n'
       '3 - Listar Cursos\n'
       '4 - Cadastrar Curso\n'
       '5 - Listar Matrículas\n'
       '6 - Cadastrar Matrícula\n'
       '7 - Sair\n'
       ))
opt = int(input('Digite a opção desejada: '))


if opt == 1:
    aluno.listar_alunos()

elif opt == 2:
    aluno.cadastrar_aluno()

elif opt == 3:
    curso.listar_cursos()

elif opt == 4:
    curso.cadastrar_curso()

elif opt == 5:
    matricula.listar_matriculas()

elif opt == 6:
    matricula.cadastrar_matricula()

else:
    conecta.close()
