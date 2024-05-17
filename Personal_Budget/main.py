import tkinter as tk
from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from tkinter.ttk import Progressbar
from tkcalendar import Calendar, DateEntry
from datetime import date
from tkinter import messagebox
from view import *

#Cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  
co3 = "#38576b"  
co4 = "#403d3d"   # uso pra letras
co5 = "#e06636"   
co6 = "#038cfc"   
co7 = "#3fbfb9"   
co8 = "#263238"   
co9 = "#e9edf5"   
colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

#janela

janela = Tk()
janela.title('Personal Budget')
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width='FALSE',height='FALSE')

style= ttk.Style(janela)
style.theme_use("clam")

#Criando frames
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief='flat')
frameCima.grid(row=0,column=0)


frameMeio = Frame(janela, width=1043, height=361, bg=co1,pady=20,relief='raised')
frameMeio.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief='flat')
frameBaixo.grid(row=2,column=0,pady=0,padx=10,sticky=NSEW)

frame_gra_pie = Frame(frameMeio, width=580, height=250, bg=co2)
frame_gra_pie.place(x=415, y=5)

#incluindo logo

img = Image.open('D:\\Python\\Python_Projects\\Personal_Budget\\logo.png')
img = img.resize((45,45))
img = ImageTk.PhotoImage(img)

logo = Label(frameCima,image=img,text='Contas x Recebimentos', compound=LEFT,width=900, padx=5, relief= RAISED, anchor=NW, font=('Ivy 20 bold'), bg=co1, fg=co4)
logo.place(x=0,y=0)

#Função insere categoria
global tree

def insere_Categoria():
    nome_categoria = entry_Ct_novoRecebimento.get()
    lista_insere_Ct = [nome_categoria]

    for i in lista_insere_Ct:
        if i == '':
            messagebox.showerror('Erro','nenhuma categoria foi preenchida')
            return
    Inserindo_Categoria(lista_insere_Ct)
    messagebox.showinfo('Sucesso','Dados inseridos com sucesso')
    #limpando os campos
    entry_Ct_novoRecebimento.delete(0,END)

    #Atualizando os valores da categoria
    categoria_funcao = ver_categorias()
    categoria = []

    for i in categoria_funcao:
        categoria.append(i)

    #atualizando lista de categorias
    combo_categoria_Despesa['values'] = categoria
def insere_Receitas():
    nome = 'Receitas'
    data = calendario_NovosRecebimentos.get()
    valor = entry_valor_novoRecebimento.get()
    
    # Verifica se algum campo está vazio
    if nome == '' or data == '' or valor == '':
        messagebox.showerror('Erro', 'Preencha todos os campos')
        return
    
    # Verifica se o valor é numérico
    try:
        valor = float(valor)
    except ValueError:
        messagebox.showerror('Erro', 'Valor inválido')
        return

    lista_inserir = [nome, data, valor]
    
    # Insere os dados no banco de dados
    Inserindo_Receita(lista_inserir)
    
    messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso')

    # Limpa os campos após a inserção
    calendario_NovosRecebimentos.delete(0, END)
    entry_valor_novoRecebimento.delete(0, END)

    
    #Atualizando graficos
    ver_receitas()
    porcentagem()
    grafico_Bar()
    grafico_pie()
    total_Renda()
    mostrar_Tabela()
    bar_valores()

def insere_Despesas():
    categoria = combo_categoria_Despesa.get()
    data = calendario_despesa.get()
    valor = entry_valor_despesa.get()
    lista_despesas = [categoria,data,valor]
    for i in lista_despesas:
        if i == '':
            messagebox.showerror('Erro','Preencha os campos')
            return
    Gastos(lista_despesas)
    messagebox.showinfo('Sucesso','Dados inseridos com sucesso')

    combo_categoria_Despesa.delete(0,END)
    calendario_despesa.delete(0,END)
    entry_valor_despesa.delete(0,END)

    ver_receitas()
    porcentagem()
    grafico_Bar()
    grafico_pie()
    mostrar_Tabela()
    bar_valores()

def deletar_acoes():
    try:
        tree_view_dados = tree.focus()
        tree_view_dicionario = tree.item(tree_view_dados)
        tree_view_lista = tree_view_dicionario['values']
        valor = tree_view_lista[0]
        categoria = tree_view_lista[1]

        if categoria == combo_categoria_Despesa.get():
            Deletar_Gastos([valor])
            messagebox.showinfo('Sucesso','Dados de gastos deletados com sucesso')

            #Atualizando dados
            ver_receitas()
            ver_gastos()
            porcentagem()
            grafico_Bar()
            grafico_pie()
            total_Renda()
            mostrar_Tabela()
        else:
            Deletar_Receitas([valor])
            messagebox.showinfo('Sucesso','Os dados foram deletados com sucesso')

            #Atualizando dados
            ver_receitas()
            porcentagem()
            grafico_Bar()
            grafico_pie()
            total_Renda()
            mostrar_Tabela()
    except IndexError:
        messagebox.showerror('Erro','Dados não foram selecionados')

