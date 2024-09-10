#0=y 1=x
#import pygame
#pygame.init()
#screen = pygame.display.set_mode((1600,900))

p1 = [['P1','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'],
     ['1 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['2 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['3 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['4 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['5 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['6 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['7 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['8 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['9 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['10', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


p1F = [['F1','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'],
     ['1 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['2 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['3 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['4 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['5 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['6 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['7 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['8 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['9 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['10', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]




p1Place = [['  ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'],
     ['1 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Galeon', 'X X X X'],
     ['2 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,  'Briga', 'X X X'],
     ['3 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 'Shlup', 'X X' ],
     ['4 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Ship1', 'X'],
     ['5 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['6 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['7 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['8 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['9 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['10', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


p2 = [['P2','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'],
     ['1 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['2 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['3 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['4 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['5 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['6 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['7 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['8 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['9 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['10', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

p2F = [['F2','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K'],
     ['1 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['2 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['3 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['4 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['5 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['6 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['7 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['8 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['9 ', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     ['10', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

mis = 1
pounch = 2
ship = 3

allshipscore1 = [0,0,0,0]
allshipscore2 = [0,0,0,0]

allship1= { 'ship411' : [[0,0,0], [0,0,0], [0,0,0], [0,0,0]],
            
            'ship311' : [[0,0,0], [0,0,0], [0,0,0]],
            'ship312' : [[0,0,0], [0,0,0], [0,0,0]],

            'ship211' : [[0,0,0], [0,0,0]],
            'ship212' : [[0,0,0], [0,0,0]],
            'ship213' : [[0,0,0], [0,0,0]],

            'ship111' : [[0,0,0]],
            'ship112' : [[0,0,0]],
            'ship113' : [[0,0,0]],
            'ship114' : [[0,0,0]]
           }

allship2= { 'ship421' : [[0,0,0], [0,0,0], [0,0,0], [0,0,0]],
            
            'ship321' : [[0,0,0], [0,0,0], [0,0,0]],
            'ship322' : [[0,0,0], [0,0,0], [0,0,0]],

            'ship221' : [[0,0,0], [0,0,0]],
            'ship222' : [[0,0,0], [0,0,0]],
            'ship223' : [[0,0,0], [0,0,0]],

            'ship121' : [[0,0,0]],
            'ship122' : [[0,0,0]],
            'ship123' : [[0,0,0]],
            'ship124' : [[0,0,0]]
           }

#print(allship1['ship411'][0][0])
numship = 0


def breakship(s,c,n,c2):
    
    print(n, 'd')
    g = 0


    #for ship_name, coordinates in s.items():
        # Проходим по всем точкам координат корабля
    #    for index, point in enumerate(coordinates):
            # Проверяем только первую и вторую координату
     #       if point[2] == 1:
     #           g = g + 1
                #print(index, ship_name)
                #return ship_name, index 

    for i in range(len(s[n])):
        print(i)
        if i < len(s[n]):
            print('2')
            print(s[n][i],'trttr')
            if s[n][i][2]== 1:
                g = g+1
        
        #print(s)
    print(s[n])
    print(len(s[n]))
    print(g)
    if g == len(s[n]):
        print('asdasdsadqwqdadasdawq')
        destroy(s,n,c,1)
        
def search(allship2,x,y):
    #global numship
    #d = 0
    #ll ={'ship':[]}
   # for i in AS:
   #    

   #     for j in AS[i]:
                #print(AS[i],'s')
                #print(a,b,'s')
                #print(j,'s')
                #print(j[0],'s')
               ## print(j[1],'s')
                #print(numship,'ss')
    #            if (j[0] == a) and (j[1] == b):
    #                return i
    #            numship+=1

    #    numship = 0
                #ll['ship'].append(1)
                #print("f")
                #d = d+1
    
    # Проходим по всем кораблям в словаре
    for ship_name, coordinates in allship2.items():
        # Проходим по всем точкам координат корабля
        for index, point in enumerate(coordinates):
            # Проверяем только первую и вторую координату
            if point[0] == x and point[1] == y:
                print(index, ship_name)
                return ship_name, index  # Возвращаем название корабля, если нашли совпадение
    #return None 

    #if len(ll['ship']) == len(AS):
        #return ll
            
#hhhh = search(allship1,0,0)     
#print(hhhh)
#print(numship)
#search(allship1,1,2)   
   
#search(allship1)

def shipscorerule(AS):
    if AS[0] > 1:
        AS[0]= 1
        return False
    if AS[1] > 2:
        AS[1]= 2
        return False
    if AS[2] > 3:
        AS[2]= 3
        return False
    if AS[3] > 4:
        AS[3]= 4
        return False
    return True


def shiprule(a,b,c,r):
    k=0
#    if r == 1:
#        if (c[a+1][b+1] == 1) or (c[a][b+1] == 1) or(c[a+1][b] == 1) or(c[a-1][b-1] == 1)or(c[a][b-1] == 1)or(c[a-1][b] == 1)or(c[a+1][b-1] == 1)or(c[a-1][b+1] == 1):
#            print('NO')
#            k = 1
    if k == 0:
        #print('yes')
        if a+1<11 and b+1<11:
            #print(a+1)
            if c[a+1][b+1] == 0:
                c[a+1][b+1] = 1

        if (a+1<11) and (b<11):
            if c[a+1][b] == 0:
                c[a+1][b] = 1

        if a<11 and b+1<11:
            if c[a][b+1] == 0:
                c[a][b+1] = 1
            

        if a-1>0 and b-1>0:
            if c[a-1][b-1] == 0:
                c[a-1][b-1] = 1
            

        if a-1>0 and b>0:
            if c[a-1][b] == 0:
                c[a-1][b] = 1
        

        if a>0 and b-1>0:
            if c[a][b-1] == 0:
                c[a][b-1] = 1
            

        if a-1>0 and b+1<11:
            if c[a-1][b+1] == 0:
                c[a-1][b+1] = 1
            

        if a+1<11 and  b-1>0 :
            if c[a+1][b-1] == 0:
                c[a+1][b-1] = 1
        

def shipplaceY(s,c,a,b):
    stop = 0
    y = a
    x = b
   
    
    for i in range(len(s)):
        if (y+i > 11) or (y+i<1) or (x > 11 or x+i<1):
            #print('stop')
            #stop = 1
            return 1
    for i in range(len(s)):
        if c[y+i][x] == 1:
            #return 1
            return 1
        
    for i in range(len(s)):
        if c[y+i][x] == 3:
            #return 1
            return 1
    if stop == 0:
        for i in range(len(s)):
            
            k = y+i
            if y+i > 0 and k<11:
                
                c[k][x] = 3
                s[i][1] = k
                s[i][0] = x
            

def shipplace(s,c):
    for i in s:
        for y in s[i]:
            if y[0] == 0:
                continue
            c[y[0]][y[1]] = 3

shipplace(allship1,p1)

def shipplaceX(s,c,y,x):
    for i in range(len(s)):
        if (y+i > 11) or (y+i<1) or (x > 11 or x+i<1):
            #print('stop')
            #stop = 1
            return 1
    for i in range(len(s)):
        if c[y+i][x] == 1:
            #return 1
            return 1
        
    for i in range(len(s)):
        if c[y+i][x] == 3:
            #return 1
            return 1
    #x=b
    #y=a
    stop = 0
    for i in range(len(s)):
        if (y > 11) or (y<1) or (x+i > 11 or x+i<1):
            print('stop')
            stop = 1
            break
    for i in range(len(s)):
        if c[y][x+i] == 1:
            print('stop')
            stop = 1
            break
    
            

    if stop == 0:
        for i in range(len(s)):
                #o = s[0][1]
                #y= s[0][0]
                k = x+i    
                if k > 0 and k<11:
                
                        c[y][k] = 3
                        s[i][1] = y
                        s[i][0] = k

                else:
                        print('F')
            

def matix(a):
    for x in range(len(a)):
        #pygame.display.update()
        print()
        for y in range(len(a)):
            print(a[x][y], end=' ')
    print()

def clearP(a):
    for x in range(len(a)):
        
        for y in range(len(a)):
            if ((y < 11) and (y>1)) and (x < 11 and x>1):
                a[x][y] = 0
                #print(x,y)
    


def shoot(x,y,c,AS,c1):
    
    print(c)
    print(c[x][y])
    if c[x][y] == 3:
        print('ff')
        c1[x][y] = 2
        a, numship = search(AS,y,x)
        print(a)
        print(AS)
        print(numship,'AAAA')
        #print(AS[a][numship],'ooo')
        AS[a][numship][2]=1
        #print(AS[a][numship])
        return 1
        print ('pounch')
    if (c[x][y] == 0 )or(c[x][y] == 1):
        print(c[x][y])
        c1[x][y] = 1
        return 0
        print('miss')
        



#shipplaceX(allship1['ship411'],p1,9,3)
#shipplaceY(ship411,p1)
#shipplaceX(ship421,p1)

#matix(p1)
#clearP(p1)
#matix(p1)
#matix(ship411)
#print(ship411)

def destroy(AA,s,c,r):
    for i in range(len(AA[s])):
        shiprule(AA[s][i][1],AA[s][i][0],c,r)


def tranclater(g,AR, a ):
    g[4]=5


    if AR[0] == 0:
        if g[0] == 'Galeon':
                g[0] = 'ship4'+ a +'1'
                g[4] = 0
                AR[0] +=1


    if AR[1] == 0:
        if g[0] == 'Briga':
            g[0] = 'ship3'+ a +'1'
            g[4] = 1
            AR[1] +=1


    if AR[1] == 1:
        if g[0] == 'Briga':
            g[0] = 'ship3'+ a +'2'
            g[4] = 1
            AR[1] +=1

    if AR[2] == 0:
        if g[0] == 'Shlup':
            g[0] = 'ship2'+ a +'1'
            g[4] = 2
            AR[2] +=1
    if AR[2] == 1:
        if g[0] == 'Shlup':
            g[0] = 'ship2'+ a +'2'
            g[4] = 2
            AR[2] +=1
    if AR[2] == 2:
        if g[0] == 'Shlup':
            g[0] = 'ship2'+ a +'3'
            g[4] = 2
            AR[2] +=1

    if AR[3] == 0:
        if g[0] == 'Boat':
            g[0] = 'ship1'+ a +'1'
            g[4] = 3
            AR[3] +=1
    if AR[3] == 1:
        if g[0] == 'Boat':
            g[0] = 'ship1'+ a +'2'
            g[4] = 3
            AR[3] +=1
    if AR[3] == 2:
        if g[0] == 'Boat':
            g[0] = 'ship1'+ a +'3'
            g[4] = 3
            AR[3] +=1
    if AR[3] == 3:
        if g[0] == 'Boat':
            g[0] = 'ship1'+ a +'4'
            g[4] = 3
            AR[3] +=1
    

    #print(g[2])
    if g[2] == 'A':
        g[2]=1
    if g[2] == 'B':
        #print('F')
        g[2]=2
    if g[2] == 'C':
        g[2]=3
    if g[2] == 'D':
        g[2]=4
    if g[2] == 'E':
        g[2]=5
    if g[2] == 'F':
        g[2]=6
    if g[2] == 'G':
        g[2]=7
    if g[2] == 'H':
        g[2]=8
    if g[2] == 'J':
        g[2]=9
    if g[2] == 'K':
        g[2]=10
    #print(g)
    g[3]=int(g[3])
    return g


def tranclaterFight(a):
    b = 0
    if a[0] == 'A':
        b=1
    if a[0] == 'B':
        #print('F')
        b=2
    if a[0] == 'C':
        b=3
    if a[0] == 'D':
        b=4
    if a[0] == 'E':
        b=5
    if a[0] == 'F':
        b=6
    if a[0] == 'G':
        b=7
    if a[0] == 'H':
        b=8
    if a[0] == 'J':
        b=9
    if a[0] == 'K':
        b=10
    
    return b


#print(allship1)
#matix(p1Place)
play = 1
shipplaceP1 =1
o = 1
shipplaceP2 = 1
fight = 1
pp1 = 1
pp2 = 1
hit1 = 0
hit2 = 0 














while play:

    while shipplaceP1 :
        o = 1
        if (allshipscore1[0] == 1)and(allshipscore1[1] == 2)and(allshipscore1[2] == 3)and(allshipscore1[3] == 4):
            print('Yes')
            o = 2
            shipplaceP1 = False


        matix(p1)
        if o == 1:
            g =[]
            k = input('place ship  ')

            if k == 'stop':
                play = 0
                shipplaceP1 =0
                shipplaceP2 =0
                continue
            if k == 'p1':
                    shipplaceP2 =0
                    shipplaceP1 =0
                    continue
            g =k.split(' ')
            g.append(0)
            print(g)
            g = tranclater(g,allshipscore1,'1')
            if g[4]== 5 :
                print('No')
                continue
            #print(g)
            if g[1] == 'Y':
                aAAAA = True
                #r12 = shipscorerule(allshipscore)
                print(g)
                if aAAAA == True:
                    a12 = shipplaceY(allship1[g[0]],p1,int(g[3]),int(g[2]))
                    if a12 == 1:
                        print('NO')


                        allshipscore1[g[4]] -=1

                        continue
                    destroy(allship1,g[0],p1,1)
                if aAAAA == False:
                    print('No')

            if g[1] == 'X':
                aAAAA = True
                aAAAA = shipscorerule(allshipscore1)
                print(g)
                if aAAAA == True:
                    a12 = shipplaceX(allship1[g[0]],p1,int(g[3]),int(g[2]))
                    if a12 == 1:
                        print('NO')


                        allshipscore1[g[4]] -=1

                        continue
                    destroy(allship1,g[0],p1,1)


                if aAAAA == False:
                    print('More')
            print(allship1)
    o = 1
#    allshipscore1[0] == 0
#    allshipscore1[1] == 0
#    allshipscore1[2] == 0
#    allshipscore1[3] == 0

    while shipplaceP2 :
            if (allshipscore2[0] == 1)and(allshipscore2[1] == 2)and(allshipscore2[2] == 3)and(allshipscore2[3] == 4):
                print('Yes')
                o = 2
                shipplaceP2 = False


            matix(p2)
            if o == 1:
                g =[]
                k = input('place ship  ')

                if k == 'stop':
                    play = 0
                    shipplaceP1 =0
                    shipplaceP2 =0
                    continue
                if k == 'p1':
                    
                    shipplaceP1 =0
                    shipplaceP2 =0
                    continue

                g =k.split(' ')
                g.append(0)
                print(g)
                g = tranclater(g,allshipscore2,'2')
                print(g)
                if g[4]== 5 :
                    print('No')
                    continue
                #print(g)
                if g[1] == 'Y':
                    aAAAA = True
                    
                    #r12 = shipscorerule(allshipscore)
                    
                    if aAAAA == True:
                        a12 = shipplaceY(allship2[g[0]],p2,int(g[3]),int(g[2]))
                        if a12 == 1:
                            print('NO')


                            allshipscore2[g[4]] -=1

                            continue
                        destroy(allship2,g[0],p2,1)
                    if aAAAA == False:
                        print('No')
                if g[1] == 'X':
                    aAAAA = True
                    aAAAA = shipscorerule(allshipscore2)

                    if aAAAA == True:
                        shipplaceX(allship2[g[0]],p2,int(g[3]),int(g[2]))
                        destroy(allship2,g[0],p2,1)
                    if aAAAA == False:
                        print('More')
    
    
    while fight:
        

        while pp1:
            pp1 = False
            name = 0
            matix(p1F)
            g1 = 0
            x = 0
            y = 0
            g1 = input()
            
            
            y = int(g1[1])
            if len(g1) == 3 :
                y = int(g1[1:3])
            x = tranclaterFight(g1)
            print(x,y)
            #name1 = name[1]
            #print(name,'A')
            #print(name,'23')
            aaa = shoot(y,x,p1,allship1,p1F)
            print(x,y)
            if aaa == 1:
                pp1 = True
                name, i = search(allship1,x,y)
                print('shoot')
                print(name,'A')
                breakship(allship1,p1F,name,p1)
                hit1 = hit1 + 1
            if aaa == 0:
                print('miss')
            #print(allship1)
            #print(hit1, 'hit')
            matix(p1F)
            if hit1 == 20:
                print('Player 1 Win ')
                pp1 = False
                pp2 = False
                fight = False
            
            
#            if hit1 == 20:
#                print('Player 1 Win ')
#                pp1 = False
#                pp2 = False
 #               fight = False
    
    
            

        while pp2:
            pp1 = False
            name = 0
            matix(p2F)
            g1 = 0
            x = 0
            y = 0
            g1 = input()
            
            
            y = int(g1[1])
            if len(g1) == 3 :
                y = int(g1[1:3])
            x = tranclaterFight(g1)
            #print(x,y)
            #name1 = name[1]
            #print(name,'A')
            #print(name,'23')
            aaa = shoot(y,x,p2,allship2,p2F)
            #print(x,y)
            if aaa == 1:
                pp1 = True
                name, i = search(allship2,x,y)
                #print('shoot')
                #print(name,'A')
                breakship(allship2,p2F,name,p2)
                hit2 = hit2 + 1
            if aaa == 0:
                print('miss')
            #print(allship1)
            #print(hit1, 'hit')
            if hit2 == 20:
                print('Player 1 Win ')
                pp1 = False
                pp2 = False
                fight = False

        if fight == True:
            pp1 = True
            pp2 = True
            print(3)

            

    
        


        
        #print(g)

        
    



# Galeon Y A 1
# Briga Y C 1
# Briga Y E 1
# Shlup Y G 1
# Shlup Y J 1
# Shlup Y A 6
# Boat X A 9
# Boat X C 9
# Boat X E 9
# Boat X G 9


# #breakship(ship411)

#destroy(ship411,p1)
#destroy(ship421,p1)
#matix(p1)

#shoot(9,3,p1)
#matix(p1)
# Galeon X A 1
# Briga X C 1
# Shlup X A 1
# Boat X A 1



