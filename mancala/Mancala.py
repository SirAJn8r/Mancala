board = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
p1 = 0
p2 = 0
p1turn = True
playing = True
theinput = 0

"""printboard() -> None -- prints the board"""
def printboard():
    print("P1    1 2 3 4 5 6")
    print("   -----------------")
    print("     |{}|{}|{}|{}|{}|{}|".format(board[0][0],board[0][1],board[0][2],board[0][3],board[0][4],board[0][5]))
    print("{}    -------------    {}".format(p1,p2))
    print("     |{}|{}|{}|{}|{}|{}|".format(board[1][5],board[1][4],board[1][3],board[1][2],board[1][1],board[1][0]))
    print("   -----------------")
    print("      6 5 4 3 2 1    P2")

"""Main() -> None -- runs all function"""
def Main():
    init()
    
    while(playing):
        printboard()
        getinput()
        update()
        checkWin()
        switch()
    
"""init() -> None -- sets up the code for usage"""
def init():
    global theinput, p1, p2, p1turn, board, playing
    p1turn = True
    p1 = 0
    p2 = 0
    for i in range(6):
        board[0][i] = 4
        board[1][i] = 4
    playing = True
    
"""getinput() -> None -- Asks for the input of the user and turns it into a number; 1-6"""
def getinput():
    global theinput, p1, p2, p1turn, board, playing
    temp = True
    inp = ""
    while(temp):
        if p1turn == True:
            inp = input("Player 1, input: ")
        else:
            inp = input("Player 2, input: ")
        try:
            num = int(inp)
            if(num < 1 or num > 6):
                raise(OverflowError)
            theinput = num-1
            temp = False
        except TypeError:
            print("Not a number")
        except OverflowError:
            print("Not between 1 and 6")
            
"""update() -> None -- Moves the stones forward"""
def update():
    global theinput, p1, p2, p1turn, board, playing
    tnum = 0
    theinput -= 1
    if(p1turn == False):
        tnum = 1
    tempnum = board[tnum][theinput]
    board[tnum][theinput+1] = 0
    for i in range(tempnum):
        if(theinput < 0):
            if(tnum == 0):
                tnum = 1
                p1 += 1
                if(tempnum == 0):
                    p1turn = False
            else:
                tnum = 0
                p2 += 1
                if(tempnum == 0):
                    p1turn = True
            theinput = 5
        else:
            theinput -= 1
            board[tnum][theinput+1] += 1
        
            
            
        
        
        
    
"""checkWin() -> None -- Self Evident. Checks if someone has one and treats appropiatly"""
def checkWin():
    global theinput, p1, p2, p1turn, board, playing
    temp = 0
    for i in range(6):
        if(board[0][i] == 0 and board[1][i] == 0):
            temp += 1
    if(temp == 6):
        playing = False
        print("Player 1: {}\nPlayer 2:{}".format(p1,p2))
        if(p1 > p2):
            print("Player 1 Won!")
        elif(p1 < p2):
            print("Player 2 Won!")
        else:
            print("It's a Tie!")
       
"""switch() -> None -- Switches to the other player's turn"""
def switch():
    global theinput, p1, p2, p1turn, board, playing
    if(p1turn):
        p1turn = False
    else:
        p1turn = True
        
  
Main()