import pygame
pygame.init()

class ImageButton:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height)) 
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
        	self.sound = pygame.mixer.Sound(sound_path)
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        font = pygame.font.Font(None, 25)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


def settings(fps, count):
    fps = fps
    count = count
    screen = pygame.display.set_mode((1715, 970))
    pygame.display.set_caption("Настройки")
    main_background = pygame.image.load("background_for_settings.jpg")
    # Создание кнопок
    change_button = ImageButton(1715/2-(252/2), 300, 252, 75, "Изменить fps", "смена.png")
    exit_button = ImageButton(1715/2-(252/2), 400, 252, 75, "Сохранить", "смена.png")
    screen.fill((0, 0, 0))
    screen.blit(main_background, (-200, -400))
    font = pygame.font.Font(None, 36)
    text = font.render(fps, True, (255, 255, 255))
    text_rect = text.get_rect(center=(1715/2, 280))
    screen.blit(text, text_rect)

    running = True
    while running:
        if pygame.mouse.get_focused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                if event.type == pygame.USEREVENT and event.button == change_button:
                    screen.fill((0, 0, 0))
                    screen.blit(main_background, (-200, -400))
                    screen.blit(text, text_rect)
                    count += 1
                    if count % 2 == 0:
                        font = pygame.font.Font(None, 36)
                        text = font.render(fps, True, (255, 255, 255))
                        text_rect = text.get_rect(center=(1715/2, 280))
                        fps = '250'
                    else:
                        font = pygame.font.Font(None, 36)
                        text = font.render(fps, True, (255, 255, 255))
                        text_rect = text.get_rect(center=(1715/2, 280))
                        fps = '360'
                    pygame.display.flip()

                if event.type == pygame.USEREVENT and event.button == exit_button:
                    return False, fps, count

                for btn in [change_button, exit_button]:
                    btn.handle_event(event)

            for btn in [change_button, exit_button]:
                btn.check_hover(pygame.mouse.get_pos())
                btn.draw(screen)

            pygame.display.flip()
