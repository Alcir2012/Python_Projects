import sqlite3 as lite

#criando a conexão

con = lite.connect('D:\\Python\\Python_Projects\\Personal_Budget\\dados.db')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categorias(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")


with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Receitas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, adiciona_em DATE, valor NUMERIC)")

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor NUMERIC) ")
