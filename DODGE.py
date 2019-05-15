#import libraries
import pygame
import sys
import random
import time


pygame.init()

# #font
# font = pygame.font.SysFont(None, 10)

# #mesaage to screen
# def message_to_screen(msg, color):
# 	screen_txt = font.render(msg, True, color)
# 	screen.blit(screen_txt,[WIDTH / 4, HEIGHT / 4])


# Screen resolution
WIDTH = 800
HEIGHT = 600

#radius of player
rad = 25

player_size = rad
half = int(rad / 2)

#enemy size
enemy1_size = rad
enemy2_size = rad
enemy3_size = rad
enemy4_size = rad
enemy5_size = rad

#speed of enemies
SPEED1 = 10
SPEED2 = 20
SPEED3 = 25
SPEED4 = 30
SPEED5 = 35

#color of player
player_color = (0,255,0)

#color of enemies
enemy1_color = (117,8,198)
enemy2_color = (255,255,18)
enemy3_color = (43,215,216)
enemy4_color = (242,48,47)
enemy5_color = (255,255,255)

#color of background
background_color = (0,0,0)

#enemies position
enemy1_pos = [random.randint(0,WIDTH - enemy1_size),0]
enemy2_pos = [random.randint(0,WIDTH - enemy2_size),0]
enemy3_pos = [random.randint(0,WIDTH - enemy2_size),0]
enemy4_pos = [random.randint(0,WIDTH - enemy2_size),0]
enemy5_pos = [random.randint(0,WIDTH - enemy2_size),0]

#player position coordinates
player_pos = [WIDTH / 2, HEIGHT - 4 * rad]

#scores
total_scr = 0
enemy1_scr = 100
enemy2_scr = 70
enemy3_scr = 50
enemy4_scr = 20
enemy5_scr = 10

#number of balls dodged
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

#screen size
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#game framerate clock
clock = pygame.time.Clock()

