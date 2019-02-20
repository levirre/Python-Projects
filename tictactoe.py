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
    if spot%2 == 0:
        mark = 'o'
    else:
        mark = 'x'
    printBoard(board)
    