#Porcentagem
def porcentagem():
    tit_Porcentagem = Label(frameMeio, text='Porcentagem de saldo restante',height=1,anchor=NW, font=('Verdana 12'),bg=co1,fg=co4)
    tit_Porcentagem.place(x=7,y=5)

    style =ttk.Style()
    style.theme_use("default")
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar")

    barprogress = Progressbar(frameMeio,length=180,style='black.Horizontal.TProgressbar')
    barprogress.place(x=10,y=35)
    barprogress['value'] = barra_porcentagem()[0]

    valor = barra_porcentagem()[0]

    value_BarProgress = Label(frameMeio,text='{:,.2f}%'.format(valor),anchor=NW,font='Verdana 12',bg=co1,fg=co4)
    value_BarProgress.place(x=200, y=33)
    

def grafico_Bar():
    lista_categorias = ['Renda', 'Despesa', 'Saldo']
    lista_valores = bar_valores()

    #faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)
    #create a list to collect the plt.patches data

    c = 0
    #set individual bar lables using above list
    for i in ax.patches:
        #get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    ax.set_xticklabels(lista_categorias,fontsize=16)


    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)

#Funções do resumo

def total_Renda():
    valor = bar_valores()
    tit_linha= Label(frameMeio, text='', width=215, height=1,font=('Arial 1'), anchor=NW,bg='#545454')
    tit_linha.place(x=309, y=52)

    tit_renda= Label(frameMeio, text='Resumo de renda total'.upper(),font=('Verdana 12'), anchor=NW,bg=co1,fg=co4)
    tit_renda.place(x=309, y=35)

    tit_values= Label(frameMeio, text='R$ {:,.2f}'.format(valor[0]),font=('Arial 17'), anchor=NW,bg=co1,fg=co4)
    tit_values.place(x=309, y=65)

    tit_linha2= Label(frameMeio, text='', width=215, height=1,font=('Arial 1'), anchor=NW,bg='#545454')
    tit_linha2.place(x=309, y=130)

    tit_despesa= Label(frameMeio, text='Resumo de despesa total'.upper(),font=('Verdana 12'), anchor=NW,bg=co1,fg=co4)
    tit_despesa.place(x=309, y=113)

    tit_valuesDespesa= Label(frameMeio, text='R$ {:,.2f}'.format(valor[1]),font=('Arial 17'), anchor=NW,bg=co1,fg=co4)
    tit_valuesDespesa.place(x=309, y=145)

    tit_linha3= Label(frameMeio, text='', width=215, height=1,font=('Arial 1'), anchor=NW,bg='#545454')
    tit_linha3.place(x=309, y=205)

    tit_saldoRestante= Label(frameMeio, text='Saldo Restante            '.upper(),font=('Verdana 12'), anchor=NW,bg=co1,fg=co4)
    tit_saldoRestante.place(x=309, y=188)

    tit_valuesRestante= Label(frameMeio, text='R$ {:,.2f}'.format(valor[2]),font=('Arial 17'), anchor=NW,bg=co1,fg=co4)
    tit_valuesRestante.place(x=309, y=215)

#funcao grafico pie
def grafico_pie():
    #faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = grafico_pizza()[1]
    lista_categorias = grafico_pizza()[0]

    #only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90,pctdistance=0.55)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=0,column=0)
    
grafico_pie()
grafico_Bar()
porcentagem()
total_Renda()
bar_valores()

#Frame da Renda
frame_Renda = Frame(frameBaixo,width=300, height=250, bg=co1)
frame_Renda.grid(row=0,column=0)

frame_Operacoes = Frame(frameBaixo,width=220, height=250, bg=co1)
frame_Operacoes.grid(row=0,column=1, padx=5)

frame_Config = Frame(frameBaixo,width=300, height=250, bg=co1)
frame_Config.grid(row=0,column=2,padx=5)

#Titulo da tabela de renda

Tit_NameTabela = Label(frameMeio,text='Tabela de ganhos e gastos', anchor=NW,font='Verdana 12',bg=co1,fg=co4)
Tit_NameTabela.place(x=5,y=309)

