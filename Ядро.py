import pygame
import sprays
import subprocess

pygame.init()
sizes_x, sizes_y = 1715, 970   # по размерам изображения
screen = pygame.display.set_mode((sizes_x, sizes_y))
icon = pygame.image.load('sprays\\button\\старт_1.png')
pygame.display.set_icon(icon)
running = True

# создания кнопак

playful_button = sprays.sprite_button("sprays\\button\\старт_1.png", int(sizes_x // 3), int(sizes_y // 2))
settings_button = sprays.sprite_button("sprays\\button\\настройки_1.png", int((sizes_x // 3) * 2), int(sizes_y // 2))
exit_button = sprays.sprite_button("sprays\\button\\выход_1.png", int((sizes_x // 3) * 1.5), int((sizes_y // 2) * 1.5))

# запуск фона

original_background = pygame.image.load('sprays\\backgrounds\\original background.png')

# основной цикл

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        # если мышка на дисплеи
        if pygame.mouse.get_focused:
            # Проверка Кнопки старт
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            if int(sizes_x // 3 - 117 // 2) <= mouse_pos_x <= int(117//2+sizes_x // 3) and int(sizes_y // 2 - 130 // 2) <= mouse_pos_y <= int(130 // 2 + sizes_y // 2):  # добавляем текст если мы в размерах кнопки
                playful_button = sprays.sprite_button("sprays\\button\\старт_2.png", int(sizes_x // 3), int(sizes_y // 2))

                # Нажата кнопка закрывает этот файл закрываем, а с основной игрой запускаем

                if event.type == pygame.MOUSEBUTTONUP:
                    # тут запуск файла
                    running = False
            else:
                playful_button = sprays.sprite_button("sprays\\button\\старт_1.png", int(sizes_x // 3), int(sizes_y // 2))  # не добавляем текст если мы не в размерах кнопки

            # Проверка Кнопки настроек
            if int(sizes_x // 3 * 2 - 120 // 2) <= mouse_pos_x <= int(120//2+(sizes_x // 3 * 2)) and int((sizes_y // 2) - 120 // 2) <= mouse_pos_y <= int((120 // 2) + sizes_y // 2):  # добавляем текст если мы в размерах кнопки
                settings_button = sprays.sprite_button("sprays\\button\\настройки_2.png", int((sizes_x // 3) * 2), int(sizes_y // 2))

                # Нажата кнопка закрывает этот файл закрываем, а с основной игрой запускаем

                if event.type == pygame.MOUSEBUTTONUP:
                    running = False
                    subprocess.run(['python', 'settings_code.py'])
            else:
                settings_button = sprays.sprite_button("sprays\\button\\настройки_1.png", int((sizes_x // 3) * 2), int(sizes_y // 2))  # не добавляем текст если мы не в размерах кнопки

            # Проверка Кнопки выход
            if int((sizes_x // 3) * 1.5 - 120 // 2) <= mouse_pos_x <= int(120 // 2 + (sizes_x // 3) * 1.5) and int(((sizes_y // 2) * 1.5) - 120 // 2) <= mouse_pos_y <= int(((sizes_y // 2) * 1.5) + sizes_y // 2):  # добавляем текст если мы в размерах кнопки
                exit_button = sprays.sprite_button("sprays\\button\\выход_2.png", int((sizes_x // 3) * 1.5), int((sizes_y // 2) * 1.5))

                # Нажата кнопка закрывает этот файл закрываем, а с основной игрой запускаем

                if event.type == pygame.MOUSEBUTTONUP:
                    running = False

            else:
                exit_button = sprays.sprite_button("sprays\\button\\выход_1.png", int((sizes_x // 3) * 1.5), int((sizes_y // 2) * 1.5))  # не добавляем текст если мы не в размерах кнопки

        screen.blit(original_background, (0, 0))
        screen.blit(playful_button.image, playful_button.rect)
        screen.blit(settings_button.image, settings_button.rect)
        screen.blit(exit_button.image, exit_button.rect)
        pygame.display.flip()
        pygame.time.Clock().tick(360)
pygame.quit()