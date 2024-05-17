import sqlite3 as lite
con = lite.connect('D:\\Python\\Python_Projects\\Personal_Budget\\dados.db')

def ver_gastos():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)

    return lista_itens

print(ver_gastos())

'''def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)

    return lista_itens

print(ver_receitas())


def deleta_receitas():
    with con:
        cur = con.cursor()
        # Use a cláusula IN para excluir várias linhas com base em IDs específicos
        cur.execute("DELETE FROM Receitas")

print(deleta_receitas())

def deleta_gastos():
    with con:
        cur = con.cursor()
        # Use a cláusula IN para excluir várias linhas com base em IDs específicos
        cur.execute("DELETE FROM Gastos")

print(deleta_gastos())'''

'''with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Nova_Receitas (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, adiciona_em DATE, valor NUMERIC)")
'''

'''with con:
    cur = con.cursor()
    cur.execute("DROP TABLE Receitas")
    cur.execute("ALTER TABLE Nova_Receitas RENAME TO Receitas")'''
