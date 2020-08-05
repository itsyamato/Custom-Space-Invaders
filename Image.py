import pygame
import os.path

if os.path.isfile("bg_image.png") == True:
    os.remove("bg_image.png")
if os.path.isfile("player.png") == True:
    os.remove("player.png")
if os.path.isfile("enemy.png") == True:
    os.remove("enemy.png")
if os.path.isfile("p_bullet.png") == True:
    os.remove("p_bullet.png")
if os.path.isfile("e_bullet.png") == True:
    os.remove("e_bullet.png")

# Background
weidth, height = 1000, 600
ask_image_bg = input("Enter Background Image Name: ")
bg_image = pygame.image.load(ask_image_bg)
pygame.image.save(pygame.transform.scale(bg_image, (weidth, height)), "bg.png")

# Player
ask_image_player = input("Enter Player Image Name: ")
player_image = pygame.image.load(ask_image_player)
pygame.image.save(pygame.transform.scale(player_image, (70, 70)), "player.png")

# Enemy
ask_image_enemy = input("Enter Enemy Image Name: ")
enemy_image = pygame.image.load(ask_image_enemy)
pygame.image.save(pygame.transform.scale(enemy_image, (50, 50)), "enemy.png")

# Player Bullet
ask_image_p_bullet = input("Enter bullet image Name: ")
pb_image = pygame.image.load(ask_image_p_bullet)
pygame.image.save(pygame.transform.scale(pb_image, (25, 25)), "p_bullet.png")

# Enemy Bullet
ask_image_e_bullet = input("Enter Enemy bullet image Name: ")
eb_image = pygame.image.load(ask_image_e_bullet)
pygame.image.save(pygame.transform.scale(eb_image, (20, 20)), "e_bullet.png")
