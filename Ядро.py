import pygame
import sprays

pygame.init()
sizes_x, sizes_y = 1715, 970   # по размерам изображения
screen = pygame.display.set_mode((sizes_x, sizes_y))
icon = pygame.image.load('sprays\\button\\старт_1.png')
pygame.display.set_icon(icon)
running = True

# создания кнопак

playful_button = sprays.Sprite_button("sprays\\button\\старт_1.png", int(sizes_x // 3), int(sizes_y // 2), 117, 130)
settings_button = sprays.Sprite_button("sprays\\button\\настройки_1.png", int((sizes_x // 3) * 2), int(sizes_y // 2), 120, 120)
exit_button = sprays.Sprite_button("sprays\\button\\выход_1.png", int((sizes_x // 3) * 1.5), int((sizes_y // 2) * 1.5), 118, 116)

# запуск фона

original_background = pygame.image.load('sprays\\backgrounds\\original background.png')

# основной цикл
start_window = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if start_window:
            # если мышка на дисплеи
            if pygame.mouse.get_focused:
                # Проверка Кнопки старт
                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                if playful_button.click("sprays\\button\\старт_2.png", mouse_pos_x, mouse_pos_y):  # добавляем текст если мы в размерах кнопки

                    # Нажата кнопка закрывает этот файл закрываем, а с основной игрой запускаем

                    if event.type == pygame.MOUSEBUTTONUP:
                        # тут запуск файла
                        start_window = False

                # Проверка Кнопки настроек
                if settings_button.click("sprays\\button\\настройки_2.png", mouse_pos_x, mouse_pos_y):  # добавляем текст если мы в размерах кнопки
                    # Нажата кнопка закрывает этот файл закрываем, а с настройками запускаем

                    if event.type == pygame.MOUSEBUTTONUP:
                        start_window = False

                # Проверка Кнопки выход
                if exit_button.click("sprays\\button\\выход_2.png", mouse_pos_x, mouse_pos_y):  # добавляем текст если мы в размерах кнопки
                    # Нажата кнопка закрывает программу

                    if event.type == pygame.MOUSEBUTTONUP:
                        start_window = False

            screen.blit(original_background, (0, 0))
            screen.blit(playful_button.image, playful_button.rect)
            screen.blit(settings_button.image, settings_button.rect)
            screen.blit(exit_button.image, exit_button.rect)
        else:
            screen.fill(color=(0, 0, 0, 255))

        pygame.display.flip()
        pygame.time.Clock().tick(360)
pygame.quit()