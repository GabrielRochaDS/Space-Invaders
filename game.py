from PPlay.sprite import *
import ship
from enemies import *

def jogar(janela,teclado,mouse,botao, dificuldade):
    
    #colocando a posição do botao "jogar" no menu    
    botao.set_position(janela.width/2 - botao.width/2,janela.height/ 2 - 230)
    #variavel booleana para retornar quando apertar esc 
    continua_jogo = False
   
    #verificando se o mouse esta sobre o botao para destaca-lo
    if mouse.is_over_object(botao):
        botao = Sprite("imgs/jogar.s.png")
        botao.set_position(janela.width / 2 - botao.width / 2, janela.height / 2 - 230)
        botao.draw()
        
        #interação com o botão quando o click do mouse é feito 
        if mouse.is_button_pressed(1):
            ship.gameplay(janela,teclado,mouse, 1,0, dificuldade, vidas = 3)
    else:
        botao.draw()
