import pygame

pygame.init()
sizes_x, sizes_y = 956, 529   # по размерам изображения
screen = pygame.display.set_mode((sizes_x, sizes_y))
icon = pygame.image.load('sprays\\button\\старт_1.png')
pygame.display.set_icon(icon)
running = True
original_background = pygame.image.load('sprays\\backgrounds\\original background2.png')
screen.blit(original_background, (0, 0))
pygame.display.flip()
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

pygame.quit()