import pygame
from sys import exit


#Setup Pygame and Screen
pygame.init()
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Ping Pong")

#Player & Ball Position Varibales
left_y_pos = 0
right_y_pos = 0
ball_y_pos = 0
ball_x_pos = 0

"""left_rect = pygame.Rect(30,left_y_pos,10,100)
right_rect = pygame.Rect(770,right_y_pos,10,100)
ball_rect = pygame.Rect(ball_x_pos,ball_y_pos,10,10)"""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if left_y_pos > 0:
                    left_y_pos -= 50
                    print(left_y_pos)
            if event.key == pygame.K_s:
                if left_y_pos < 300:
                    left_y_pos += 50
            if event.key == pygame.K_UP:
                if right_y_pos > 0:
                    right_y_pos -= 50
                    print(right_y_pos)
            if event.key == pygame.K_DOWN:
                if right_y_pos < 300:
                    right_y_pos += 50
            
    
    #Screen Update
    screen.fill("Black")
    #Left Player
    pygame.draw.rect(screen, "White", pygame.Rect(20,left_y_pos,10,100))
   
    #Right Player
    pygame.draw.rect(screen, "White", pygame.Rect(770,right_y_pos,10,100))
    
    #Ball
    pygame.draw.rect(screen, "White", pygame.Rect(ball_x_pos,ball_y_pos,10,10))


    pygame.display.update()
    clock.tick(60)