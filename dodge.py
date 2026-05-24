import pygame
import random
pygame.init()

WIDTH = 600
HEIGHT = 800

FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill("purple")

space = pygame.image.load("lesson 6 - space dodge/images/space.png")
ship = pygame.image.load("lesson 6 - space dodge/images/spaceship_yellow.png")
asteroid = pygame.image.load("lesson 6 - space dodge/images/asteroid.png")
shipt = pygame.transform.scale(ship,(90,80))
asteroidt = pygame.transform.scale(asteroid,(80,80))

yellow = pygame.Rect(300,700,90,80)

scorevalue = 0

font = pygame.font.SysFont("bradleyhand",30)




def Move():
    if keys_pressed[pygame.K_a] and yellow.x> 0:
        yellow.x -= 5
    if keys_pressed[pygame.K_d] and yellow.x< 510:
        yellow.x += 5

meteorgroup = []

def Meteor():
    x = random.randint(0,600)
    y = 0
    rect = pygame.Rect(x,y,80,80)
    meteorgroup.append(rect)

    
spawntimer = 0
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(space,(0,0))
    score = font.render("Score:" + str(scorevalue),True,"white")
    screen.blit(score,(5,5))
    screen.blit(shipt,yellow)
    keys_pressed = pygame.key.get_pressed()
    Move()
    spawntimer +=1
    if spawntimer >= 70:
        Meteor()
        spawntimer = 0
    for i in meteorgroup:
        screen.blit(asteroidt,i)
    for ast in meteorgroup[:]:
        ast.y +=5
        if ast.y > 800:
            meteorgroup.remove(ast)
            scorevalue +=1
    pygame.display.update()