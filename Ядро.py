import pygame_widgets
import time
from pygame_widgets.progressbar import ProgressBar
import pygame
import sprays
from Settings import settings


pygame.init()
sizes_x, sizes_y = 1715, 970   # по размерам изображения
screen = pygame.display.set_mode((sizes_x, sizes_y))
icon = pygame.image.load('sprites\\иконка.png')
pygame.display.set_icon(icon)
running = True

# создания кнопак

playful_button = sprays.Sprite_button("sprites\\button\\старт_1.png", int(sizes_x // 3), int(sizes_y // 2), 117, 130)
settings_button = sprays.Sprite_button("sprites\\button\\настройки_1.png", int((sizes_x // 3) * 2), int(sizes_y // 2), 120, 120)
exit_button = sprays.Sprite_button("sprites\\button\\выход_1.png", int((sizes_x // 3) * 1.5), int((sizes_y // 2) * 1.5), 118, 116)
# Анимация сылки
main_hero_animation_pravo = ['sprites\\characters\\даниил\\даниил_вправо\\1.png',
                             'sprites\\characters\\даниил\\даниил_вправо\\2.png',
                             'sprites\\characters\\даниил\\даниил_вправо\\3.png',
                             'sprites\\characters\\даниил\\даниил_вправо\\4.png',
                             'sprites\\characters\\даниил\\даниил_вправо\\5.png',
                             'sprites\\characters\\даниил\\даниил_вправо\\6.png',
                             'sprites\\characters\\даниил\\даниил_вправо\\7.png',
                             'sprites\\characters\\даниил\\даниил_вправо\\8.png',
                             'sprites\\characters\\даниил\\даниил_вправо\\9.png',
                              ]

main_hero_animation_levo = ['sprites\\characters\\даниил\\даниил_влево\\1.png',
                            'sprites\\characters\\даниил\\даниил_влево\\2.png',
                            'sprites\\characters\\даниил\\даниил_влево\\3.png',
                            'sprites\\characters\\даниил\\даниил_влево\\4.png',
                            'sprites\\characters\\даниил\\даниил_влево\\5.png',
                            'sprites\\characters\\даниил\\даниил_влево\\6.png',
                            'sprites\\characters\\даниил\\даниил_влево\\7.png',
                            'sprites\\characters\\даниил\\даниил_влево\\8.png',
                            'sprites\\characters\\даниил\\даниил_влево\\9.png',
                            ]

citizen_animation_pravo = ['sprites\\characters\\житель\\житель_вправо\\1.png',
                           'sprites\\characters\\житель\\житель_вправо\\2.png',
                           'sprites\\characters\\житель\\житель_вправо\\3.png',
                           'sprites\\characters\\житель\\житель_вправо\\4.png',
                           ]
citizen_animation_levo = ['sprites\\characters\\житель\\житель_влево\\1.png',
                          'sprites\\characters\\житель\\житель_влево\\2.png',
                          'sprites\\characters\\житель\\житель_влево\\3.png',
                          'sprites\\characters\\житель\\житель_влево\\4.png',
                           ]

# Персонаж
main_hero = sprays.Player('sprites\\characters\\даниил\\Первое положение.png', 100, 450, 47, 64, False, 9, main_hero_animation_pravo, main_hero_animation_levo)  # Даниил
moon = sprays.Player('sprites\\characters\\moon.png', 300, 300, 100, 100, False, 0, 0, 0)  # Луна
kira = sprays.Player('sprites\\characters\\кира\\Первое положение.png', 500, 450, 74, 59, False, 0, 0, 0)  # Кира
citizen_1 = sprays.Player('sprites\\characters\\житель\\Первое положение.png', 200, 685, 48, 67, False, 4, citizen_animation_pravo, citizen_animation_levo)
citizen_2 = sprays.Player('sprites\\characters\\житель\\Первое положение.png', 272, 685, 48, 67, False, 4, citizen_animation_pravo, citizen_animation_levo)
citizen_3 = sprays.Player('sprites\\characters\\житель\\Первое положение.png', 344, 685, 48, 67, False, 4, citizen_animation_pravo, citizen_animation_levo)
seller = sprays.Player('sprites\\characters\\торговец\\Первое положение.png', 1000, 685, 46, 65, False, 0, 0, 0)
wiseacre = sprays.Player('sprites\\characters\\мудрец\\мудрец.png', 200, 640, 46, 65, False, 0, 0, 0)
paintress = sprays.Player('sprites\\characters\\художница\\художница.png', 1000, 640, 48, 62, False, 0, 0, 0)
# Разговор
text = sprays.Speech()

# запуск фона
original_background = pygame.image.load('sprites\\backgrounds\\original background.png')

# Флаги и таймер
start_window = True
game = False
egypt = False
prehistory = True
settings1 = False
counter = 0
p_l = pygame.USEREVENT + 25
pygame.time.set_timer(p_l, 10)
draw = []
counter_min = 0
counter_buffer = 0
egypt_one = False
egypt_two = False
ending = False
fps = '250'
count = 0

# основной цикл
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
                        with open('conservation.txt', 'r+', encoding='utf-8') as file:
                            level_check = file.read()
                            if '1' in level_check:
                                prehistory = False
                                egypt = True
                                egypt_one = True
                            if '2' in level_check:
                                prehistory = False
                                egypt = True
                                egypt_one = False
                                egypt_two = True
                            file.close()


                # Проверка Кнопки настроек
                if settings_button.click("sprites\\button\\настройки_2.png", mouse_pos_x, mouse_pos_y):  # добавляем текст если мы в размерах кнопки
                    # Нажата кнопка закрывает этот файл закрываем, а с настройками запускаем

                    if event.type == pygame.MOUSEBUTTONUP:
                        settings1 = True
                        start_window = False

                # Проверка Кнопки выход
                if exit_button.click("sprites\\button\\выход_2.png", mouse_pos_x, mouse_pos_y):  # добавляем текст если мы в размерах кнопки
                    # Нажата кнопка закрывает программу

                    if event.type == pygame.MOUSEBUTTONUP:
                        running = False

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
                    duration = 50
                if counter <= 15 * duration:
                    if 1 == counter:
                        screen.blit(original_background, (0, 0))
                        main_hero.movements(event, screen, prohibition=True)
                        moon.movements(event, screen, prohibition=True)
                        kira.movements(event, screen, prohibition=True)
                        text.draw(text_t[0], main_hero, main_hero.height, main_hero.width, screen)
                    pygame.display.flip()
                    counter = text.click(event, (15 * duration), counter)

                if 15 * duration < counter <= 30 * duration:
                    if (15 * duration) + 1 == counter:
                        screen.blit(original_background, (0, 0))
                        main_hero.movements(event, screen, prohibition=True)
                        moon.movements(event, screen, prohibition=True)
                        kira.movements(event, screen, prohibition=True)
                        text.draw(text_t[1], moon, moon.height, moon.width, screen)
                    pygame.display.flip()
                    counter = text.click(event, (30 * duration), counter)

                if 30 * duration < counter <= 45 * duration:
                    if (30 * duration) + 1 == counter:
                        screen.blit(original_background, (0, 0))
                        main_hero.movements(event, screen, prohibition=True)
                        moon.movements(event, screen, prohibition=True)
                        kira.movements(event, screen, prohibition=True)
                        text.draw(text_t[2], main_hero, main_hero.height, main_hero.width, screen)
                    pygame.display.flip()
                    counter = text.click(event, (45 * duration), counter)

                if 45 * duration < counter <= 75 * duration:
                    if (45 * duration) + 1 == counter:
                        screen.blit(original_background, (0, 0))
                        main_hero.movements(event, screen, prohibition=True)
                        moon.movements(event, screen, prohibition=True)
                        kira.movements(event, screen, prohibition=True)
                        text.draw(text_t[3], kira, kira.height, kira.width, screen)
                    pygame.display.flip()
                    counter = text.click(event, (75 * duration)-2, counter)

                if 75 * duration < counter <= 90 * duration:
                    if (75 * duration) + 1 == counter:
                        screen.blit(original_background, (0, 0))
                        main_hero.movements(event, screen, prohibition=True)
                        moon.movements(event, screen, prohibition=True)
                        kira.movements(event, screen, prohibition=True)
                        text.draw(text_t[4], main_hero, main_hero.height, main_hero.width, screen)
                    pygame.display.flip()
                    counter = text.click(event, (90 * duration), counter)

                if 90 * duration < counter <= 105 * duration:
                    if (90 * duration) + 1 == counter:
                        screen.blit(original_background, (0, 0))
                        main_hero.movements(event, screen, prohibition=True)
                        moon.movements(event, screen, prohibition=True)
                        kira.movements(event, screen, prohibition=True)
                        text.draw(text_t[5], kira, kira.height, kira.width, screen)
                    pygame.display.flip()
                    counter = text.click(event, (105 * duration), counter)

                if 105 * duration < counter <= 120 * duration:
                    if (105 * duration) + 1 == counter:
                        screen.blit(original_background, (0, 0))
                        main_hero.movements(event, screen, prohibition=True)
                        moon.movements(event, screen, prohibition=True)
                        kira.movements(event, screen, prohibition=True)
                        text.draw(text_t[6], moon, moon.height, moon.width, screen)
                    pygame.display.flip()
                    counter = text.click(event, (120 * duration), counter)

                if 120 * duration < counter <= 135 * duration:
                    if (120 * duration) + 1 == counter:
                        screen.blit(original_background, (0, 0))
                        main_hero.movements(event, screen, prohibition=True)
                        moon.movements(event, screen, prohibition=True)
                        kira.movements(event, screen, prohibition=True)
                        text.draw(text_t[7], main_hero, main_hero.height, main_hero.width, screen)
                    pygame.display.flip()
                    counter = text.click(event, 135 * duration, counter)

                if counter == (135 * duration) + 1:
                    with open('conservation.txt', 'w', encoding='utf-8') as file:
                        file.write('1')
                        file.close()
                    prehistory = False
                    egypt = True
                    egypt_one = True
                    counter = 0
                else:
                    counter += 1

            if egypt and (pygame.mouse.get_focused() or event.type == p_l):
                if egypt_one and (pygame.mouse.get_focused() or event.type == p_l):
                    text_t = ['Слышал, что фараон собирает армию, чтобы завоевать соседние земли!',
                              'Да, но у него есть другие проблемы. Новый закон требует жертву для богов. Люди боятся!',
                              'Надеюсь, это не коснется нас! Мы просто хотим жить мирно.',
                              'О, юноша! Ты не местный? У нас есть чудесные артефакты из самых чистых песков пустыни!',
                              'Что за артефакты ты предлагаешь?',
                              'Скарабеи удачи, священные амулеты и даже драгоценные камни, которые раньше принадлежали фараонов!',
                              'Но у меня нет золота, чтобы купить что-либо...',
                              'Ну, строить бизнес здесь – это не только загребать деньги, но и заключать сделки! Ты, возможно, можешь помочь мне найти что-то ценное в пирамиде.']
                    if counter == 0:
                        original_background = pygame.image.load('sprites\\backgrounds\\egypt_background (2).png')
                        sizes_x, sizes_y = 1340, 890  # по размерам изображения
                        screen = pygame.display.set_mode((sizes_x, sizes_y))
                        duration = 50

                        startTime = time.time()
                        progressBar = ProgressBar(screen, 370, 715, 500, 40, lambda: 1 - (time.time() - startTime) / 10,
                                                  curved=True)
                        main_hero.pos_y = 685

                    if counter <= 465:
                        screen.blit(original_background, (0, 0))
                        pygame_widgets.update(event)
                        pygame.display.update()

                    if counter == 466:
                        progressBar = 0
                        original_background = pygame.image.load('sprites\\backgrounds\\first_egypt_background.PNG')
                        sizes_x, sizes_y = 1456, 816  # по размерам изображения
                        screen = pygame.display.set_mode((sizes_x, sizes_y))
                        duration = 50

                    if 466 <= counter <= 466 + 15 * duration:
                        if 467 == counter:
                            screen.blit(original_background, (0, 0))
                            citizen_1.movements(event, screen, prohibition=True)
                            citizen_2.movements(event, screen, prohibition=True)
                            citizen_3.movements(event, screen, prohibition=True)
                            seller.movements(event, screen, prohibition=True)
                            main_hero.movements(event, screen, prohibition=True)

                            text.draw(text_t[0], citizen_1, citizen_1.height, citizen_1.width, screen)
                        counter = text.click(event, (466 + (15 * duration)-2), counter)

                        pygame.display.flip()

                    if 466 + 15 * duration <= counter <= 466 + 30 * duration:
                        if 466 + 15 * duration == counter:
                            screen.blit(original_background, (0, 0))
                            citizen_1.movements(event, screen, prohibition=True)
                            citizen_2.movements(event, screen, prohibition=True)
                            citizen_3.movements(event, screen, prohibition=True)
                            seller.movements(event, screen, prohibition=True)
                            main_hero.movements(event, screen, prohibition=True)

                            text.draw(text_t[1], citizen_2, citizen_1.height, citizen_1.width, screen)
                        counter = text.click(event, (466 + (30 * duration)-2), counter)
                        pygame.display.flip()

                    if 466 + 30 * duration <= counter <= 466 + 45 * duration:
                        if 466 + 30 * duration == counter:
                            screen.blit(original_background, (0, 0))
                            citizen_1.movements(event, screen, prohibition=True)
                            citizen_2.movements(event, screen, prohibition=True)
                            citizen_3.movements(event, screen, prohibition=True)
                            seller.movements(event, screen, prohibition=True)
                            main_hero.movements(event, screen, prohibition=True)

                            text.draw(text_t[2], citizen_3, citizen_1.height, citizen_1.width, screen)
                        counter = text.click(event, (466 + (45 * duration)-2), counter)
                        pygame.display.flip()

                    if counter >= 466 + 45 * duration and main_hero.pos_x <= 900:
                        if counter_min == 0:
                            screen.blit(original_background, (0, 0))
                            main_hero.movements(event, screen, background=original_background, draw=[citizen_1, citizen_2, citizen_3, seller], display_x=sizes_x)
                        counter_min += 1
                    if main_hero.pos_x <= 30:
                        main_hero.pos_x = 31
                    if counter_buffer == 0 and main_hero.pos_x >= 900:
                        counter_buffer = counter
                    if counter_min == 1:
                        counter_min = 0

                    if counter_buffer <= counter <= counter_buffer + 15 * duration and counter_buffer != 0:
                        if counter_buffer == counter:
                            screen.blit(original_background, (0, 0))
                            citizen_1.movements(event, screen, prohibition=True)
                            citizen_2.movements(event, screen, prohibition=True)
                            citizen_3.movements(event, screen, prohibition=True)
                            seller.movements(event, screen, prohibition=True)
                            main_hero.movements(event, screen, prohibition=True)
                            text.draw(text_t[3], seller, seller.height, seller.width, screen)
                        counter = text.click(event, (counter_buffer + (15 * duration) - 2), counter)

                    if counter_buffer + 15 * duration <= counter <= counter_buffer + 30 * duration and counter_buffer != 0:
                        if counter_buffer + 15 * duration == counter:
                            screen.blit(original_background, (0, 0))
                            citizen_1.movements(event, screen, prohibition=True)
                            citizen_2.movements(event, screen, prohibition=True)
                            citizen_3.movements(event, screen, prohibition=True)
                            seller.movements(event, screen, prohibition=True)
                            main_hero.movements(event, screen, prohibition=True)
                            text.draw(text_t[4], main_hero, main_hero.height, main_hero.width, screen)
                        counter = text.click(event, (counter_buffer + (30 * duration) - 2), counter)

                    if counter_buffer + 30 * duration <= counter <= counter_buffer + 45 * duration and counter_buffer != 0:
                        if counter_buffer + 30 * duration == counter:
                            screen.blit(original_background, (0, 0))
                            citizen_1.movements(event, screen, prohibition=True)
                            citizen_2.movements(event, screen, prohibition=True)
                            citizen_3.movements(event, screen, prohibition=True)
                            seller.movements(event, screen, prohibition=True)
                            main_hero.movements(event, screen, prohibition=True)
                            text.draw(text_t[5], seller, seller.height, seller.width, screen)
                        counter = text.click(event, (counter_buffer + (45 * duration) - 2), counter)

                    if counter_buffer + 45 * duration <= counter <= counter_buffer + 60 * duration and counter_buffer != 0:
                        if counter_buffer + 45 * duration == counter:
                            screen.blit(original_background, (0, 0))
                            citizen_1.movements(event, screen, prohibition=True)
                            citizen_2.movements(event, screen, prohibition=True)
                            citizen_3.movements(event, screen, prohibition=True)
                            seller.movements(event, screen, prohibition=True)
                            main_hero.movements(event, screen, prohibition=True)
                            text.draw(text_t[6], main_hero, main_hero.height, main_hero.width, screen)
                        counter = text.click(event, (counter_buffer + (60 * duration) - 2), counter)

                    if counter_buffer + 60 * duration <= counter <= counter_buffer + 75 * duration and counter_buffer != 0:
                        if counter_buffer + 60 * duration == counter:
                            screen.blit(original_background, (0, 0))
                            citizen_1.movements(event, screen, prohibition=True)
                            citizen_2.movements(event, screen, prohibition=True)
                            citizen_3.movements(event, screen, prohibition=True)
                            seller.movements(event, screen, prohibition=True)
                            main_hero.movements(event, screen, prohibition=True)
                            text.draw(text_t[7], seller, seller.height, seller.width, screen)
                        counter = text.click(event, (counter_buffer + (75 * duration) - 2), counter)

                    pygame.display.flip()
                    counter += 1
                    if counter >= counter_buffer + 75 * duration and counter_buffer != 0:
                        egypt_one = False
                        egypt_two = True
                        counter = 0
                        with open('conservation.txt', 'w', encoding='utf-8') as file:
                            file.write('2')
                            file.close()

                if egypt_two:
                    text_t = ['Скоро в святилище сберут жертв. Ты не знаешь, каково это быть в их шкуре, но подходит умный... Что ты ищешь в Египте, путник?',
                              'Я ищу древний артефакт в пирамиде. Как мне туда попасть?',
                              'Ты должен расшифровать древние иероглифы, которые охраняют вход. Могу помочь тебе, если принесешь священный свиток.',
                              'Привет! Ты выглядишь рассеянным. Что привело тебя в этот мир? Хочешь увидеть моё искусство?',
                              'Я ищу артефакт, который поможет мне вернуться домой.',
                              'Погоди, мой друг! Если ты умеешь читать иероглифы, возможно, я смогу показать некоторые старинные изображения, которые помогут тебе!',
                              'Это невероятно! Может, они укажут мне путь?']
                    if counter == 0:

                        original_background = pygame.image.load('sprites\\backgrounds\\egypt_background.png')
                        sizes_x, sizes_y = 1340, 890  # по размерам изображения
                        screen = pygame.display.set_mode((sizes_x, sizes_y))
                        duration = 50
                        startTime = time.time()
                        progressBar = ProgressBar(screen, 370, 715, 500, 40, lambda: 1 - (time.time() - startTime) / 10,
                                                  curved=True)
                        main_hero.pos_y = 685

                    if counter <= 465:
                        screen.blit(original_background, (0, 0))
                        pygame_widgets.update(event)
                        pygame.display.update()

                    if counter == 466:
                        progressBar = 0
                        original_background = pygame.image.load('sprites\\backgrounds\\египет.jpg')
                        sizes_x, sizes_y = 1280, 717  # по размерам изображения
                        screen = pygame.display.set_mode((sizes_x, sizes_y))
                        duration = 50
                        screen.blit(original_background, (0, 0))
                        main_hero.movements(event, screen, prohibition=True)
                        wiseacre.movements(event, screen, prohibition=True)
                        paintress.movements(event, screen, prohibition=True)
                        main_hero.pos_x = 100
                        main_hero.pos_y = 640

                    if 466 <= counter <= 466 + 15 * duration:
                        if counter == 466:
                            screen.blit(original_background, (0, 0))
                            main_hero.movements(event, screen, prohibition=True)
                            wiseacre.movements(event, screen, prohibition=True)
                            paintress.movements(event, screen, prohibition=True)
                            text.draw(text_t[0], wiseacre, wiseacre.height, wiseacre.width, screen)
                        counter = text.click(event, (466 + (15 * duration) - 2), counter)

                    if 466 + 15 * duration <= counter <= 466 + 30 * duration:
                        if 466 + 15 * duration == counter:
                            screen.blit(original_background, (0, 0))
                            main_hero.movements(event, screen, prohibition=True)
                            wiseacre.movements(event, screen, prohibition=True)
                            paintress.movements(event, screen, prohibition=True)
                            text.draw(text_t[1], main_hero, main_hero.height, main_hero.width, screen)
                        counter = text.click(event, (466 + (30 * duration) - 2), counter)

                    if 466 + 30 * duration <= counter <= 466 + 45 * duration:
                        if 466 + 30 * duration == counter:
                            screen.blit(original_background, (0, 0))
                            main_hero.movements(event, screen, prohibition=True)
                            wiseacre.movements(event, screen, prohibition=True)
                            paintress.movements(event, screen, prohibition=True)
                            text.draw(text_t[2], wiseacre, wiseacre.height, wiseacre.width, screen)
                        counter = text.click(event, (466 + (45 * duration) - 2), counter)
                    if counter >= 466 + 45 * duration and main_hero.pos_x <= 900:
                        if counter_min == 0:
                            screen.blit(original_background, (0, 0))
                            main_hero.movements(event, screen, background=original_background,
                                                draw=[wiseacre, paintress], display_x=sizes_x)
                        counter_min += 1
                    if main_hero.pos_x <= 30:
                        main_hero.pos_x = 31
                    if counter_buffer == 0 and main_hero.pos_x >= 900:
                        counter_buffer = counter
                    if counter_min == 1:
                        counter_min = 0

                    if counter_buffer <= counter <= counter_buffer + 15 * duration and counter_buffer != 0:
                        if counter_buffer == counter:
                            screen.blit(original_background, (0, 0))
                            wiseacre.movements(event, screen, prohibition=True)
                            main_hero.movements(event, screen, prohibition=True)
                            paintress.movements(event, screen, prohibition=True)
                            text.draw(text_t[3], seller, seller.height, seller.width, screen)
                        counter = text.click(event, (counter_buffer + (15 * duration) - 2), counter)

                    if counter_buffer + 15 * duration <= counter <= counter_buffer + 30 * duration and counter_buffer != 0:
                        if counter_buffer + 15 * duration == counter:
                            screen.blit(original_background, (0, 0))
                            wiseacre.movements(event, screen, prohibition=True)
                            main_hero.movements(event, screen, prohibition=True)
                            paintress.movements(event, screen, prohibition=True)
                            text.draw(text_t[4], seller, seller.height, seller.width, screen)
                        counter = text.click(event, (counter_buffer + (30 * duration) - 2), counter)

                    if counter_buffer + 30 * duration <= counter <= counter_buffer + 45 * duration and counter_buffer != 0:
                        if counter_buffer + 30 * duration == counter:
                            screen.blit(original_background, (0, 0))
                            wiseacre.movements(event, screen, prohibition=True)
                            main_hero.movements(event, screen, prohibition=True)
                            paintress.movements(event, screen, prohibition=True)
                            text.draw(text_t[5], seller, seller.height, seller.width, screen)
                        counter = text.click(event, (counter_buffer + (45 * duration) - 2), counter)

                    if counter_buffer + 45 * duration <= counter <= counter_buffer + 50 * duration and counter_buffer != 0:
                        if counter_buffer + 45 * duration == counter:
                            screen.blit(original_background, (0, 0))
                            wiseacre.movements(event, screen, prohibition=True)
                            main_hero.movements(event, screen, prohibition=True)
                            paintress.movements(event, screen, prohibition=True)
                            text.draw(text_t[6], seller, seller.height, seller.width, screen)
                        counter = text.click(event, (counter_buffer + (50 * duration) - 2), counter)

                    if counter == (counter_buffer + 50 * duration) + 1 and counter_buffer != 0:
                        egypt_two = False
                        ending = True
                        egypt = False
                        counter = 0
                    counter += 1

        if ending:
            screen.fill((0, 0, 0, 255))
            font = pygame.font.SysFont("comicsansms", 100)
            text_surface = font.render('Продолжение следует', True, (255, 255, 255, 255))  # Создаем поверхность текста
            screen.blit(text_surface, (100, 100))
            pygame.display.flip()

        if settings1:
            settings1, fps, count = settings(fps, count)
            if settings1 == False:
                start_window = True
            continue
            

        pygame.display.flip()
        pygame.time.Clock().tick(int(fps))

pygame.quit()
