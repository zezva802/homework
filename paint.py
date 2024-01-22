import pygame

pygame.init()

width = 500
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()