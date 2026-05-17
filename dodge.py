import pygame
pygame.init()

WIDTH = 600
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))

screen.fill("purple")

space = pygame.image.load("lesson 6 - space dodge/images/space.png")
ship = pygame.image.load("lesson 6 - space dodge/images/spaceship_yellow.png")
asteroid = pygame.image.load("lesson 6 - space dodge/images/asteroid.png")
shipt = pygame.transform.scale(ship,(90,80))

yellow = pygame.Rect(300,700,90,80)

SHealth = 10

def Move():
    if keys_pressed[pygame.K_a] and yellow.x> 0:
        yellow.x -= 3.5
    if keys_pressed[pygame.K_d] and yellow.x< 510:
        yellow.x += 3.5


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(space,(0,0))
    screen.blit(shipt,yellow)
    keys_pressed = pygame.key.get_pressed()
    Move()
    pygame.display.update()