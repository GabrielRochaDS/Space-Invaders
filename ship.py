from PPlay.window import *
from PPlay.sprite import *
from pplay.keyboard import Keyboard
from enemies import *
import menu
from ranking_arquivos import *

def gameplay(janela,teclado,mouse, fase, pontuacao, velocidade, vidas):
    #Criando os sprites
    nave = Sprite("imgs/nave.png")
    
    #criando as variaveis qua vai mover o tiro e a nave
    movimento_nave = 500
    movimento_tiro = -800
    tiro_nave_delay = 0
    #setando a posição das coisas
    nave.set_position(janela.width/2 - nave.width/2,janela.height - nave.height)
    nave.draw()
    janela.update()
    tiro = []
    

    #spawnando os inimigos antes do gameloop para não diminuir muito o fps
    for enemy in enemies:
        del enemies[enemies.index(enemy)]
    if fase == 1:
        spawn_enemy(2, 10)
    elif fase == 2:
        spawn_enemy(3, 14)
    elif fase == 3:
        spawn_enemy(4, 14)
    elif fase == 4:
        spawn_enemy(5, 14)

    #variavel que conta a valocidade do inimigo e um temporizador para o inimigo se mecher.
    enemy_speed = 1000
    temporizador_movimento_inimigo = 0
    temporizador_tiro_enemy = 0
    #variavel que vai ajudar a contar o fps
    frames = 0
    start_time = time.time()

    #game loop
    while(True):

        janela.set_background_color((0, 0, 0))
        if teclado.key_pressed("A") and (nave.x >= 0):
            nave.x = nave.x - movimento_nave*janela.delta_time()
        if teclado.key_pressed("D") and (nave.x <= janela.width-nave.width):
            nave.x = nave.x + movimento_nave*janela.delta_time()
        
        #verificando tecla para sair do jogo
        if teclado.key_pressed("esc"):
            janela.close()
        
        #verificando se o space foi apertado para atirar
        tiro_nave_delay = tiro_nave_delay + 1*janela.delta_time()
        if teclado.key_pressed("space"):
            if len(tiro) != 0:
                if tiro_nave_delay > 0.5:
                    shot_particle = Sprite("imgs/shot.png")
                    shot_particle.set_position(nave.x+nave.width/2, nave.y)
                    tiro.append(shot_particle)
                    tiro_nave_delay = 0
            else:
                shot_particle = Sprite("imgs/shot.png")
                shot_particle.set_position(nave.x+nave.width/2, nave.y)
                tiro.append(shot_particle)
        
        
        #desenhando os inimigos e os tiros
        for enemy in enemies:
            enemy.draw()
            if (enemy.y+enemy.height > nave.y):
                break        
                    
        for i in tiro:
            i.y = i.y + movimento_tiro*janela.delta_time()
            i.draw()

        
        #vendo a posição do inimigo para calibrar a sua direção e atualizando a posição y.
        num_enemy = 0
        for enemy in enemies:
            num_enemy +=1
            if enemy.x >= (janela.width - enemy.width):
                enemy_speed = -1000
                for enemy in enemies:
                    enemy.y += 1.5
                break          
            if enemy.x <= 0:
                enemy_speed = 1000
                for enemy in enemies:
                    enemy.y += 1.5
                break     

        #vendo a colisão dos tiros com os inimigos.
        for i in tiro:
            for enemy in enemies:
                if i.collided(enemy):
                    if i.y > janela.height/2:
                        pontuacao +=1
                    else:
                        pontuacao +=2
                    del enemies[enemies.index(enemy)]
                    del tiro[tiro.index(i)]
        #FPS
        frames += 1
        fps = frames / (time.time() - start_time)
        frames = 0
        start_time = time.time()
        janela.draw_text(f"FPS: {fps:.2f}", janela.width - 120, janela.height - 50, size=15, color=(255, 255, 255))
        
        #Tiro enemy
        temporizador_tiro_enemy, vidas = tiro_enemy(janela, temporizador_tiro_enemy, num_enemy, nave, vidas)
        if (vidas<1):
            nome = input("Digite seu Nome:")
            set_ranking ("ranking.txt", pontuacao, nome, "##--data--##")
            organizador_ranking("ranking.txt")
            janela.close()

        if num_enemy == 0:
            fase +=1
            gameplay(janela,teclado,mouse, fase, pontuacao, velocidade, vidas)
        
        
        janela.draw_text(f"Vidas: {vidas}", 0, janela.height - 50, size=20, color=(255, 255, 255))

        #Contador de Pontuação
        janela.draw_text(f"Pontuação: {pontuacao}", 0, janela.height - 75, size=20, color=(255, 255, 255))
        
        #movendo os inimigos e atualizando o temporizador
        temporizador_movimento_inimigo = move_enemy(janela, temporizador_movimento_inimigo, enemy_speed)
        
        #desenhando as naves
        nave.draw()
        
        janela.update()