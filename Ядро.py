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
main_hero = sprays.Player('sprites\\characters\\даниил\\Первое положение.png', 100, 450, 47, 64, True)  # Даниил
moon = sprays.Player('sprites\\characters\\moon.png', 400, 350, 100, 100, False)  # Луна
kira = sprays.Player('sprites\\characters\\кира\\Первое положение.png', 500, 450, 74, 59, False)  # Кира

# Разговор
text = sprays.Speech()

# запуск фона
original_background = pygame.image.load('sprites\\backgrounds\\original background.png')

# основной цикл
start_window = True
game = False
egypt = False
prehistory = True
counter = 0
p_l =pygame.USEREVENT + 25
pygame.time.set_timer(p_l, 10)
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
            if prehistory and (pygame.mouse.get_focused() or event.type == p_l):
                text_t = ['Что за артефакт я нашел, Луна? Он кажется невероятно мощным',
                          'Этот амулет — ключ к древним тайнам. Он может открыть двери в различные эпохи, но помни, его сила значительна, и неправильное использование может привести к разрушениям.',
                          'Как мне узнать, когда и где мне следует использовать его? Вся эта энергия сбивает с толку.',
                          'Разве ты не любишь разгадывать головоломки? Уверена, что у тебя получится! Даниил, с твоими навыками и знаниями о кибернетике мы сможем создать нечто удивительное.',
                          'Но для этого нам нужно понимание временных механизмов. Как я могу перенастроить амулет, чтобы он не раскрылся в самых неподходящих моментах?',
                          'Я могу подсказать, как вписать его в наш кибернетический интерфейс. Сначала нам нужно сохранить его в защищенной среде, пока мы выясним, как работают потоки времени.',
                          'Будьте осторожны. Время — это не линейная стрела, а ткань. Каждое ваше действие может изменить ход истории.',
                          'Пора начать. Давайте откроем эту новую эру вместе!'
                          ]
                if counter == 0:
                    original_background = pygame.image.load('sprites\\backgrounds\\background_dark.jpg')
                    sizes_x, sizes_y = 800, 600  # по размерам изображения
                    screen = pygame.display.set_mode((sizes_x, sizes_y))
                    i = 50
                if counter <= 15 * i:

                    screen.blit(original_background, (0, 0))
                    main_hero.movements(event, screen, True)
                    moon.movements(event, screen, True)
                    kira.movements(event, screen, True)
                    text.draw(text_t[0], main_hero, main_hero.height, main_hero.width, screen)
                    pygame.display.flip()

                if 15 * i < counter <= 30 * i:
                    screen.blit(original_background, (0, 0))
                    main_hero.movements(event, screen, True)
                    moon.movements(event, screen, True)
                    kira.movements(event, screen, True)
                    text.draw(text_t[1], moon, moon.height, moon.width, screen)
                    pygame.display.flip()

                if 30 * i < counter <= 45 * i:
                    screen.blit(original_background, (0, 0))
                    main_hero.movements(event, screen, True)
                    moon.movements(event, screen, True)
                    kira.movements(event, screen, True)
                    text.draw(text_t[2], main_hero, main_hero.height, main_hero.width, screen)
                    pygame.display.flip()

                if 45 * i < counter <= 60 * i:
                    screen.blit(original_background, (0, 0))
                    main_hero.movements(event, screen, True)
                    moon.movements(event, screen, True)
                    kira.movements(event, screen, True)
                    text.draw(text_t[3], kira, kira.height, kira.width, screen)
                    pygame.display.flip()

                if 75 * i < counter <= 90 * i:
                    screen.blit(original_background, (0, 0))
                    main_hero.movements(event, screen, True)
                    moon.movements(event, screen, True)
                    kira.movements(event, screen, True)
                    text.draw(text_t[4], main_hero, main_hero.height, main_hero.width, screen)
                    pygame.display.flip()

                if 90 * i < counter <= 105 * i:
                    screen.blit(original_background, (0, 0))
                    main_hero.movements(event, screen, True)
                    moon.movements(event, screen, True)
                    kira.movements(event, screen, True)
                    text.draw(text_t[5], kira, kira.height, kira.width, screen)
                    pygame.display.flip()

                if 105 * i < counter <= 120 * i:
                    screen.blit(original_background, (0, 0))
                    main_hero.movements(event, screen, True)
                    moon.movements(event, screen, True)
                    kira.movements(event, screen, True)
                    text.draw(text_t[6], moon, moon.height, moon.width, screen)
                    pygame.display.flip()

                if 120 * i < counter <= 135 * i:
                    screen.blit(original_background, (0, 0))
                    main_hero.movements(event, screen, True)
                    moon.movements(event, screen, True)
                    kira.movements(event, screen, True)
                    text.draw(text_t[7], main_hero, main_hero.height, main_hero.width, screen)
                    pygame.display.flip()

                if counter == (135 * i) + 1:
                    prehistory = False
                    egypt = True
                counter += 1
            if egypt:
                screen.fill(color=(255, 255, 255, 255))
        pygame.display.flip()
        pygame.time.Clock().tick(360)

pygame.quit()
