import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Определение цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Начальные параметры объекта
rect_x, rect_y = 400, 300
rect_width, rect_height = 50, 50
rect_speed_x, rect_speed_y = 5, 5

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновление позиции объекта
    rect_x += rect_speed_x
    rect_y += rect_speed_y

    # Проверка на соприкосновение с границами окна
    if rect_x < 0 or rect_x + rect_width > width:
        rect_speed_x = -rect_speed_x  # Отразить по X

    if rect_y < 0 or rect_y + rect_height > height:
        rect_speed_y = -rect_speed_y  # Отразить по Y

    # Очистка экрана
    screen.fill(BLACK)

    # Рисуем объект
    pygame.draw.rect(screen, WHITE, (rect_x, rect_y, rect_width, rect_height))

    # Обновление дисплея
    pygame.display.flip()

    # Ограничение кадровой скорости
    pygame.time.Clock().tick(60)

pygame.quit()