def mostrar_Tabela():

    #creating a treeview with dual scrollbars
    tabela_head = ['#Id','Categoria','Data','Valor']

    lista_itens = tabela()
    
    global tree

    tree = ttk.Treeview(frame_Renda, selectmode="extended",columns=tabela_head, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_Renda, orient="vertical", command=tree.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_Renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

mostrar_Tabela()

#Configurações de despesas
descricao_despesa = Label(frame_Operacoes,text="Insira novas despesas", anchor=NW,font='Verdana 10 bold',bg=co1,fg=co4)
descricao_despesa.place(x=10,y=10)

Categorias_info = Label(frame_Operacoes,text="Categoria", anchor=NW, font='Ivy 10',bg=co1,fg=co4)
Categorias_info.place(x=10,y=40)

#Coletando categorias
categoria_funcao = ver_categorias()
categoria = []

for i in categoria_funcao:
    categoria.append(i[1])

combo_categoria_Despesa = ttk.Combobox(frame_Operacoes, font='Ivy 10 bold', width=10)
combo_categoria_Despesa['values'] = categoria
combo_categoria_Despesa.place(x=100,y=41)

descricao_despesa_datas= Label(frame_Operacoes,text="Data", anchor=NW,font='Ivy 10',bg=co1,fg=co4)
descricao_despesa.place(x=10,y=10)

calendario_despesa = DateEntry(frame_Operacoes,width=12,background='darkblue',foreground='white',borderwidth=2,year=2024)
calendario_despesa.place(x=100,y=71)

#valores
valor_despesa= Label(frame_Operacoes,text="Valor total", anchor=NW,font='Ivy 10',bg=co1,fg=co4)
valor_despesa.place(x=10,y=100)

entry_valor_despesa=Entry(frame_Operacoes,width=14,justify='left', relief='solid')
entry_valor_despesa.place(x=100,y=101)

#botão de inserir
img_add = Image.open('D:\\Python\\Python_Projects\\Personal_Budget\\logo_add.png')
img_add = img_add.resize((17,17))
img_add = ImageTk.PhotoImage(img_add)

bttn_inserir_despesa = Button(frame_Operacoes,command=insere_Despesas,image=img_add,text='Adicionar'.upper(), compound=LEFT,width=80, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief='ridge')
bttn_inserir_despesa.place(x=100,y=126)

#botão de exclusão
Tit_exlusao = Label(frame_Operacoes,text='Exluir ação', anchor=NW,compound=LEFT,font=('Ivy 10'),bg=co1,fg=co0) 
Tit_exlusao.place(x=10,y=180)

#Configurações de despesas

img_del = Image.open('D:\\Python\\Python_Projects\\Personal_Budget\\logo_delete_action.png')
img_del = img_del.resize((17,17))
img_del = ImageTk.PhotoImage(img_del)

bttn_excluir_acao = Button(frame_Operacoes,command=deletar_acoes,image=img_del,text='Exluir'.upper(), compound=LEFT,width=80, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief='ridge')
bttn_excluir_acao.place(x=100,y=180)

#Inserir novas receitas
tit_NovasRecebimentos = Label(frame_Config,text="Insira novos recebimentos", anchor=NW,font='Verdana 10 bold',bg=co1,fg=co4)
tit_NovasRecebimentos.place(x=10,y=10)
#Calendario
Data_NovosRecebimentos= Label(frame_Config,text="Data", anchor=NW,font='Ivy 10',bg=co1,fg=co4)
Data_NovosRecebimentos.place(x=10,y=40)

calendario_NovosRecebimentos = DateEntry(frame_Config,width=12,backgroud='darkblue',foreground='white',borderwidth=2,year=2024)
calendario_NovosRecebimentos.place(x=80,y=43)
#Valores
Valor_NovosRecebimentos= Label(frame_Config,text="Valor", anchor=NW,font='Ivy 10',bg=co1,fg=co4)
Valor_NovosRecebimentos.place(x=10,y=100)

entry_valor_novoRecebimento =Entry(frame_Config,width=14,justify='left', relief='solid')
entry_valor_novoRecebimento.place(x=80,y=100)

#botão adicionar novo recebimento

bttn_inserir_novoRecebimento = Button(frame_Config,command=insere_Receitas,image=img_add,text='Adicionar'.upper(), compound=LEFT,width=80, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief='ridge')
bttn_inserir_novoRecebimento.place(x=80,y=127)

#categoria de novos recebimentos
Categorias_NovosRecebimentos = Label(frame_Config,text="Categoria", anchor=NW, font='Ivy 10',bg=co1,fg=co4)
Categorias_NovosRecebimentos.place(x=10,y=180)

#Novas categorias entry
entry_Ct_novoRecebimento=Entry(frame_Config,width=14,justify='left', relief='solid')
entry_Ct_novoRecebimento.place(x=80,y=180)

#Classificando corretamente o botão de add categoria
tit_NovaCategoria = Label(frame_Config,text="Nova categoria para despesa", anchor=NW,font='Verdana 7 bold',bg=co1,fg=co4)
tit_NovaCategoria.place(x=10,y=160)
#Adiciona categoria
img_add_Ct = Image.open('D:\\Python\\Python_Projects\\Personal_Budget\\logo_add.png')
img_add_Ct = img_add_Ct.resize((17,17))
img_add_Ct = ImageTk.PhotoImage(img_add_Ct)

bttn_inserir_novaCt = Button(frame_Config,command=insere_Categoria,image=img_add_Ct,text='Adicionar'.upper(), compound=LEFT,width=80, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief='ridge')
bttn_inserir_novaCt.place(x=80,y=208)

#Botão exlcuir categorias
bttn_excluir_categorias = Button(frame_Config,command=deleta_categorias,image=img_del,text='Del CT'.upper(), compound=LEFT,width=50, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief='ridge')
bttn_excluir_categorias.place(x=10,y=208)

janela.mainloop()