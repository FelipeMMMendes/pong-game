#fazendo os imports necessarios
from turtle import Screen

#instancia um objeto da classe Screen
tela = Screen()
#coloca a cor de fundo da tela como preto
tela.bgcolor('black')
#definindo o tamanho da tela
tela.setup(width=600,height=600)
#definindo o titulo da tela
tela.title("PONG")

#so fecha a tela quando o usuario clicar
tela.exitonclick()