import pygame
import time
import random

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH,HEIGHT)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEEN = (0,255,0)
BLUE = (0,0,255)
GREY = (128,128,128)
YELLOW = (255,255,0)
WAITING = 1
PLAYING = 2

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Let's Play Pong!")

state = WAITING
state_time = time.time()

speed_lpaddle = 0
speed_rpaddle = 0
speed_ball_x = 0
speed_ball_y = 0

paddle_w = 0.05*WIDTH
paddle_h = 5*paddle_w
ball_w = paddle_w
ball_h = ball_w
rect_lpaddle = pygame.Rect(paddle_w, HEIGHT/2 - paddle_h/2, paddle_w,paddle_h)
rect_rpaddle = pygame.Rect(0.90*WIDTH, HEIGHT/2 - paddle_h/2, paddle_w,paddle_h)
rect_ball = pygame.Rect(WIDTH/2 - ball_w/2, HEIGHT/2 - ball_h/2, ball_w,ball_h)

square = pygame.Rect(640/2 - 100/2, 480/2 - 100/2, 100, 100)
direction = 1

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			speed_lpaddle = -1
		elif event.type == pygame.KEYUP and event.key == pygame.K_w:
			speed_lpaddle = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			speed_lpaddle = 1
		elif event.type == pygame.KEYUP and event.key == pygame.K_s:
			speed_lpaddle = 0

		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			speed_rpaddle = -1
		elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
			speed_rpaddle = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			speed_rpaddle = 1
		elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
			speed_rpaddle = 0

	rect_lpaddle.move_ip(0, speed_lpaddle)
	rect_rpaddle.move_ip(0, speed_rpaddle)
	rect_ball.move_ip(speed_ball_x,speed_ball_y)
	if state == PLAYING:
		rect_ball.move.ip(speed_ball_x, speed_ball_y)
	elif state == WAITING:
		if time.time() - state_time >= 2:
			state = PLAYING
			state_time = time.time()
			speed_ball_x = 2*random.randint(0,1) - 1
			speed_ball_y = random.randint(-5,5)
			
	if rect_ball.y <= 0:
		rect_ball.y = 0
		speed_ball_y = abs(speed_ball_y)
	elif rect_ball.y + rect_ball.h >= HEIGHT:
		rect_ball.y = HEIGHT - rect_ball.h
		speed_ball_y = -abs(speed_ball_y)
		
	if rect_lpaddle.x <= rect_ball.x and rect_ball.x <= rect_lpaddle.x + rect_lpaddle.w:
		if rect_lpaddle.y-rect_ball.h <= rect_ball.y and rect_ball.y <= rect_lpaddle.y + rect_lpaddle::
			rect_ball.x = rect_lpaddle.x+rect_lpaddle.w
			speed_ball_x = abs(speed_ball_x)
			speed_ball_y = random.randint(-5,5)
	if rect_rpaddle.x <= rect_ball.x and rect_ball.x + rect_wall.w <= rect_rpaddle.x + rect_rpaddle.w:
		if rect_rpaddle.y-rect_ball.h <= rect_ball.y and rect_ball.y <= rect_rpaddle.y + rect_rpaddle.h:
			rect_ball.x = rect_rpaddle.x+rect_ball.w
			speed_ball_x = -abs(speed_ball_x)
			speed_ball_y = random.randint(-5,5)

	if rect_ball.x + rect_ball.w < 0:
		score = WAITING
		state_time = time.time()
		rect_ball.x = WIDTH/2 - rect_ball.w/2
		rect_ball.y = HEIGHT/2 - rect_ball.h/2
		speed_ball_x = 0
		speed_ball_y = 0

	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, rect_lpaddle)
	pygame.draw.rect(screen, WHITE, rect_rpaddle)
	pygame.draw.rect(screen, WHITE, rect_ball)
	pygame.display.flip()

	time.sleep(1/30)

