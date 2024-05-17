import sqlite3 as lite
from tkinter import messagebox
import pandas as pd

con = lite.connect('D:\\Python\\Python_Projects\\Personal_Budget\\dados.db')

def Inserindo_Categoria(i):
    if i and i[0]:
        with con:
            cur = con.cursor()
            query = ("INSERT INTO Categorias (nome) VALUES (?)")
            cur.execute(query,i)

Inserindo_Categoria([""])

def deleta_categorias():
    with con:
        cur = con.cursor()
        cur.execute("DELETE FROM Categorias")
        con.commit()


def Inserindo_Receita(i):
    with con:
        cur = con.cursor()
        query = ("INSERT INTO Receitas (nome, adiciona_em, valor) VALUES (?,?,?)")
        cur.execute(query,i)    
def Gastos(i):
    with con:
        cur = con.cursor()
        query = ("INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)")
        cur.execute(query, i) 

#Funções para deletar
def Deletar_Receitas(i):
    with con:
        cur = con.cursor()
        query= "DELETE FROM Receitas WHERE id = ?"
        cur.execute(query,i)

def Deletar_Gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos where id = ?"
        cur.execute(query,i)

#Função Vendo categorias

def ver_categorias():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categorias")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

#Vendo receitas
def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)

    return lista_itens

#vendo gastos

def ver_gastos():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

def tabela():
    gastos = ver_gastos()
    receitas = ver_receitas()
    tabela_lista = []
    for i in gastos:
        tabela_lista.append(i)
    for i in receitas:
        tabela_lista.append(i)

    return tabela_lista

#função grafico de barra
def bar_valores():
    receitas = ver_receitas()
    receitas_lista =[]

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    despesa = ver_gastos()
    despesas_lista =[]

    for i in despesa:
        despesas_lista.append(i[3])

    despesa_total = sum(despesas_lista)

    #Calculos da renda x despesa
    saldo_total = receita_total - despesa_total

    return[receita_total,despesa_total,saldo_total]

def grafico_pizza():
    Gastos=ver_gastos()
    tabela_lista = []

    for i in Gastos:
        tabela_lista.append(i)
    
    dataframe = pd.DataFrame(tabela_lista,columns= ['id','categoria','retirado_em','valor'])

    dataframe = dataframe.groupby('categoria')['valor'].sum()

    lista_quantias = dataframe.values.tolist()
    lista_categorias = []
    for i in dataframe.index:
        lista_categorias.append(i)

    return(lista_categorias,lista_quantias)

def barra_porcentagem():
    receitas = ver_receitas()
    receitas_lista = []

    for i in receitas:
        receitas_lista.append(i[3])

    receita_total = sum(receitas_lista)

    Gastos = ver_gastos()
    gastos_lista = []
    
    for i in Gastos:
        gastos_lista.append(i[3])
    gastos_total = sum(gastos_lista)

    saldo_total = ((receita_total - gastos_total) / receita_total) * 100

    return [saldo_total]