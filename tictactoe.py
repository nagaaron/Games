#tictactoe
import pygame


        
def in_rect(point,field):
    def area (x1,y1,x2,y2,x3,y3):
        return abs((x1 * (y2 - y3) + 
                x2 * (y3 - y1) + 
                x3 * (y1 - y2)) / 2.0) 
    
    a1 = area(field[0][0],field[0][1],field[1][0],field[1][1],field[2][0],field[2][1])
    a2 = area(field[1][0],field[1][1],field[2][0],field[2][1],field[3][0],field[3][1])
    a = a1+a2
    
    abp = area(point[0],point[1],field[0][0],field[0][1],field[1][0],field[1][1])
    bcp = area(point[0],point[1],field[1][0],field[1][1],field[2][0],field[2][1])
    cdp = area(point[0],point[1],field[2][0],field[2][1],field[3][0],field[3][1])
    dap = area(point[0],point[1],field[0][0],field[0][1],field[3][0],field[3][1])
    
    return a ==(abp+bcp+cdp+dap)


def draw_field(window):
    pygame.draw.rect(window,(255,255,255),(100,150,300,300))
    pygame.draw.rect(window,(255,0,0),(100,150,300,300),2)
    for i in range(200,400,100):
        pygame.draw.line(window,(255,0,0),(i,150),(i,450),2)
    for j in range(250,400,100):
        pygame.draw.line(window,(255,0,0),(100,j),(400,j),2)
    
def draw_board(window,p,players,score):
    #colorcheck
    if p ==0:
        c0 = (0,255,0)
        c1 = (128,128,128)
    else:
        c0 = (128,128,128)
        c1  = (0,255,0)
            
    #player 1  
    pygame.font.init()
    font = pygame.font.SysFont('comicsans',50)
    text_width,text_height = font.size(players[0])
    label = font.render(players[0],1, (255,255,255))
    window.blit(label,(50,35))
    pygame.draw.rect(window,c0,(50,35,text_width,text_height),4)
    
    #player 2
    pygame.font.init()
    font = pygame.font.SysFont('comicsans',50)
    text_width,text_height = font.size(players[1])
    label = font.render(players[1],1, (255,255,255))
    window.blit(label,(500-50-text_width,35))
    pygame.draw.rect(window,c1,(500-50-text_width,35,text_width,text_height),4)
    
    #score
    stringtoput = str(score[0]) + '  :  ' + str(score[1])
    font = pygame.font.SysFont('comicsans',50)
    text_width,text_height = font.size(stringtoput)
    label = font.render(stringtoput,1, (240,240,240))
    window.blit(label,(250-int(text_width/2),85))
def draw_positions(window,fields,taken):
    for k,field in enumerate(fields):
        if taken[k]== 1:
            pygame.draw.line(window,(0,0,0),(field[3][0]+10,field[3][1]+10),(field[3][0]+90,field[3][1]+90),5)
            pygame.draw.line(window,(0,0,0),(field[3][0]+10,field[3][1]+90),(field[3][0]+90,field[3][1]+10),5)
        elif taken[k] == 0:
            pygame.draw.circle(window,(0,0,0),(field[3][0]+50,field[3][1]+50),40,5)
            
            
def win_check(taken,p1op2):
    i = p1op2
    if taken[0] == i and taken[1]==i and taken[2]==i:
        return True
    if taken[3] == i and taken[4]==i and taken[5]==i:
        return True
    if taken[6] == i and taken[7]==i and taken[8]==i:
        return True
    if taken[0] == i and taken[3]==i and taken[6]==i:
        return True
    if taken[1] == i and taken[4]==i and taken[7]==i:
        return True
    if taken[2] == i and taken[5]==i and taken[8]==i:
        return True
    if taken[0] == i and taken[4]==i and taken[8]==i:
        return True
    if taken[2] == i and taken[4]==i and taken[6]==i:
        return True
    return False

def board_full(taken):
    for i in range(len(taken)):
        if taken[i] == None:
            return False
    return True


    
def main():
    fields = [[(200,150),(200,250),(100,250),(100,150)],
         [(300,150),(300,250),(200,250),(200,150)],
         [(400,150),(400,250),(300,250),(300,150)],
         [(200,250),(200,350),(100,350),(100,250)],
         [(300,250),(300,350),(200,350),(200,250)],
         [(400,250),(400,350),(300,350),(300,250)],
         [(200,350),(200,450),(100,450),(100,350)],
         [(300,350),(300,450),(200,450),(200,350)],
         [(400,350),(400,450),(300,450),(300,350)],
         ]
    screen = 500
    p1op2 = 0
    score = [0,0]
    players = ['Player 1','Player 2']
    taken = [None]*9
    new = 0
    window = pygame.display.set_mode((screen,screen))
    pygame.display.set_caption('Tic Tac Toe')
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                gridpos = pygame.mouse.get_pos()

                new = 1
        if new == 1:    
            for k,field in enumerate(fields):
                if in_rect(gridpos,field)==True and taken[k] is None:
                    taken[k] = p1op2
                    new = 0
                    if p1op2 == 0:
                        p1op2 =1
                    else:
                        p1op2 =0

        draw_field(window)
        draw_board(window,p1op2,players,score)
        draw_positions(window,fields,taken)
        pygame.display.update()
        if win_check(taken,p1op2) == True:
            if p1op2 == 0:
                print('Player1 wins!')
            elif p1op2 ==1:
                print('Player2 wins !')
            taken = [None]*9
        if board_full(taken) == True:
            taken = [None]*9
        
    
    pass

if __name__ == '__main__':
    main()