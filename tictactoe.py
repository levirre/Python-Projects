board = {
    'HIGH_L':'','HIGH_M':'','HIGH_R':'',
    'MID_L':'','MID_M':'','MID_R':'',
    'LOW_L':'','LOW_M':'','LOW_R':''
}
def printBoard(board) : 
    print(board['HIGH_L'] + '| ' + board['HIGH_M'] + '| ' + board['HIGH_R'])
    print('-+-+-')

    print(board['MID_L'] + ' |' + board['MID_M'] + '| ' + board['MID_R'])
    print('-+-+-')
    print(board['LOW_L'] + ' |' + board['LOW_M'] + ' | ' + board['LOW_R'])

#create empty board
#print empty board

#choose spot on board 
#placement = input()
#board[placement] = 'x' #replace with x or o based on turn
#printBoard(board)
printBoard(board)
mark = 'x'
win = 0

def checkWin(move):
#   if board['HIGH_L'] == board['HIGH_M'] == board['HIGH_R']:
#        print(' Player : ' + mark + ' wins')
#        win = 1
#        return win

def changePlayer(player):
    
    if spot%2 == 0:
        return 'o'
    else:
        return 'x'

for spot in range(9):
    print('turn for ' + mark + ' Turn ' + str(spot) + ' Type a spot' )
    move = input()
    #check if value exists in key. If so, input a different spot
    while board[move]:
        print('Try another spot')
        printBoard(board)
        move = input()
    board[move] = mark
    #check mark based on turn order
    checkWin()
    if win == 1:
        break
    
    mark = changePlayer(spot)
    printBoard(board)
    
    #based on move, check winning sets
    #2 winning setson sides 
    #3 winning sets on corners
    #4 winning sets in middle

winning_set = {
    "HIGH_L": {1: ["HIGH_M","HIGH_R"],2:["MID_M","LOW_R"],3:["MID_L","LOW_L"]},

}




    


        



    





