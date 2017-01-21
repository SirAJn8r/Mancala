board = []
board2 = []
for i in range(10):
    board.append([])
    board2.append([])
    for j in range(10):
        board[i].append("*")
        board[i].append("*")

def printboard():
    for i in range(len(board)):
        line = ""
        for j in range(len(board[i])):
            line += board[i][j] + " "
        print(line)
        
printboard()