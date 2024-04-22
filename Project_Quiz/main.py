import tkinter as Tk
from tkinter  import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

#Ler excel
df =  pd.read_excel("D:\\Python\\Python_Projects\\Project_Quiz\\Questions.xlsx")

#Pega as perguntas
questions = df.sample(n=10).values.tolist()


#Variaveis globais
score = 0
current_question = 0

#função para exibir próxima pergunta

def display_question():
    question,option1,option2,option3,option4,answer = questions[current_question]
    question_label.config(text=question)
    option1_button.config(text=option1, state= Tk.NORMAL)
    option2_button.config(text=option2, state= Tk.NORMAL)
    option3_button.config(text=option3, state= Tk.NORMAL)
    option4_button.config(text=option4, state= Tk.NORMAL)

#Cores e janela
janela = Tk.Tk()
janela.title ('Quiz')
janela.geometry('400x450')
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
button_text_color = "#FFFFFF"


janela.config(bg=background_color)
janela.option_add('*Font','Arial')

#Icone da tela
app_icon = PhotoImage(file="D:\\Python\\Python_Projects\\Project_Quiz\\logo.png")
app_label = Tk.Label(janela, image=app_icon, bg= background_color)
app_label.pack(pady=10)


#Componentes
question_label = Tk.Label(janela, text="",wraplength=380, bg=background_color,
                           fg=text_color, font= ("Arial",12,"bold"))
question_label.pack(pady=20)

correct_answer = Tk.IntVar()

#Buttons
option1_button = Tk.Button(janela, text="", width=30, bg=button_color,
                            fg=button_text_color, state= Tk.DISABLED, font= ("Arial", 10, "bold"))
option1_button.pack(pady=10)

option2_button = Tk.Button(janela, text="", width=30, bg=button_color,
                            fg=button_text_color, state= Tk.DISABLED, font= ("Arial", 10, "bold"))
option2_button.pack(pady=10)

option3_button = Tk.Button(janela, text="", width=30, bg=button_color,
                            fg=button_text_color, state= Tk.DISABLED, font= ("Arial", 10, "bold"))
option3_button.pack(pady=10)

option4_button = Tk.Button(janela, text="", width=30, bg=button_color,
                            fg=button_text_color, state= Tk.DISABLED, font= ("Arial", 10, "bold"))
option4_button.pack(pady=10)

playagain_button = Tk.Button(janela, text="Jogar novamente", width=30, bg=button_color,
                            fg=button_text_color, font= ("Arial", 10, "bold"))
playagain_button.pack(pady=10)



display_question() 
janela.mainloop()