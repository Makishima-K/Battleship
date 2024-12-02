import pygame
import sys
import random


# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 1000, 1000  # Размер экрана
GRID_COLS, GRID_ROWS = 10, 10  # Количество колонок и строк в сетке
CELL_WIDTH = WIDTH // GRID_COLS  # Ширина ячейки
CELL_HEIGHT = HEIGHT // GRID_ROWS  # Высота ячейки
IMAGE_SIZE = 50  # Размер картинки (50x50 пикселей)

k =[]


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0,0)
GREEN = (0,255,0)

# Начальная позиция (в центре сетки)
x_index = GRID_COLS // 2
y_index = GRID_ROWS // 2


image = pygame.image.load("body.png")
image = pygame.transform.scale(image, (IMAGE_SIZE, IMAGE_SIZE))

image2 = pygame.image.load("back.png")
image2 = pygame.transform.scale(image2, (IMAGE_SIZE, IMAGE_SIZE))


image3 = pygame.image.load("candy.png")
image3 = pygame.transform.scale(image3, (IMAGE_SIZE, IMAGE_SIZE))

image4 = pygame.image.load("head.png")
image4 = pygame.transform.scale(image4, (IMAGE_SIZE, IMAGE_SIZE))



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
        



# Основной игровой цикл
clock = pygame.time.Clock()
#print(clock)
#pygame.quit()
#sys.exit()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
way = 14

x = 0
y = 0
time = 900

tail = []
longTail = 0

candy = [15,10]

pygame.time.set_timer(pygame.USEREVENT, time)

ok = 1


FONT_SIZE = 120

font = pygame.font.Font(None, FONT_SIZE)  # None использует шрифт по умолчанию

# Текст
text = "FAIL"  # Текст для отображения

# Рендеринг текста
text_surface = font.render(text, True, RED)  # Создаём поверхность с текстом
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP :
                way = 1
            elif event.key == pygame.K_DOWN :
                way = 2
            elif event.key == pygame.K_LEFT :
                way = 3
            elif event.key == pygame.K_RIGHT :
                way = 4


        if ok == 1:
            if event.type == pygame.USEREVENT:

                if way == 1:
                    y-=1
                    if y<0:
                        y = GRID_COLS-1
                        
                if way == 2:
                    y+=1
                    if y==10:
                        
                    
                        y = 0
                        #screen.blit(image, (mmm[y][x][0], mmm[x][y][1]))
                if way == 3:
                    x-=1
                    if x<0:
                        
                    
                        x = GRID_ROWS-1
            
                if way == 4:
                    x+=1
                    if x==10:
                        x = 0


        


                screen.fill((0,0,0))

                for yy in range(len(mmm)):
                    #pygame.display.update()
                    
                    for xx in range(len(mmm)):
                        screen.blit(image2, (mmm[yy][xx][0], mmm[yy][xx][1]))
                
                #print(x,y)
                #print((mmm[y][x][0], mmm[y][x][1]))

                
                if (mmm[y][x][0], mmm[y][x][1]) in k:

                    print(k,longTail)
                    #time = 99999999
                    ok = 2
                    print('fail')
                    #pygame.quit()
                    #sys.exit() 

                

                if candy[0] == 15:
                    candy[0] = random.randint(0,9)
                    candy[1] = random.randint(0,9)
                    
                screen.blit(image3, (mmm[candy[1]][candy[0]][0], mmm[candy[1]][candy[0]][1]))
                #screen.blit(image, (x_pos, y_pos))

                if (mmm[y][x][0], mmm[y][x][1]) == (mmm[candy[1]][candy[0]][0], mmm[candy[1]][candy[0]][1]):
                    #candy[0] == 15
                    candy[0] = random.randint(0,9)
                    candy[1] = random.randint(0,9)
                    longTail += 1
                    print('+1')
                    while (candy[0], candy[1]) in k:
                        print('SHIT')
                        candy[0] = random.randint(0,9)
                        candy[1] = random.randint(0,9)



                if longTail>0:
                    k =[]
                    for i in range(longTail):
                        k.append((mmm[tail[-i][0]][tail[-i][1]][0], mmm[tail[-i][0]][tail[-i][1]][1]))
                        
                        i =i+1
                        screen.blit(image, (mmm[tail[-i][0]][tail[-i][1]][0], mmm[tail[-i][0]][tail[-i][1]][1]))
                

                tail.append((y,x))
                #print(tail[-1])
                


                screen.blit(image4, (mmm[y][x][0], mmm[y][x][1]))
        if ok == 2:
            screen.fill((0, 0, 0))  # Чёрный фон
            screen.blit(text_surface, text_rect)
            
    
    pygame.display.flip()  # Обновляем экран
    
    clock.tick(60)


    