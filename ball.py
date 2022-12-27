#fazendo os imports necessarios
from turtle import Turtle

#a classe Ball herda da Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        #levanta a caneta para a bola nao desenhar por onde passa
        self.penup()
        #muda a forma para um circulo
        self.shape('circle')
        #muda a cor
        self.color('white')

    #metodo para mover a bola
    def mover(self):
        #Pega as coordenadas X e Y e soma elas
        novoX = self.xcor() + 10
        novoY = self.ycor() + 10
        self.goto(novoX,novoY)    