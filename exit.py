from PPlay.sprite import *

def sair(janela,mouse,botao):
    #colocando a posição do botao.
    botao.set_position(janela.width/2 - botao.width/2,janela.height / 2 + 190)

    #verificando se o mouse esta sobre o botao para destaca-lo
    if mouse.is_over_object(botao):
        botao = Sprite("imgs/sair.s.png")
        botao.set_position(janela.width / 2 - botao.width / 2, janela.height / 2 + 190)
        botao.draw()
        #interação com o botão quando o click do mouse é feito 
        if mouse.is_button_pressed(1):
            janela.close()
    else:
        botao.draw()