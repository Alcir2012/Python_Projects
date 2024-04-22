import pandas as pd

import openpyxl

questions = [
    ["Qual é a capital da França?", "Paris", "Londres", "Berlim", "Roma", 1],
    ["Qual é o resultado de 8 + 5?", "12", "13", "15", "18", 2],
    ["Quem pintou a Mona Lisa?", "Picasso", "Da Vinci", "Van Gogh", "Warhol", 2],
    ["Quanto é 6 multiplicado por 7?", "36", "42", "48", "54", 2],
    ["Qual é o maior planeta do sistema solar?", "Marte", "Saturno", "Júpiter", "Vênus", 3],
    ["Quem escreveu a obra 'Dom Quixote'?", "Machado de Assis", "Miguel de Cervantes", "Jorge Luis Borges", "Gabriel García Márquez", 2],
    ["Qual é a fórmula química da água?", "H2O", "CO2", "NaCl", "CH4", 1],
    ["Quem foi o primeiro presidente dos Estados Unidos?", "George Washington", "Abraham Lincoln", "Thomas Jefferson", "John F. Kennedy", 1],
    ["Qual é o resultado de 4 ao cubo?", "16", "32", "64", "128", 3],
    ["Qual é a capital da Rússia?", "Moscou", "São Petersburgo", "Kiev", "Varsóvia", 1],
    ["Quem descobriu a teoria da relatividade?", "Isaac Newton", "Galileu Galilei", "Albert Einstein", "Nikola Tesla", 3],
    ["Qual é o símbolo químico do ouro?", "Au", "Ag", "Cu", "Fe", 1],
    ["Quem foi o autor da obra 'Romeu e Julieta'?", "William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen", 1],
    ["Qual é a capital do Brasil?", "Rio de Janeiro", "Brasília", "São Paulo", "Salvador", 2],
    ["Qual é o resultado de 9 dividido por 3?", "1", "2", "3", "4", 3],
    ["Quem pintou a obra 'A Noite Estrelada'?", "Leonardo da Vinci", "Michelangelo", "Salvador Dalí", "Vincent van Gogh", 4],
    ["Qual é o maior oceano do mundo?", "Atlântico", "Índico", "Pacífico", "Ártico", 3],
    ["Qual é o resultado de 2 elevado a 8?", "8", "16", "64", "256", 4],
    ["Quem escreveu a obra '1984'?", "George Orwell", "Aldous Huxley", "Ernest Hemingway", "F. Scott Fitzgerald", 1],
    ["Qual é o resultado de 15 menos 7?", "5", "6", "7", "8", 3],
    ["Quem foi o pintor do quadro 'A Última Ceia'?", "Pablo Picasso", "Salvador Dalí", "Michelangelo", "Leonardo da Vinci", 4]
]

# criando DataFrame Pandas

df = pd.DataFrame(questions, columns=['Peruntas','Opção 1', 'Opção 2', 'Opção 3', 'Opção 4',"respostas"])

#Salvando em excel
df.to_excel("D:\\Python\\Python_Projects\\Project_Quiz\\Questions.xlsx", index =False)

print('Perguntas inseridas com sucesso!')

