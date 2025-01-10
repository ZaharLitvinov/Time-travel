import pygame
# кнопки
class sprite_button(pygame.sprite.Sprite):
    def __init__(self, file_path, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))

