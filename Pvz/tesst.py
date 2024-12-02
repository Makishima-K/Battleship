
WIDTH, HEIGHT = 1000, 1000  # Размер экрана
GRID_COLS, GRID_ROWS = 10, 10  # Количество колонок и строк в сетке
CELL_WIDTH = WIDTH // GRID_COLS  # Ширина ячейки
CELL_HEIGHT = HEIGHT // GRID_ROWS  # Высота ячейки
IMAGE_SIZE = 50  # Размер картинки (50x50 пикселей)

print(CELL_HEIGHT)

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0,0)
GREEN = (0,255,0)

# Начальная позиция (в центре сетки)
x_index = GRID_COLS // 2
y_index = GRID_ROWS // 2
b = 0
c =0
#d =0
mmm = []
for i in range(GRID_COLS):
    mmm.append([])
    c = 0
    b+=1
    
    for j in range(GRID_ROWS):
        c +=1
        #d+=1
        Xpoint = c * CELL_WIDTH - (CELL_WIDTH // 2) - IMAGE_SIZE // 2

        Ypoint = b * CELL_HEIGHT - (CELL_HEIGHT  // 2) - IMAGE_SIZE // 2

        mmm[i].append([Xpoint,Ypoint])
        

def matix(a):
    for x in range(len(a)):
        #pygame.display.update()
        print()
        for y in range(len(a)):
            print(a[x][y], end=' ')
    print()
#print(mmm)
matix(mmm)
x = 0
y =10
print((mmm[x][y][0], mmm[x][y][1]))