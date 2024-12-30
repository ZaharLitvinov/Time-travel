import pygame
import sprays

pygame.init()
sizes_x, sizes_y = 2000, 1000
screen = pygame.display.set_mode((sizes_x, sizes_y))
running = True
clock = pygame.time.Clock()
Tick = 30
playful_button = sprays.sprite_button("sprays\\button\\старт.png", int(sizes_x // 3), int(sizes_y // 2))
settings_button = sprays.sprite_button("sprays\\button\\настройки.png", int((sizes_x // 3) * 2), int(sizes_y // 2))
exit_button = sprays.sprite_button("sprays\\button\\выход.png", int((sizes_x // 3) * 1.5), int((sizes_y // 2) * 1.5))
original_background = pygame.image.load('sprays\\backgrounds\\original background.png')

while running:
    for event in pygame.event.get():
        screen.blit(original_background, (0, 0))
        screen.blit(playful_button.image, playful_button.rect)
        screen.blit(settings_button.image, settings_button.rect)
        screen.blit(exit_button.image, exit_button.rect)
        pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False
pygame.quit()