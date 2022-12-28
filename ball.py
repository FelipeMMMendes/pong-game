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
        #atributos auxiliares
        self.xMove = 10
        self.yMove = 10

    #metodo para mover a bola
    def mover(self):
        #Pega as coordenadas X e Y e soma elas
        novoX = self.xcor() + self.xMove
        novoY = self.ycor() + self.yMove
        #move a bola para as novas coordenadas
        self.goto(novoX,novoY)

    #metodo para inverter o valor do Y em caso de colisao
    def bounceY(self):
        self.yMove *= -1

    #metodo para inverter o valor do X em caso de colisao
    def bounceX(self):
        self.xMove *= -1    

        #metodo para fazer a bola voltar para a posicao original e inverter o rumo dela
    def resetarBola(self):
        self.goto(0,0)
        self.bounceX()
                          