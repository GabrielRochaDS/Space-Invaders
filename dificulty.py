from PPlay.window import *
from PPlay.sprite import *


def dif (janela,teclado,mouse,botao, dificuldade_jogo):
    #colocando a posição do botao e criando sprites dos botoes dos niveis
    botao.set_position(janela.width/2 - botao.width/2,janela.height / 2 - 90)
    botao_facil = Sprite("imgs/facil.png")
    botao_medio = Sprite("imgs/medio.png")
    botao_dificil = Sprite("imgs/dificil.png")
    dificuldade_jogo = 1
    #verificando se o mouse esta sobre o botao para destaca-lo
    if mouse.is_over_object(botao):
        botao = Sprite("imgs/dificuldade.s.png")
        botao.set_position(janela.width / 2 - botao.width / 2, janela.height / 2 - 90)
        botao.draw()
        #interação com o botão quando o click do mouse é feito 
        if mouse.is_button_pressed(1):
            while True:
                botao_facil.set_position(janela.width/2 - botao_facil.width/2,janela.height/2 - 150)
                botao_medio.set_position(janela.width/2 - botao_medio.width/2,janela.height/2)
                botao_dificil.set_position(janela.width / 2 - botao_dificil.width / 2, janela.height / 2 + 150)

                janela.set_background_color([0,0,0])
                #verificando se o mouse esta sobre o botao para destaca-lo
                if mouse.is_over_object(botao_facil):
                    botao_facil = Sprite("imgs/facil.s.png")
                    botao_facil.set_position(janela.width / 2 - botao_facil.width / 2, janela.height / 2 - 150)
                    botao_facil.draw()
                    if mouse.is_button_pressed(1):
                        return  1
                        
                else:
                    botao_facil = Sprite(("imgs/facil.png"))
                    botao_facil.set_position(janela.width / 2 - botao_facil.width / 2, janela.height / 2 - 150) 
                    botao_facil.draw()
                #verificando se o mouse esta sobre o botao para destaca-lo
                if mouse.is_over_object(botao_medio):
                    botao_medio = Sprite("imgs/medio.s.png")
                    botao_medio.set_position(janela.width / 2 - botao_medio.width / 2, janela.height / 2)
                    botao_medio.draw()
                    if mouse.is_button_pressed(1):
                        return  2
                        
                else:
                    botao_medio = Sprite(("imgs/medio.png"))
                    botao_medio.set_position(janela.width / 2 - botao_medio.width / 2, janela.height / 2)
                    botao_medio.draw()
                #verificando se o mouse esta sobre o botao para destaca-lo
                if mouse.is_over_object(botao_dificil):
                    botao_dificil = Sprite("imgs/dificil.s.png")
                    botao_dificil.set_position(janela.width / 2 - botao_dificil.width / 2, janela.height / 2 + 150)
                    botao_dificil.draw()
                    if mouse.is_button_pressed(1):
                        return  3
                      
                else:
                    botao_dificil = Sprite(("imgs/dificil.png"))
                    botao_dificil.set_position(janela.width / 2 - botao_dificil.width / 2, janela.height / 2 + 150)
                    botao_dificil.draw()
                #verificando se o mouse esta sobre o botao para destaca-lo
                if teclado.key_pressed("esc"):
                    break
                janela.update()
    else:
        botao.draw()
    return dificuldade_jogo
    