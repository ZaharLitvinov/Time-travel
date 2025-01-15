import sprays
import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))
p = sprays.Player('sprays\\characters\\daniil_stepanov.png', 200, 200)

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYUP:
            if pygame.K_d:
                print("Я блин не тут")
                p.movements('d')
        screen.blit(p.image, p.rect)
        pygame.display.flip()
    clock.tick(120)
pygame.quit()