import pygame
pygame.init()
import math
import time
import random
pygame.font.init()

# import Image

# Window
width, height = 1000, 600
screen = pygame.display.set_mode((width, height))
caption = pygame.display.set_caption("AAO KHELEIN!!")

# Image Load
bg_image = pygame.image.load("bck.png")
p_image = pygame.image.load("player.png")
e_image = pygame.image.load("enemy.png")
pb_image = pygame.image.load("p_bullet.png")
eb_img = pygame.image.load("e_bullet.png")


class laser:
	def __init__(self, x, y, img):
		self.x = x
		self.y = y
		self.img = img
		self.mask = pygame.mask.from_surface(self.img)

	def draw(self):
		screen.blit(self.img, (self.x, self.y))

	def move(self, movement):
		self.y += movement

	def off_screen(self, height):
		return not (self.y <= height and self.y >= 0)


class ship:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.ship_image = None
		self.bullet_image = None
		self.lasers = []
		self.count = 0

	def ship_draw(self):
		screen.blit(self.ship_image, (self.x, self.y))

	def get_width(self):
		return self.ship_image.get_width()

	def get_height(self):
		return self.ship_image.get_height()

class player(ship):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.ship_image = p_image
		self.bullet_image = pb_image
		self.mask = pygame.mask.from_surface(self.ship_image)

class enemy(ship):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.ship_image = e_image
		self.bullet_image = eb_img
		self.mask = pygame.mask.from_surface(self.ship_image)

def collide(obj1, obj2):
	offset_x = obj2.x - obj1.x
	offset_y = obj2.y - obj1.y
	return obj1.mask.overlap(obj2.mask, (int(offset_x), int(offset_y))) #!= None



def game_loop():
	run = True
	score, level = 0, 1 
	num_of_enemies, num_of_enemies_increment = 2, 2
	enemies = []
	e_ship_movex, e_ship_movey = [], 0.6
	p_movement = 6
	info_font = pygame.font.SysFont("comisans", 50)
	display_font = pygame.font.SysFont("comisans", 100)
	lost = False
	pb_state = "Ready"


	#Objects
	p_ship = player(450, 500)
	

	while run:
		screen.blit(bg_image, (0,0))

		# ENemy Ship 
		for i in range (num_of_enemies):
			enemies.append(enemy((random.randint(50, (width - 100))), -50))
			e_ship_movex.append(random.randint(-5, 5))
			

		# Score and Level
		if score == num_of_enemies:
			level += 1
			num_of_enemies_increment += 2
			num_of_enemies += num_of_enemies_increment 

		
		# Objects Draw
		# Player Bullet
		if pb_state == "Ready":
			pb = laser((p_ship.x + 22), (p_ship.y + 20), pb_image)
		if pb_state == "Fire":
			pb.draw()
			pb.move(-10)
		if pb.y < 10:
			pb_state = "Ready"
		# Enemy
		for i in range(num_of_enemies):
			enemies[i].ship_draw()
		# PLayer
		p_ship.ship_draw()
		

		# Text Display
		score_label = info_font.render(f"Score: {score}", 1, (255, 255, 255))
		level_label = info_font.render(f"Level: {level}", 1, (255, 255, 255))
		lost_label = display_font.render(f"""GAME KHATAM""", 1, (255, 0, 0))
		screen.blit(score_label, (10, 10))
		screen.blit(level_label, (width - level_label.get_width() - 10, 10))

		# Loosing Text
		if lost == True:
			screen.blit(lost_label, ((width) / 2 - (lost_label.get_width())/ 2, 300))
			p_ship.x = 2000
			for i in enemies:
				i.y = 1000


		#Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		# MOVEMENT
		# PLayer
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP] and p_ship.y > 0 :
			p_ship.y -= p_movement
		if keys[pygame.K_DOWN] and p_ship.y + p_ship.get_height() < height:
			p_ship.y += p_movement
		if keys[pygame.K_RIGHT] and p_ship.x + p_ship.get_width() < width:
			p_ship.x += p_movement
		if keys[pygame.K_LEFT] and p_ship.x > 0:
			p_ship.x -= p_movement
		if keys[pygame.K_SPACE]:
			pb_state = "Fire"
		
		# Enemy Movement
		for i in range(num_of_enemies):
			enemies[i].x += e_ship_movex[i]
			enemies[i].y += e_ship_movey
			if enemies[i].x > (width - 70) or enemies[i].x < (20):
				e_ship_movex[i] = -(e_ship_movex[i])

			# Collide of PB and ENemy
			if collide(pb, enemies[i]):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
				score += 1
				pb_state = "Ready"
				enemies[i].y = -10000000

			#Collide of Enemy and Player
			if collide(enemies[i], p_ship) or enemies[i].y >= 500:
				lost = True


		print(score)
		pygame.display.update()

game_loop()