import pygame
import sprays

pygame.init()
sizes_x, sizes_y = 1715, 970
screen = pygame.display.set_mode((sizes_x, sizes_y))
running = True
clock = pygame.time.Clock()
Tick = 30
playful_button = sprays.sprite_button("sprays\\button\\старт_1.png", int(sizes_x // 3), int(sizes_y // 2))
settings_button = sprays.sprite_button("sprays\\button\\настройки.png", int((sizes_x // 3) * 2), int(sizes_y // 2))
exit_button = sprays.sprite_button("sprays\\button\\выход.png", int((sizes_x // 3) * 1.5), int((sizes_y // 2) * 1.5))
original_background = pygame.image.load('sprays\\backgrounds\\original background.png')

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_focused():
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            if int(sizes_x // 3) <= mouse_pos_x <= (117+int(sizes_x // 3)) and int(sizes_y // 2) <= mouse_pos_y <= (130 + int(sizes_y // 2)):
                playful_button = sprays.sprite_button("sprays\\button\\старт_2.png", int(sizes_x // 3), int(sizes_y // 2))

            else:
                playful_button = sprays.sprite_button("sprays\\button\\старт_1.png", int(sizes_x // 3), int(sizes_y // 2))

        screen.blit(original_background, (0, 0))
        screen.blit(playful_button.image, playful_button.rect)
        screen.blit(settings_button.image, settings_button.rect)
        screen.blit(exit_button.image, exit_button.rect)
        pygame.display.flip()
pygame.quit()