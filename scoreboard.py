#fazendo os imports necessarios
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        #pontuacao da esquerda
        self.pontE = 0
        #pontuacao da direita
        self.pontD = 0

    #metodo para atualizar a pontuacao
    def atualizarPont(self):
        #limpa a tela para nao ficar sobreposto
        self.clear()
        #move a tartaruga para a posicao que queremos
        self.goto(-150,200)
        #escreve na tela
        self.write(self.pontE, align="center", font=("Bahnschrift",'40','normal'))
        #move a tartaruga para a posicao que queremos
        self.goto(150,200)
        #escreve na tela
        self.write(self.pontD, align="center", font=("Bahnschrift",'40','normal'))

    #metodo para aumentar a pontuacao do esquerda
    def pontoEsq(self):
        self.pontE += 1                    

    #metodo para aumentar a pontuacao do direita
    def pontoDir(self):
        self.pontD += 1           