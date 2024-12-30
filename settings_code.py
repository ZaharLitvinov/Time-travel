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
        if pygame.mouse.get_focused:
            # Проверка Кнопки старт
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            if int(sizes_x // 3 - 117 // 2) <= mouse_pos_x <= int(117 // 2 + sizes_x // 3) and int(
                    sizes_y // 2 - 130 // 2) <= mouse_pos_y <= int(
                    130 // 2 + sizes_y // 2):  # добавляем текст если мы в размерах кнопки
                playful_button = sprays.sprite_button("sprays\\button\\старт_2.png", int(sizes_x // 3),
                                                      int(sizes_y // 2))

                # Нажата кнопка закрывает этот файл закрываем, а с основной игрой запускаем

                if event.type == pygame.MOUSEBUTTONUP:
                    # тут запуск файла
                    running = False
            else:
                playful_button = sprays.sprite_button("sprays\\button\\старт_1.png", int(sizes_x // 3),
                                                      int(sizes_y // 2))  # не добавляем текст если мы не в размерах кнопки
    pygame.display.flip()
    pygame.time.Clock().tick(360)
pygame.quit()