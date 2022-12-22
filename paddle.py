#fazendo os imports necessarios
from turtle import Turtle

#variaveis flag para auxiliar na configuracao visual e posicional dos tracos
COR = 'white'
POS_PLAYER = (350,0)
POS_PC = (-350,0)

#a classe Paddle eh herdeira da Turtle
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        #instancia um traco
        self.paddle= Turtle(shape='square')
        #muda o tamanho dele
        self.paddle.shapesize(stretch_len=1,stretch_wid=5)
        #muda a cor dele
        self.paddle.color(COR)
        #faz com que nao deixe marcas por onde passar
        self.paddle.penup()
        #move cada um para um canto da tela
        self.paddle.goto(POS_PLAYER)

    def subir(self):
        novoY = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(),novoY)   

    def descer(self):
        novoY = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(),novoY)    
        

