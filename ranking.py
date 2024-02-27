from PPlay.sprite import *
from ranking_arquivos import *

def rank (janela,mouse,botao, teclado):
    #colocando a posição do botao.
    botao.set_position(janela.width/2 - botao.width/2,janela.height / 2 + 50)
    #verificando se o mouse esta sobre o botao para destaca-lo
    if mouse.is_over_object(botao):
        botao = Sprite("imgs/ranking.s.png")
        botao.set_position(janela.width / 2 - botao.width / 2, janela.height / 2 + 50)
        botao.draw()
        
        if mouse.is_button_pressed(1):
            show_rank(janela,mouse,botao, teclado)
                
    
    else:
        botao.draw()
def show_rank(janela,mouse,botao, teclado):
    while True:

        janela.set_background_color([0, 0, 0])
        organizador_ranking('ranking.txt')
        lista = lista_ranking('ranking.txt')
        altura = 40
        contador = 0
        janela.draw_text("Pontos - Nomes - Data", janela.width / 2 - 180, janela.height / 2 - 200, size=40,
                              color=(255, 255, 255), font_name="Arial", bold=True, italic=False)
        for i in lista:
            if (contador < 5):
                janela.draw_text(i, janela.width/2 - 180, janela.height/2 - 140 + altura * contador, size=24,
                                      color=(255, 255, 255), font_name="Arial", bold=True, italic=False)
            contador += 1

        janela.update()

        if teclado.key_pressed("esc"):
            break