import pygame

# кнопки
class Sprite_button(pygame.sprite.Sprite):
    def __init__(self, file_path, pos_x, pos_y, height, width):
        pygame.sprite.Sprite.__init__(self)
        self.file_path_global = file_path
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

    def click(self, file_path, mouse_pos_x, mouse_pos_y):
        if self.pos_x - (self.width / 2) <= mouse_pos_x <= self.pos_x + (self.width / 2) and self.pos_y - (self.height / 2) <= mouse_pos_y <= self.pos_y + (self.height / 2):
            self.image = pygame.image.load(file_path)
            self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
            return True
        else:
            self.image = pygame.image.load(self.file_path_global)
            self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

class Player(pygame.sprite.Sprite):
    def __init__(self, file_path, pos_x, pos_y, height, width, prohibition, Number_of_elements, pravo_animation, levo_animation, right='d', left='a'):
        pygame.sprite.Sprite.__init__(self)

        # позиция размеры и картинка

        self.file_path_global = file_path
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.prohibition = prohibition
        self.team = ''

        # Кнопки

        self.right = right
        self.left = left

        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

        # Анимац
        self.number_of_elements = Number_of_elements
        self.pravo_animation = pravo_animation
        self.levo_animation = levo_animation

    # если нажата кнопка

    def movements(self, event, display, team='',  background='', draw=[], prohibition=False, display_x=10000):
        if self.prohibition or prohibition:
            self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
            display.blit(self.image, self.rect)
        else:
            if self.number_of_elements == 0:
                if event.type == pygame.KEYUP:
                    if event.unicode.lower() == self.right:
                        self.pos_x += 5
                    if event.unicode.lower() == self.left:
                        self.pos_x -= 5

                    self.image = pygame.image.load(self.file_path_global)
                    self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
                    display.blit(self.image, self.rect)
                    pygame.display.flip()

                else:
                    if event.type == pygame.TEXTINPUT:
                        if event.text.lower() == self.right:
                            self.pos_x += 5
                        if event.text.lower() == self.left:
                            self.pos_x -= 5
                        self.image = pygame.image.load(self.file_path_global)
                        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
                        display.blit(self.image, self.rect)
                        pygame.display.flip()

            else:
                if (event.type == pygame.TEXTINPUT and event.text.lower() == self.right) or (event.type == pygame.KEYUP and event.unicode.lower() == self.right) or (len(team) != 0 and team == self.right):
                    counter = 0
                    for i in range(self.number_of_elements * 20):

                        if i % 20 == 0:
                            file_path = self.pravo_animation[counter]
                            self.pos_x += 5
                            counter += 1

                        self.image = pygame.image.load(file_path)
                        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
                        display.blit(background, (0, 0))
                        display.blit(self.image, self.rect)
                        if len(draw) != 0:
                            for draw_i in draw:
                                display.blit(draw_i.image, draw_i.rect)
                        pygame.display.flip()
                elif (event.type == pygame.TEXTINPUT and event.text.lower() == self.left) or (event.type == pygame.KEYUP and event.unicode.lower() == self.left) or (len(team) != 0 and team == self.left):
                    counter = 0
                    for i in range(self.number_of_elements * 20):

                        if i % 20 == 0:
                            file_path = self.levo_animation[counter]
                            self.pos_x -= 5
                            counter += 1
                        self.image = pygame.image.load(file_path)
                        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
                        display.blit(background, (0, 0))
                        display.blit(self.image, self.rect)
                        if len(draw) != 0:
                            for draw_i in draw:
                                display.blit(draw_i.image, draw_i.rect)
                        pygame.display.flip()
        self.image = pygame.image.load(self.file_path_global)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        display.blit(self.image, self.rect)
        if len(draw) != 0:
            for draw_i in draw:
                display.blit(draw_i.image, draw_i.rect)
        pygame.display.flip()


class Speech(pygame.sprite.Sprite):
    def __init__(self):
        self.pos_x = 222
        self.pos_y = 222

    def draw(self, text_t, personage, personage_height, personage_width, display):
        # изменяем текст
        counter = 1
        text_finite = []
        for i in text_t.split():
            if counter % 5 == 0 and counter != 1:
                text_finite.append(i + '\n')
            else:
                text_finite.append(i)
            counter += 1

        font = pygame.font.SysFont("comicsansms", 15)
        font_2 = pygame.font.SysFont('arial', 15)
        text = (' '.join(text_finite)).split('\n')
        text_2 = (' '.join(text_finite)).split('\n')
        self.pos_x = personage.pos_x - personage_width
        self.pos_y = personage.pos_y - (len(text_finite) * 5)
        for i, line in enumerate(text_2):
            text_surface = font_2.render(('█' * round((len(line)//4)*3)),  False, (0, 0, 0, 0))  # Создаем поверхность текста
            display.blit(text_surface, (self.pos_x-5, self.pos_y + i * 15))  # Отображаем текст с отступом

        for i, line in enumerate(text):
            text_surface = font.render(line, True, (255, 255, 255, 255))  # Создаем поверхность текста
            display.blit(text_surface, (self.pos_x, self.pos_y + i * 15))  # Отображаем текст с отступом
        pygame.display.flip()

    def click(self, event, number, counter):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return number
        else:
            return counter

