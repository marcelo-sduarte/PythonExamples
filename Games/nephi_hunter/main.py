import pygame
from pygame import mixer
from pygame.locals import *
import random
from constants import *


#call functions pygame
pygame.mixer.pre_init(FREQUENCY, SIZE, CHANNELS, BUFFER)
mixer.init()
pygame.init()


#define fps
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_NAME)

#define fonts
font30 = pygame.font.SysFont('Constantia', 30)
font40 = pygame.font.SysFont('Constantia', 40)

#load sounds and set volume
animal_sound = pygame.mixer.Sound(ANIMAL_SOUND)
animal_sound.set_volume(VOLUME)

nephi_sound = pygame.mixer.Sound(NEPHI_SOUND)
nephi_sound.set_volume(VOLUME)

arrow_sound = pygame.mixer.Sound(ARROW_SOUND)
arrow_sound.set_volume(VOLUME)

last_animal_shot = pygame.time.get_ticks()
countdown = 3
last_count = pygame.time.get_ticks()

#load image
background = pygame.image.load(DESERT_IMAGE)

#method of class main to show background
def draw_bg():
	screen.blit(background, (0, 0))

#method class main to write text
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

#create Desert class

class Desert(pygame.sprite.Sprite):
	""" 
    
    The responsibility of a Desert class is to create interations on the desert background
	

    Attributes:
       x, y (int) : position retangle 
		health_start : health

    """

	def __init__(self, x, y, health):
		"""Constructs a new Desert instance."""
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(BOW_IMAGE)
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.health_start = health
		self.health_remaining = health
		self.last_shot = pygame.time.get_ticks()


	def update(self):
		"""Checks if the given key is currently right or left.
        
        Args:
            key (pygame): The given key (left, right and space)
        """
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
		
		#shoot arrow to the bow
		if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
			arrow_sound.play()
			arrow = Arrow(self.rect.centerx, self.rect.top)
			bullet_group.add(arrow)
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


#create Arrow class
class Arrow(pygame.sprite.Sprite):
	""" A arrow from the bow.
    
    The responsibility of arrow is to move from bow to animals target.

    Attributes:
        image (pygame): the path to the arrow image constant
		x, y (int) : position retangle 
        """
	def __init__(self, x, y):
		"""Constructs a new Arrow instance."""
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(ARROW_IMAGE)
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):
		""" To verify collisions between animal group and arrow"""
		self.rect.y -= 5
		if self.rect.bottom < 0:
			self.kill()
		if pygame.sprite.spritecollide(self, animal_group, True):
			self.kill()
			animal_sound.play()
	

#create Animal class
class Animals(pygame.sprite.Sprite):
	""" Show a group Animals on the screen
    
    The responsibility of Animlas is to move on the screen.

    Attributes:
        _image (pygame): the path to the Animal image constant
		x, y (int) : position retangle 
        """

	def __init__(self, x, y):
		"""Constructs a new Animal instance."""

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("images/animal" + str(random.randint(1, 5)) + ".png")
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.move_counter = 0
		self.move_direction = 1

	def update(self):
		""" Center animals on the screen an move yourself"""
		self.rect.x += self.move_direction
		self.move_counter += 1
		if abs(self.move_counter) > 75:
			self.move_direction *= -1
			self.move_counter *= self.move_direction

#create Poison Bullets class
class Poison(pygame.sprite.Sprite):
	""" Show a group Animals on the screen
    
    The responsibility of Poison is to move from animals to the Nephi bow

    Attributes:
        _image (pygame): the path to the Poison image constant
		x, y (int) : position on the retangle 
        """

	def __init__(self, x, y):
		"""Constructs a new Poison instance."""
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(POISON_IMAGE)
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):
		"""To veify the collisions on the animals group"""
		self.rect.y += 2
		if self.rect.top > SCREEN_HEIGHT:
			self.kill()
		if pygame.sprite.spritecollide(self, bow_group, False, pygame.sprite.collide_mask):
			self.kill()
			nephi_sound.play()
			#reduce nephi health
			bow.health_remaining -= 1		

#create sprite groups
bow_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
animal_group = pygame.sprite.Group()
poison_group = pygame.sprite.Group()



def create_animals():
	#method to generate animals
	for row in range(ROWS):
		for item in range(COLUMNS):
			animal = Animals(100 + item * 100, 100 + row * 70)
			animal_group.add(animal)


create_animals()

#create player
bow = Desert(int(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 100, 3)
bow_group.add(bow)

countdown = 3
run = True
while run:

	clock.tick(FPS)

	#draw background
	draw_bg()

	if countdown == 0:
		#create random bow bullets
		#record current time
		time_now = pygame.time.get_ticks()
		#shoot
		if time_now - last_animal_shot > COOLDOWN and len(poison_group) < 5 and len(animal_group) > 0:
			attacking_animal = random.choice(animal_group.sprites())
			poison = Poison(attacking_animal.rect.centerx, attacking_animal.rect.bottom)
			poison_group.add(poison)
			last_animal_shot = time_now

		#check if all the animals have been killed
		if len(animal_group) == 0:
			GAME_OVER = 1

		if GAME_OVER == 0:
			#update spaceship
			GAME_OVER = bow.update()

			#update sprite groups
			bullet_group.update()
			animal_group.update()
			poison_group.update()
		else:
			if GAME_OVER == -1:
				draw_text('GAME OVER!', font40, WHITE, int(SCREEN_WIDTH / 2 - 100), int(SCREEN_HEIGHT / 2 + 50))
			if GAME_OVER == 1:
				draw_text('YOU WIN!', font40, WHITE, int(SCREEN_WIDTH / 2 - 100), int(SCREEN_HEIGHT / 2 + 50))

	if countdown > 0:
		draw_text('GET READY!', font40, WHITE, int(SCREEN_WIDTH / 2 - 110), int(SCREEN_HEIGHT / 2 + 50))
		draw_text(str(countdown), font40, WHITE, int(SCREEN_WIDTH / 2 - 10), int(SCREEN_HEIGHT / 2 + 100))
		count_timer = pygame.time.get_ticks()
		if count_timer - last_count > 1000:
			countdown -= 1
			last_count = count_timer


	#draw sprite groups
	bow_group.draw(screen)
	bullet_group.draw(screen)
	animal_group.draw(screen)
	poison_group.draw(screen)


	#event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
