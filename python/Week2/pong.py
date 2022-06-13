import pygame, sys

pygame.init() #initiates pygame modules and is required in all pygame projects

clock = pygame.time.Clock()

screen_width = 1280
screen_height = 560

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Pong")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



