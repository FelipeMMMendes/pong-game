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

#instancia um objeto do tipo Paddle
traco = Paddle()

#faz com que a tela receba inputs do teclado
tela.listen()

#desce ou sobe o traco de acordo com os comandos
tela.onkey(traco.subir,"Up")
tela.onkey(traco.descer,"Down")

#variavel para controlar a continuidade do jogo
jogoAtivo = True
while jogoAtivo:
    #faz com que a tela atualize a posicao do traco de maneira mais lenta, para parecer com o jogo
    tela.update()

#so fecha a tela quando o usuario clicar
tela.exitonclick()