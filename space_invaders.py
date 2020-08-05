import pygame
import math
import time
import random
from PIL import Image
# import Image

pygame.init()
weidth, height = 1000, 600
screen = pygame.display.set_mode((weidth, height))
caption = pygame.display.set_caption("AAO KHELEIN!!")

# Background
bg_image = pygame.image.load("bg.png")

# Player
p_image = pygame.image.load("player.png")
playerX = 500
playerY = 500
playerX_change = 0

# Enemy
e_image = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = 0.2
num_of_enemies = 3
for i in range(num_of_enemies):
    e_image.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(10, 990))
    enemyY.append(10)
    enemyX_change.append(random.randrange(-3, 3))

# Player Bullet
pb_image = pygame.image.load("p_bullet.png")
pbX, pbY = playerX, playerY
pb_movement = 0
bullet_state = "Ready"

# Enemy Bullet
eb_img = pygame.image.load("e_bullet.png")
eb_scale = []
eb_movement = 1
ebX1, ebY1 = [], 0
ebX2, ebY2 = [], 0
eb_state = []
num_of_eb = num_of_enemies
for i in range(num_of_eb):
    eb_scale.append(pygame.transform.scale(eb_img, (20, 20)))
    eb_state.append("Ready")


def icon_pos(name, posx, posy):
    return screen.blit(name, (posx, posy))


# Player Bullet Fire
p_bullet_movement = 0


def pb_fire():
    global bullet_state
    bullet_state = "Fire"


# Collisions
# Player Side
def p_bang(enemyX, enemyY, pbX, pbY):
    d_pb_2_e = math.sqrt((math.pow((enemyX - pbX), 2) + (math.pow((enemyY - pbY), 2))))
    if d_pb_2_e < 25:
        print("enemyX:", enemyY, "pbX:", pbX)
        print("enemyY:", enemyY, "pbY: ", pbY)
        print("d_pb_2_e: ", d_pb_2_e)
        return True
    else:
        return False


# Enemy Side
def e_bang(playerX, playerY, ebX1, ebY1, ebX2, ebY2):
    d_eb1_2_p = math.sqrt((math.pow(playerX - ebX1, 2)) + (math.pow(playerY - ebY1, 2)))
    d_eb2_2_p = math.sqrt((math.pow(playerX - ebX2, 2)) + (math.pow(playerY - ebY2, 2)))
    if d_eb1_2_p < 20 or d_eb2_2_p < 20:
        return True
    else:
        return False


score_val = 0
running = True
while running:
    screen.blit(bg_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # KEYDOWN
        if event.type == pygame.KEYDOWN:
            # Player
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            # Bullet
            if event.key == pygame.K_SPACE:
                pbX = playerX
                pbY = playerY
                pb_fire()
        # KEYUP
        if event.type == pygame.KEYUP:
            playerX_change = 0

    # Player Bullet
    pb_movement = 20
    if bullet_state == "Fire":
        icon_pos(pb_image, (pbX + 20), (pbY + 20))
        pbY -= pb_movement
        if pbY < 0:
            bullet_state = "Ready"
            pbY = playerY + 15

    # Player Movement
    icon_pos(p_image, playerX, playerY)
    if playerX < 20:
        playerX = 20
    if playerX > 911:
        playerX = 910
    playerX += playerX_change

    # Enemy Bullet

    for state in eb_state:
        if state == "Ready":
            for i in range(num_of_enemies):
                ebX1.append(enemyX[i] + 10)
                ebY1 = enemyY[i] + 20
                ebX2.append(enemyX[i] + 25)
                ebY2 = enemyY[i] + 20

    for state in range(len(eb_state)):
        eb_state[state] = "Fire"
        if eb_state[state] == "Fire":
            for i in range(num_of_enemies):
                icon_pos(eb_scale[i], ebX1[i], ebY2)
                icon_pos(eb_scale[i], ebX2[i], ebY2)
                ebY1 += eb_movement
                ebY2 += eb_movement
    if ebY1 > 650:
        ebX1, ebX2 = [], []
        for state in range(len(eb_state)):
            eb_state[state] = "Ready"

    # Enemy Movement
    for i in range(num_of_enemies):
        enemyY[i] += enemyY_change
        enemyX[i] += enemyX_change[i]
        icon_pos(e_image[i], enemyX[i], enemyY[i])
        if enemyX[i] < 20:
            #enemyX[i] = 20
            enemyX_change[i] = -(enemyX_change[i])
        if enemyX[i] > 950:
            #enemyX[i] = 950
            enemyX_change[i] = -(enemyX_change[i])
        # Collision
        smash = p_bang(enemyX[i], enemyY[i], pbX, pbY)
        if smash:
            bullet_state = "Ready"
            pbY = playerY
            enemyY[i] = 0
            ebX1[i] = 0 
            score_val += 1

    print(score_val)

    pygame.display.update()
