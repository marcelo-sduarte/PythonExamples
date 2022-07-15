from main import pygame
from constants import *
from main import bow_group, nephi_sound, bow


class Poison(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(POISON_IMAGE)
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):
		self.rect.y += 2
		if self.rect.top > SCREEN_HEIGHT:
			self.kill()
		if pygame.sprite.spritecollide(self, bow_group, False, pygame.sprite.collide_mask):
			self.kill()
			nephi_sound.play()
			#reduce spaceship health
			bow.health_remaining -= 1