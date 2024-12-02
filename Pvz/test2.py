import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 1200, 900  # Размер экрана
GRID_COLS, GRID_ROWS = 9, 5  # Количество колонок и строк в сетке
CELL_WIDTH = WIDTH // GRID_COLS  # Ширина ячейки
CELL_HEIGHT = HEIGHT // GRID_ROWS  # Высота ячейки
IMAGE_SIZE = 50  # Размер картинки (50x50 пикселей)

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0,0)
GREEN = (0,255,0)

d = 0 
g = 1

circle_radius = 30
circle_x = -circle_radius  # Начальная позиция круга за пределами экрана
circle_y = HEIGHT // 2     # Круг движется по центру по вертикали
circle_speed = 5           # Скорость движения круга
circle_color = BLUE        # Начальный цвет круга


# Инициализация экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Перемещение картинки по сетке")

# Загрузка картинки
image = pygame.image.load("test.png")
image = pygame.transform.scale(image, (IMAGE_SIZE, IMAGE_SIZE))

# Начальная позиция (в центре сетки)
x_index = GRID_COLS // 2
y_index = GRID_ROWS // 2

# Основной игровой цикл
clock = pygame.time.Clock()
print(clock)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and y_index > 0:
                y_index -= 1
            elif event.key == pygame.K_DOWN and y_index < GRID_ROWS - 1:
                y_index += 1
            elif event.key == pygame.K_LEFT and x_index > 0:
                x_index -= 1
            elif event.key == pygame.K_RIGHT and x_index < GRID_COLS - 1:
                x_index += 1

    circle_x += circle_speed

     

    # Рассчитываем центр текущей ячейки
    x_pos = x_index * CELL_WIDTH + CELL_WIDTH // 2 - IMAGE_SIZE // 2
    y_pos = y_index * CELL_HEIGHT + CELL_HEIGHT // 2 - IMAGE_SIZE // 2


    #print(circle_x)
    
    if (((circle_x  > x_pos-10) and (circle_x<x_pos+10)) and 425 == y_pos):

        if g == 1:

            if d == 0:
                circle_color = RED
            if d == 1:
                circle_color = GREEN
            if d == 2:
                circle_color = BLUE
            d+=1
            g =5
            if d > 2:
                d = 0
    
    #print(y_pos,'XXX')
    #print(circle_y)

    if circle_x> x_pos+10:
        g = 1

    if circle_x - circle_radius > WIDTH:  # Если круг полностью вышел за правую границу
        circle_x = 0  
    
    # Отрисовка фона и картинки
    screen.fill(WHITE)  # Заполняем фон черным цветом
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)  # Рисуем круг
   
    screen.blit(image, (x_pos, y_pos))  # Рисуем картинку в нужной ячейке
    pygame.display.flip()  # Обновляем экран

    clock.tick(60)  # Ограничиваем FPS
