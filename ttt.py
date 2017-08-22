import numpy
import sys

def draw_row(size):
    print(' ---' * size)
    
def draw_box(size, a):    
    for i in range(len(a)):
        if a[i] == 0:
            p = '|   '
        elif a[i] == 1:
            p = '| X '
        elif a[i] == 2:
            p = '| O '
        else:
            p = '| ' + str(a[i]) + ' '
        print(p, end = "")
    print('|')

def find_win_row(a):    
    for j in range(len(a)):
        set_g = set(a[j])
        if (len(set_g) == 1 and a[j] != 0):
            return a[j][0]
    return 0

def find_win_col(a):
    numpy.transpose(a)
    for j in range(len(a)):
        set_g = set(a[j])
        if (len(set_g) == 1 and a[j] != 0):
            return a[j][0]
    return 0

def find_win_dia(a):
    if a[1][1] != 0:
        if a[1][1] == a[0][0] == a[2][2]: 
            return a[1][1]
        elif a[1][1] == a[0][2] == a[2][0]:
            return a[1][1]			
    return 0

def find_win(a):
    i = find_win_row(a)
    i = max(find_win_col(a), i)
    i = max(find_win_dia(a), i)
    if i != 0:
        return i
    if any(0 in sublist for sublist in a):
        return 0
    else:
        return 3
    
while True:            
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    #size = input('Size of board?')
    #size = int(size)
    size = 3
    p1 = 0
    p2 = 0
    end = False
    for i in range(len(game)):
        draw_row(size)
        draw_box(size, game[i])
    draw_row(size)

    while not end:
        flag = True
        while flag:
            try:
                p1_move = input("P1 Move (row,column)")
                x,y = p1_move.split(",")
                x = int(x) - 1
                y = int(y) - 1
                if (game[x][y] != 0 or x < 0 or y < 0 or x > size or y > size):
                    print("Invalid Input")
                else:
                    flag = False
            except:
                print("Invalid Input")
                
        game[x][y] = 1
        
        for i in range(len(game)):
            draw_row(size)
            draw_box(size, game[i])
        draw_row(size)

        w = find_win(game)
        if w != 0:
            if w == 3:
                print("Tie")
                end = True
            else:
                print("Player ", w, " win!")
                end = True
                p1 += 1

        if end:
            break
        
        flag = True
        while flag:
            p2_move = input("P2 Move (row,column)")
            try:
                x,y = p2_move.split(",")
                x = int(x) - 1
                y = int(y) - 1
                if (game[x][y] != 0 or x < 0 or y < 0 or x > size or y > size):
                    print("Invalid Input")
                else:
                    flag = False  
            except:
                print("Invalid Input")
                      
        game[x][y] = 2
        
        for i in range(len(game)):
            draw_row(size)
            draw_box(size, game[i])
        draw_row(size)

        w = find_win(game)
        if w != 0:
            if w == 3:
                print("Tie")
                end = True            
            else:
                print("Player ", w, " win!")
                end = True
                p2 += 1

    print(p1, " - Player 1 | ", p2, " - Player 2")
    again = input("Play again? y/n")
    if again != "y":
        sys.exit()      
