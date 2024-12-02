import pygame
import sys
import random

# Инициализация Pygame
pygame.init()



TIME = 1000
# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Движущийся круг с изменением цвета")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Параметры круга
circle_radius = 30
circle_x = -circle_radius  # Начальная позиция круга за пределами экрана
circle_y = HEIGHT // 2     # Круг движется по центру по вертикали
circle_speed = 5           # Скорость движения круга
circle_color = BLUE        # Начальный цвет круга


pygame.time.set_timer(pygame.USEREVENT, TIME)


# Функция для изменения цвета круга
def change_circle_color():
    """Меняет цвет круга на случайный."""
    global circle_color
    circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Основной игровой цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # Проверка нажатия клавиши A
                change_circle_color()

    # Логика движения круга
    circle_x += circle_speed
    if circle_x - circle_radius > WIDTH:  # Если круг полностью вышел за правую границу
        circle_x = -circle_radius         # Вернуть его на левую сторону

    # Отрисовка
    screen.fill(WHITE)  # Очистить экран
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)  # Рисуем круг
    pygame.display.flip()  # Обновляем экран

    # Ограничиваем FPS
    clock.tick(60)
