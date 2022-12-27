#fazendo os imports necessarios
from turtle import Screen
from paddle import Paddle

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

#instancia dois objetos do tipo Paddle
tracoDireito = Paddle((350,0))
tracoEsquerdo = Paddle((-350,0))

#faz com que a tela receba inputs do teclado
tela.listen()

#desce ou sobe o traco de acordo com os comandos
tela.onkey(tracoDireito.subir,"Up")
tela.onkey(tracoDireito.descer,"Down")
tela.onkey(tracoEsquerdo.subir,"w")
tela.onkey(tracoEsquerdo.descer,"s")

#variavel para controlar a continuidade do jogo
jogoAtivo = True
while jogoAtivo:
    #faz com que a tela atualize a posicao do traco de maneira mais lenta, para parecer com o jogo
    tela.update()

#so fecha a tela quando o usuario clicar
tela.exitonclick()