#Collion detection function
def collision_detection1(player_pos,enemy1_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e1_x = enemy1_pos[0]
	e1_y = enemy1_pos[1]

	if (e1_x >= p_x and e1_x < (p_x + player_size + half)) or (p_x >= e1_x and p_x <(e1_x + enemy1_size + half)):
		if(e1_y >= p_y and e1_y < (p_y + player_size + half)) or (p_y >= e1_y and p_y < (e1_y + enemy1_size + half)):
			return True
	return False

def collision_detection2(player_pos,enemy2_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e2_x = enemy2_pos[0]
	e2_y = enemy2_pos[1]

	if (e2_x >= p_x and e2_x < (p_x + player_size + half)) or (p_x >= e2_x and p_x <(e2_x + enemy2_size + half)):
		if(e2_y >= p_y and e2_y < (p_y + player_size + half)) or (p_y >= e2_y and p_y < (e2_y + enemy2_size + half)):
			return True
	return False

def collision_detection3(player_pos,enemy3_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e3_x = enemy3_pos[0]
	e3_y = enemy3_pos[1]

	if (e3_x >= p_x and e3_x < (p_x + player_size + half)) or (p_x >= e3_x and p_x <(e3_x + enemy3_size + half)):
		if(e3_y >= p_y and e3_y < (p_y + player_size + half)) or (p_y >= e3_y and p_y < (e3_y + enemy3_size + half)):
			return True
	return False

def collision_detection4(player_pos,enemy4_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e4_x = enemy4_pos[0]
	e4_y = enemy4_pos[1]

	if (e4_x >= p_x and e4_x < (p_x + player_size + half)) or (p_x >= e4_x and p_x <(e4_x + enemy4_size + half)):
		if(e4_y >= p_y and e4_y < (p_y + player_size + half)) or (p_y >= e4_y and p_y < (e4_y + enemy4_size + half)):
			return True
	return False

def collision_detection5(player_pos,enemy5_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e5_x = enemy5_pos[0]
	e5_y = enemy5_pos[1]

	if (e5_x >= p_x and e5_x < (p_x + player_size + half)) or (p_x >= e5_x and p_x <(e5_x + enemy5_size + half)):
		if(e5_y >= p_y and e5_y < (p_y + player_size + half)) or (p_y >= e5_y and p_y < (e5_y + enemy5_size + half)):
			return True
	return False
game_over = False

# game loop
while not game_over:

#events in the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

#controling player position with keys
		if event.type == pygame.KEYDOWN:

			x = player_pos[0]
			y = player_pos[1]

			x1 = enemy1_pos[0]
			y2 = enemy1_pos[1]

			if event.key == pygame.K_LEFT:
				if x <= 0 + rad:
					player_pos = [x,y]
				else:
					x -= rad
			elif event.key == pygame.K_RIGHT:
				if x >= WIDTH - rad:
					player_pos = [x,y]
				else:
					x += rad

			player_pos = [x,y]


# drawing the shape on the canvass
	screen.fill((background_color))

#make enemy1 fall update
	if enemy1_pos[1] >= 0 and enemy1_pos[1] < HEIGHT:
		enemy1_pos[1] += SPEED1
	else:
		enemy1_pos[0] = random.randint(0,WIDTH - half + enemy1_size)
		enemy1_pos[1] = 0

	if collision_detection1(player_pos,enemy1_pos):
		game_over = True

#make enemy2 fall update
	if enemy2_pos[1] >= 0 and enemy2_pos[1] < HEIGHT:
		enemy2_pos[1] += SPEED2
	else:
		enemy2_pos[0] = random.randint(0,WIDTH - half + enemy2_size)
		enemy2_pos[1] = 0

	if collision_detection2(player_pos,enemy2_pos):
		game_over = True

#make enemy3 fall update
	if enemy3_pos[1] >= 0 and enemy3_pos[1] < HEIGHT:
		enemy3_pos[1] += SPEED3
	else:
		enemy3_pos[0] = random.randint(0,WIDTH - half + enemy3_size)
		enemy3_pos[1] = 0

	if collision_detection3(player_pos,enemy3_pos):
		game_over = True

#make enemy4 fall update
	if enemy4_pos[1] >= 0 and enemy4_pos[1] < HEIGHT:
		enemy4_pos[1] += SPEED4
	else:
		enemy4_pos[0] = random.randint(0,WIDTH - half + enemy4_size)
		enemy4_pos[1] = 0

	if collision_detection4(player_pos,enemy4_pos):
		game_over = True

#make enemy5 fall update
	if enemy5_pos[1] >= 0 and enemy5_pos[1] < HEIGHT:
		enemy5_pos[1] += SPEED5
	else:
		enemy5_pos[0] = random.randint(0,WIDTH - half + enemy5_size)
		enemy5_pos[1] = 0

	if collision_detection5(player_pos,enemy5_pos):
		game_over = True


	if enemy1_pos[1] >= HEIGHT:
		total_scr += enemy1_scr
		num1 += 1

	if enemy2_pos[1] >= HEIGHT:
		total_scr += enemy2_scr
		num2 += 1

	if enemy3_pos[1] >= HEIGHT:
		total_scr += enemy3_scr
		num3 += 1

	if enemy4_pos[1] >= HEIGHT:
		total_scr += enemy4_scr
		num4 += 1

	if enemy5_pos[1] >= HEIGHT:
		total_scr += enemy5_scr
		num5 += 1

#draw enemy1
	pygame.draw.circle(screen,((enemy1_color)),(enemy1_pos[0],enemy1_pos[1]),rad)

#draw enemy2
	pygame.draw.circle(screen,((enemy2_color)),(enemy2_pos[0],enemy2_pos[1]),rad)

#draw enemy3
	pygame.draw.circle(screen,((enemy3_color)),(enemy3_pos[0],enemy3_pos[1]),rad)

#draw enemy4
	pygame.draw.circle(screen,((enemy4_color)),(enemy4_pos[0],enemy4_pos[1]),rad)

#draw enemy5
	pygame.draw.circle(screen,((enemy5_color)),(enemy5_pos[0],enemy5_pos[1]),rad)

#draw player
	pygame.draw.circle(screen,((player_color)),(int(player_pos[0]),int(player_pos[1])),rad)

#framerate
	clock.tick(30)


#update the display screen
	pygame.display.update()

# message_to_screen("You lose",(0,255,255))
# pygame.display.update()
# time.sleep(2)

print("Purple balls dodged\t",num1,"x",enemy1_scr)
print("Yellow balls dodged\t",num2,"x",enemy2_scr)
print("Cyan balls dodged\t",num3,"x",enemy3_scr)
print("Red balls dodged\t",num4,"x",enemy4_scr)
print("White balls dodged\t",num5,"x",enemy5_scr)
print("Your total score\t",total_scr)

time.sleep(20)


