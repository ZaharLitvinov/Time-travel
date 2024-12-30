import pygame
import sprays

pygame.init()
screen = pygame.display.set_mode((2000, 1000))
running = True
clock = pygame.time.Clock()
Tick = 30
playful_button = sprays.start_button("sprays\\button\\старт.png", 1000, 500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()