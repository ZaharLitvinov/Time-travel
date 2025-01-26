import pygame

# Инициализация Pygame
pygame.init()

# Установка шрифта
font = pygame.font.Font(None, 36)

# Создание текста с переносом
text_lines = ["Это первая строка.", "Это вторая строка.", "Это третья строка."]
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Заполняем фон белым цветом

    # Отображаем каждую строку текста
    for i, line in enumerate(text_lines):
        text_surface = font.render(line, True, (0, 0, 0))  # Создаем поверхность текста
        screen.blit(text_surface, (50, 50 + i * 40))  # Отображаем текст с отступом

    pygame.display.flip()  # Обновляем экран

pygame.quit()