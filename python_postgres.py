import psycopg2

# Cria a conexão
conexao = psycopg2.connect(
    host = 'localhost',
    database = 'senacwebdb',
    user = 'senacwebuser',
    password = '123456',
)


# sql = 'select m.id, a.nome, m.data_matricula, c.nome from matricula as m left join aluno as a on m.aluno_id = a.id left join curso as c on m.curso_id = c.id;'

# cursor =  conexao.cursor()

# cursor.execute(sql)

# resultado = cursor.fetchall()

# for r in resultado:
#     print ('ID', r[0])
#     print ('Nome', r[1])
#     print ('Data Matrícula', r[2].strftime("%d/%m/%Y"))
#     print ('Curso', r[3])        

# conexao.close()    