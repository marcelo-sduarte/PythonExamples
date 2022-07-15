from main import screen
from constants import *
from arrow import Arrow
import pygame

class Desert(pygame.sprite.Sprite):
	def __init__(self, x, y, health, group):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(BOW_IMAGE)
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.health_start = health
		self.health_remaining = health
		self.last_shot = pygame.time.get_ticks()
		self.arrow_sound = pygame.mixer.Sound(ARROW_SOUND)
		self.arrow_sound.set_volume(VOLUME)
		self.bullet_group = group


	def update(self):
		#set movement speed
		speed = 8
		#set a cooldown variable
		cooldown = 500 #milliseconds
		game_over = 0


		#get key press
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and self.rect.left > 0:
			self.rect.x -= speed
		if key[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
			self.rect.x += speed

		#record current time
		time_now = pygame.time.get_ticks()
		#shoot
		if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
			self.arrow_sound.play()
			arrow = Arrow(self.rect.centerx, self.rect.top)
			self.bullet_group.add(arrow)
			self.last_shot = time_now


		#update mask
		self.mask = pygame.mask.from_surface(self.image)


		#draw health bar
		pygame.draw.rect(screen, RED, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
		if self.health_remaining > 0:
			pygame.draw.rect(screen, GREEN, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))
		elif self.health_remaining <= 0:
			self.kill()
			game_over = -1
		return game_over


		