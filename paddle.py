#fazendo os imports necessarios
from turtle import Turtle

#variaveis flag para auxiliar na configuracao visual e posicional dos tracos
COR = 'white'

#a classe Paddle eh herdeira da Turtle
class Paddle(Turtle):
    def __init__(self,posicao):
        super().__init__()
        #instancia um traco
        self.shape('square')
        #muda o tamanho dele
        self.shapesize(stretch_len=1,stretch_wid=5)
        #muda a cor dele
        self.color(COR)
        #faz com que nao deixe marcas por onde passar
        self.penup()
        #faz com que se mova para as coordenadas que passou
        self.goto(posicao)

    #funcao para subir o traco
    def subir(self):
        novoY = self.ycor() + 20
        self.goto(self.xcor(),novoY)   

    #funcao para descer o traco
    def descer(self):
        novoY = self.ycor() - 20
        self.goto(self.xcor(),novoY) 
        

