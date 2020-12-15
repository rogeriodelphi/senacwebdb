import psycopg2


class ConexaoDB:

    def conectar(self):
        conexao = psycopg2.connect(
            host='localhost',
            database='senacwebdb',
            user='senacwebuser',
            password='123456'
        )
        return conexao
