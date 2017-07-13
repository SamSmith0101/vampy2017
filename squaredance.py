import pygame
import time
import random

SIZE = (640,480)
ColorBack = (255,255,255)
ColorSquare = (0,0,0)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hello World!")

square = pygame.Rect(640/2 - 100/2, 480/2 - 100/2, 100, 100)
direction = 1

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			direction *= 2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			direction /= 2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			ColorBack =(random.randint(0,255),random.randint(0,255),random.randint(0,255))
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			ColorSquare =(random.randint(0,255),random.randint(0,255),random.randint(0,255))
			
	screen.fill(ColorBack)
	pygame.draw.rect(screen, ColorSquare, square)
	pygame.display.flip()
	
	time.sleep(1/30)
	
	square = square.move(direction, 0)
	if square.x + square.w >= SIZE[0]:
		direction = -abs(direction)
	elif square.x <= 0:
		direction = abs(direction)
