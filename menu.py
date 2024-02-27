from PPlay.window import *
from PPlay.sprite import *
import game
import dificulty
import ranking
import exit

#criando os sprites iniciais
janela = Window(1080, 720)
janela.set_title("Gabriel Rocha - Space invaders")
janela.set_background_color([0,0,0])

dificuldade_jogo = 1

#criando mouse e teclado
mouse = Window.get_mouse()
teclado = Window.get_keyboard()

#criando sprites
botao_dificuldade = Sprite("imgs/dificuldade.png")
botao_jogar = Sprite("imgs/jogar.png") 
botao_ranking = Sprite("imgs/ranking.png") 
botao_sair = Sprite("imgs/sair.png") 


#game loop
while(True):
    janela.set_background_color([0,0,0])

    game.jogar(janela,teclado,mouse,botao_jogar, dificuldade_jogo)
    dificuldade_jogo = dificulty.dif(janela,teclado,mouse,botao_dificuldade, dificuldade_jogo)
    ranking.rank(janela,mouse,botao_ranking, teclado)
    exit.sair(janela,mouse,botao_sair)
    janela.update()
