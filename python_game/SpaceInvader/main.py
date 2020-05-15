import pygame


pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))



pygame.display.set_caption("Space Invader")

icon = pygame.image.load("spaceship.png")

pygame.display.set_icon(icon)

running = True

#Main loop
while running:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False	
	screen.fill((0,19,0))
	pass
