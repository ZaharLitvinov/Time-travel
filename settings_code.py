import pygame
import sprays

pygame.init()
sizes_x, sizes_y = 956, 529   # по размерам изображения
screen = pygame.display.set_mode((sizes_x, sizes_y))
icon = pygame.image.load('sprays\\button\\старт_1.png')
pygame.display.set_icon(icon)
running = True
original_background = pygame.image.load('sprays\\backgrounds\\original background2.png')
screen.blit(original_background, (0, 0))
pygame.display.flip()

sound_button = sprays.sprite_button("sprays\\button\\Звук_1.png", int(sizes_x // 9), int(sizes_y // 7))

while running:
    for event in pygame.event.get():
        screen.blit(sound_button.image, sound_button.rect)
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    pygame.time.Clock().tick(360)
pygame.quit()