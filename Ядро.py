import pygame
import sprays

pygame.init()
sizes_x, sizes_y = int(input()), int(input())
screen = pygame.display.set_mode((sizes_x, sizes_y))
running = True
clock = pygame.time.Clock()
Tick = 30
playful_button = sprays.sprite_button("sprays\\button\\старт.png", int(sizes_x // 3), int(sizes_y // 2))
_button = sprays.sprite_button("sprays\\button\\старт.png", int(sizes_x // 3), int(sizes_y // 2))
sprays.sprite_button("sprays\\button\\старт.png", int(sizes_x // 3), int(sizes_y // 2))


while running:
    for event in pygame.event.get():
        screen.blit(playful_button.image, playful_button.rect)
        pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False
pygame.quit()