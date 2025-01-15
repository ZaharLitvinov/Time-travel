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
    def __init__(self, file_path, pos_x, pos_y, height, width, up='w', right='d', left='a'):
        pygame.sprite.Sprite.__init__(self)

        # позиция размеры и картинка

        self.file_path_global = file_path
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width

        # Кнопки

        self.up = up
        self.right = right
        self.left = left

        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

    # если нажата кнопка

    def movements(self, click_name_button):
        if not '+' in click_name_button:
            if click_name_button == self.rect:
                self.pos_x += 5
            if click_name_button == self.left:
                self.pos_x += 5
            if click_name_button == self.up:
                pass

        else:
            click_name_button = str(click_name_button).split('+')
            if click_name_button[1] == self.rect:
                pass

        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

