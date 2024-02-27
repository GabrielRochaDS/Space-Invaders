from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random

enemy_image = "imgs/enemy.png"
enemy_direction = 10
enemies = []
temporizador = 1
enemy_tiro = []
mov_tiro = 750


def spawn_enemy(L, C):    
    enemy = Sprite(enemy_image)
    espaco_entre_inimigos_x = 0.5 * enemy.width
    espaco_entre_inimigos_y = 0.5 * enemy.height

    for i in range(L):  
        for j in range(C):  
            posição_x = j * (enemy.width + espaco_entre_inimigos_x) + 50
            posição_y = i * (enemy.height + espaco_entre_inimigos_y)
            enemy = Sprite(enemy_image)
            enemy.set_position(posição_x, posição_y)
            enemy.direction = 1
            enemies.append(enemy)

def move_enemy(janela, temporizador, enemy_speed):
    if (temporizador>=0.01):
        for enemy in enemies:
            enemy.x =  enemy.x + enemy_speed * janela.delta_time()
        return 0
    temporizador = temporizador + 1*janela.delta_time()
    return temporizador

def tiro_enemy(janela, temporizador, num_eney, nave, vidas):
    if(num_eney >1):
        num_lin = random.randint(0,num_eney-1)
        randomizador = random.randint(0,30)
        if (temporizador >= 1.5 and randomizador == 1):
            shot_particle = Sprite("imgs/shot.png")
            shot_particle.set_position(enemies[num_lin].x+enemies[num_lin].width/2, enemies[num_lin].y)
            enemy_tiro.append(shot_particle)
            return (0, vidas)  
        if (enemy_tiro):
            for tiro in enemy_tiro:
                if tiro.collided(nave):
                    del enemy_tiro[enemy_tiro.index(tiro)]
                    vidas -=1
                tiro.y = tiro.y + mov_tiro*janela.delta_time()
                tiro.draw()
    temporizador = temporizador + 1*janela.delta_time()
    return (temporizador, vidas)

def remove_enemies():
    for enemy in enemies:
       del enemies[enemies.index(enemy)]
    return []