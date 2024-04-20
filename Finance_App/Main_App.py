from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk


#cores
co0 = "#000000" #preto
co1 = "#FFFFFF" #branco
co2 = " #00FF00" #verde
co3 = "#001F3F" #azul 
co6 = "038cfc" #azul
co8 = "#263238" # + verde
co9 = "#808080"

#Criando janela

janela = Tk()
janela.title('Seu Financeiro')
janela.geometry('250x400')
janela.configure(background=co1)
janela.resizable(width=FALSE,height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

#Frames

frameCima = Frame(janela, width=300, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)
frameMeio = Frame(janela, width=300, height=100, bg=co1, relief="flat")
frameMeio.grid(row=1, column=0)
frameBaixo = Frame(janela, width=300, height=290, bg=co9, relief="flat")
frameBaixo.grid(row=2, column=0)

#Logo

app_label = Label(frameCima, text='Financeiro', compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 20'), bg=co1, fg=co9)
app_label.place(x=0, y=0)

#Inserindo imagem

app_image = Image.open('D:\Python\Projetos\Finance_App\projeto_orçamento.png')
app_image = app_image.resize((40,40))
app_image = ImageTk.PhotoImage (app_image)

app_logo = Label(frameCima, image=app_image, compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 20'), bg=co1, fg=co9)
app_logo.place(x=150, y=0)

app_linha = Label(frameCima,width=295,relief=FLAT, anchor=NW, font=('Verdana 1'), bg=co0, fg=co1)
app_linha.place(x=0, y=47)


#Funções 
def calcular():
    #renda total
    renda_mensal = float(e_valor.get())

    #Porcentagens
    obter_50_porcento = (50 / 100) * renda_mensal
    obter_20_porcento = (20 / 100) * renda_mensal
    obter_30_porcento = (30 / 100) * renda_mensal

    #Mostrando na tela
    necessidades_valores['text'] = ('R${:,.2f}'.format(obter_50_porcento))
    investimentos_valores['text'] = ('R${:,.2f}'.format(obter_20_porcento))
    lazeres_valores['text'] = ('R${:,.2f}'.format(obter_30_porcento))

#Frame de separação

app_label = Label(frameMeio, text='Qual seu salário mensal?', relief=FLAT, anchor=NW, font=('Ivy 10'), bg=co1, fg=co9)
app_label.place(x=7, y=15)

e_valor= Entry(frameMeio, width= 10, font= ('Ivy 14'),justify='center',relief='solid')
e_valor.place(x=10,y=40)

bttn_calcular = Button(frameMeio,command=calcular, text='Calcular'.upper(), overrelief=RIDGE, anchor=NW, font=('Ivy 9'), bg=co1, fg=co0)
bttn_calcular.place(x=150, y=40)


#Frame Baixo

app_label = Label(frameBaixo, text='Segue a dica de orçamento 50/20/30', relief=FLAT, width=35, anchor=NW, font=('Verdana 9'), bg=co3, fg=co1)
app_label.place(x=0, y=0)

#Necessidades
necessidades = Label(frameBaixo, text='Necessidades', relief=FLAT, width=35, anchor=NW, font=('Verdana 9'), bg=co9, fg=co0)
necessidades.place(x=10, y=40)

necessidades_valores = Label(frameBaixo, relief=FLAT, width=22, anchor=NW, font=('Verdana 11'), bg=co1, fg=co0)
necessidades_valores.place(x=10, y=75)

#Investimentos
investimentos = Label(frameBaixo, text='Investimentos', relief=FLAT, width=35, anchor=NW, font=('Verdana 9'), bg=co9, fg=co0)
investimentos.place(x=10, y=115)

investimentos_valores = Label(frameBaixo, relief=FLAT, width=22, anchor=NW, font=('Verdana 11'), bg=co1, fg=co0)
investimentos_valores.place(x=10, y=145)


#Lazeres
lazeres = Label(frameBaixo, text='Lazeres', relief=FLAT, width=35, anchor=NW, font=('Verdana 9'), bg=co9, fg=co0)
lazeres.place(x=10, y=185)

lazeres_valores = Label(frameBaixo, relief=FLAT, width=22, anchor=NW, font=('Verdana 11'), bg=co1, fg=co0)
lazeres_valores.place(x=10, y=215)

janela.mainloop()