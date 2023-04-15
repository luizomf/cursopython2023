# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import dotenv
import pymysql

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(  # type: ignore
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # type: ignore
    connection.commit()

    # Começo a manipular dados a partir daqui

    # Inserindo um valor usando placeholder e um iterável
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('Luiz', 18)
        result = cursor.execute(sql, data)  # type: ignore
        # print(sql, data)
        # print(result)
    connection.commit()

    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = {
            "age": 37,
            "name": "Le",
        }
        result = cursor.execute(sql, data2)  # type: ignore
        # print(sql)
        # print(data2)
        # print(result)
    connection.commit()

    # Inserindo vários valores usando placeholder e um tupla de dicionários
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "Sah", "age": 33, },
            {"name": "Júlia", "age": 74, },
            {"name": "Rose", "age": 53, },
        )
        result = cursor.executemany(sql, data3)  # type: ignore
        # print(sql)
        # print(data3)
        # print(result)
    connection.commit()

    # Inserindo vários valores usando placeholder e um tupla de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("Siri", 22, ),
            ("Helena", 15, ),
            ("Luiz", 18, ),
        )
        result = cursor.executemany(sql, data4)  # type: ignore
        # print(sql)
        # print(data4)
        # print(result)
    connection.commit()

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        menor_id = int(input('Digite o menor id: '))
        maior_id = int(input('Digite o maior id: '))

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s  '
        )

        cursor.execute(sql, (menor_id, maior_id))  # type: ignore
        print(cursor.mogrify(sql, (menor_id, maior_id)))  # type: ignore
        data5 = cursor.fetchall()  # type: ignore

        for row in data5:
            print(row)
