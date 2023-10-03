#constant
COL_COUNT = 7
ROW_COUNT = 6

def createBoard():
    board=[]
    row=[]
    for r in range(ROW_COUNT): # r= 0,1,... ROW_COUNT-1
        row.clear()
        for c in range(COL_COUNT): # c= 0,1,.... COL_COUNT-1
            row.append(0)
        board.append(row.copy())
    return board


def showBoard(board):
    print('\n'*40)
    print(''.center(COL_COUNT*2-1,chr(95)))
    for r in range(ROW_COUNT):
        print(*board[r])
    print(''.center(COL_COUNT*2-1,chr(175)))


def get_next_open_row(board,col):
    for r in range( ROW_COUNT-1,-1,-1): # r= 5,4,3,2,1,0
        if board[r][col] == 0:
            return r

def createColString():
    s = ''
    for c in range(COL_COUNT): # c=0,1,2,3,4,5,6
        s = s + str(c) +' '
    return s

def get_player_input(playerNum):
    valid = False
    while not valid:
        col = input( createColString()+' Player #{} Choose a column -> '.format(playerNum) )
        #valid = col.isnumeric() and  int(col)>=0 and int(col) < COL_COUNT
        valid = col.isnumeric() and  0 <= int(col) < COL_COUNT
    return int(col)


def is_column_filled(board,col):
    return board[0][col] != 0

def is_winning_move(b,p):
    
# check horizontal wins

    for c in range(COL_COUNT-3): #c=0,1,2...COL_COUNT-3
        for r in range(ROW_COUNT):
            #print('b[{}][{}]'.format(r,c))
            if b[r][c] == b[r][c+1] == b[r][c+2] == b[r][c+3] == p :
                return True

# check verticle
    for c in range(COL_COUNT): #c=0,1,2...COL_COUNT-3
        for r in range(ROW_COUNT-3): # r=0,1,2
            #print('b[{}][{}]'.format(r,c))
            if b[r][c] == b[r+1][c] == b[r+2][c] == b[r+3][c] == p :
                return True

# check diaginal up
    for c in range(COL_COUNT-2): #c=0,1,2...COL_COUNT-3
        for r in range(3, ROW_COUNT): # r=3,4,5
            #print('b[{}][{}]'.format(r,c))
            if b[r][c] == b[r-1][c-1] == b[r-2][c-2] == b[r-3][c-3] == p :
                return True   

# check diaginal down
    for c in range(COL_COUNT-3): #c=0,1,2...COL_COUNT-3
        for r in range(ROW_COUNT-3): # r=0,1...2 ROW-COUNT
            #print('b[{}][{}]'.format(r,c))
            if b[r][c] == b[r+1][c+1] == b[r+2][c+2] == b[r+3][c+3] == p :
                return True             

b = createBoard()
showBoard(b)
player = 1 
game_over = False


while not game_over:
    col = get_player_input(player)
    if is_column_filled(b,col):
        print("sorry that column is filled")
    else:    
        row = get_next_open_row(b,col)
        b[row][col] = player   
        showBoard(b)
        if is_winning_move(b,player):
            game_over = True
            print('Player {} you are the winner!'.format(player))
        player += 1
        if player == 3:
            player = 1
            
