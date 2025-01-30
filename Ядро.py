from traceback import print_tb

import pygame
import sprays

pygame.init()
sizes_x, sizes_y = 1715, 970   # по размерам изображения
screen = pygame.display.set_mode((sizes_x, sizes_y))
# icon = pygame.image.load('sprays\\button\\старт_1.png')
# pygame.display.set_icon(icon)
running = True

# создания кнопак

playful_button = sprays.Sprite_button("sprites\\button\\старт_1.png", int(sizes_x // 3), int(sizes_y // 2), 117, 130)
settings_button = sprays.Sprite_button("sprites\\button\\настройки_1.png", int((sizes_x // 3) * 2), int(sizes_y // 2), 120, 120)
exit_button = sprays.Sprite_button("sprites\\button\\выход_1.png", int((sizes_x // 3) * 1.5), int((sizes_y // 2) * 1.5), 118, 116)

# Персонаж
main_hero = sprays.Player('sprites\\characters\\даниил\\Первое положение.png', 100, 450, 47, 64)  # Даниил
moon = sprays.Player('sprites\\characters\\moon.png', 400, 350, 100, 100,)  # Луна
kira = sprays.Player('sprites\\characters\\кира\\Первое положение.png', 500, 450, 74, 59)  # Кира

# Разговор
text = sprays.Speech()

# запуск фона
original_background = pygame.image.load('sprites\\backgrounds\\original background.png')

# основной цикл
start_window = True
game = False
egypt = False
prehistory = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if start_window:
            # если мышка на дисплеи
            if pygame.mouse.get_focused:
                # Проверка Кнопки старт
                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                if playful_button.click("sprites\\button\\старт_2.png", mouse_pos_x, mouse_pos_y):  # добавляем текст если мы в размерах кнопки

                    # Нажата кнопка закрывает этот файл закрываем, а с основной игрой запускаем

                    if event.type == pygame.MOUSEBUTTONUP:
                        game = True
                        start_window = False


                # Проверка Кнопки настроек
                if settings_button.click("sprites\\button\\настройки_2.png", mouse_pos_x, mouse_pos_y):  # добавляем текст если мы в размерах кнопки
                    # Нажата кнопка закрывает этот файл закрываем, а с настройками запускаем

                    if event.type == pygame.MOUSEBUTTONUP:
                        start_window = False

                # Проверка Кнопки выход
                if exit_button.click("sprites\\button\\выход_2.png", mouse_pos_x, mouse_pos_y):  # добавляем текст если мы в размерах кнопки
                    # Нажата кнопка закрывает программу

                    if event.type == pygame.MOUSEBUTTONUP:
                        start_window = False

            screen.blit(original_background, (0, 0))
            screen.blit(playful_button.image, playful_button.rect)
            screen.blit(settings_button.image, settings_button.rect)
            screen.blit(exit_button.image, exit_button.rect)
            if not start_window:
                screen.fill(color=(0, 0, 0, 255))

        if game:
            if prehistory:
                original_background = pygame.image.load('sprites\\backgrounds\\background_dark.jpg')
                sizes_x, sizes_y = 800, 600  # по размерам изображения
                screen = pygame.display.set_mode((sizes_x, sizes_y))
                screen.blit(original_background, (0, 0))
                main_hero.movements(event, screen, False)
                moon.movements(event, screen)
                kira.movements(event, screen)
                text.draw('Что за артефакт я нашел, Луна? Он кажется невероятно мощным', main_hero, main_hero.height, main_hero.width, screen)
                pygame.display.flip()
                pygame.time.delay(5000)

                screen.blit(original_background, (0, 0))
                main_hero.movements(event, screen, False)
                moon.movements(event, screen)
                kira.movements(event, screen)
                text.draw('Этот амулет — ключ к древним тайнам. Он может открыть двери в различные эпохи, но помни, его сила значительна, и неправильное использование может привести к разрушениям.', moon, moon.height, moon.width, screen)
                pygame.display.flip()
                pygame.time.delay(15000)

                screen.blit(original_background, (0, 0))
                main_hero.movements(event, screen, False)
                moon.movements(event, screen)
                kira.movements(event, screen)
                text.draw('Как мне узнать, когда и где мне следует использовать его? Вся эта энергия сбивает с толку.', main_hero, main_hero.height, main_hero.width, screen)
                pygame.display.flip()
                pygame.time.delay(15000)
                screen.blit(original_background, (0, 0))
                main_hero.movements(event, screen, False)
                moon.movements(event, screen)
                kira.movements(event, screen)
                text.draw('Как мне узнать, когда и где мне следует использовать его? Вся эта энергия сбивает с толку.',
                          main_hero, main_hero.height, main_hero.width, screen)
                pygame.display.flip()
                pygame.time.delay(15000)

                screen.blit(original_background, (0, 0))
                main_hero.movements(event, screen, False)
                moon.movements(event, screen)
                kira.movements(event, screen)
                text.draw('Разве ты не любишь разгадывать головоломки? Уверена, что у тебя получится! Даниил, с твоими навыками и знаниями о кибернетике мы сможем создать нечто удивительное.',
                          kira, kira.height, kira.width, screen)
                pygame.display.flip()
                pygame.time.delay(5000)
                prehistory = False
                egypt = True
            if egypt:
                screen.fill(color=(255, 255, 255, 255))
        pygame.display.flip()
        pygame.time.Clock().tick(60)

pygame.quit()
