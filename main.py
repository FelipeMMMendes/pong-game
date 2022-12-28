#fazendo os imports necessarios
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#instancia um objeto da classe Screen
tela = Screen()
#coloca a cor de fundo da tela como preto
tela.bgcolor('black')
#definindo o tamanho da tela
tela.setup(width=800,height=600)
#definindo o titulo da tela
tela.title("PONG")

#desliga as animacoes de criacao do traco
tela.tracer(0)

#instancia o objeto para mostrar a pontuacao
pontuacao = Scoreboard()
pontuacao.atualizarPont()

#instancia dois objetos do tipo Paddle
tracoDireito = Paddle((350,0))
tracoEsquerdo = Paddle((-350,0))

#instancia o objeto bola
bola = Ball()

#faz com que a tela receba inputs do teclado
tela.listen()

#desce ou sobe o traco de acordo com os comandos
tela.onkey(tracoDireito.subir,"Up")
tela.onkey(tracoDireito.descer,"Down")
tela.onkey(tracoEsquerdo.subir,"w")
tela.onkey(tracoEsquerdo.descer,"s")
tela.onkey(tracoEsquerdo.subir,"W")
tela.onkey(tracoEsquerdo.descer,"S")

#variavel para controlar a continuidade do jogo
jogoAtivo = True
while jogoAtivo:
    #faz o loop while dormir, para dar mais fluidez para o jogo
    time.sleep(bola.velBola)
    #faz com que a tela atualize a posicao do traco de maneira mais lenta, para parecer com o jogo
    tela.update()
    #faz com que a bola se mova
    bola.mover()
    #detecta se a bola bateu nas bordas superiores ou inferiores
    if bola.pos()[1] > 280 or bola.pos()[1] < -280 :
        #aplica o metodo bounce
        bola.bounceY()
    #detectar colisao com os dois tracos
    if (bola.distance(tracoDireito) < 50 and bola.xcor()) > 320 or (bola.distance(tracoEsquerdo) < 50 and bola.xcor() < -320):
        bola.bounceX()

    #detectar se a bola passou do lado esquerdo
    if bola.xcor() < -380:
        pontuacao.pontoDir()
        pontuacao.atualizarPont()
        bola.resetarBola()

    #detectar se a bola passou do lado direito
    if bola.xcor() > 380:
        pontuacao.pontoEsq()
        pontuacao.atualizarPont()
        bola.resetarBola()

#so fecha a tela quando o usuario clicar
tela.exitonclick()