#board = {
#    'HIGH_L':'','HIGH_M':'','HIGH_R':'',
#    'MID_L':'','MID_M':'','MID_R':'',
#    'LOW_L':'','LOW_M':'','LOW_R':''
#}
moves_left = [0,1,2,3,4,5,6,7,8,9]
board = {
    7:'',8:'',9:'',
    4:'',5:'',6:'',
    1:'',2:'',3:''
}
winning_set = {
    1: {1,2,3,4,5,7,9}
}
# moves_left = ['HIGH_L','HIGH_M','HIGH_R','MID_L','MID_M','MID_R','LOW_L','LOW_M','LOW_R']
player_moves = {'x':[],'o':[]}
def printBoard(board): 
    print(board[7] + '| ' + board[8] + '| ' + board[9])
    print('-+-+-')

    print(board[4] + ' |' + board[5] + '| ' + board[6])
    print('-+-+-')
    print(board[1] + ' |' + board[2] + ' | ' + board[3])

#create empty board
#print empty board

#choose spot on board 
#placement = input()
#board[placement] = 'x' #replace with x or o based on turn
#printBoard(board)
printBoard(board)
mark = 'x'
win = False

#def checkWin(move):
#   if board['HIGH_L'] == board['HIGH_M'] == board['HIGH_R']:
#        print(' Player : ' + mark + ' wins')
#        win = 1
#        return win


def checkWin(curr_move,player):
    
#player_moves[x].append('HIGH_L')
#player_moves['x'].remove('HIGH_L')
#add previous move to player moves
#remove move from available pool
    #moves_left.remove(curr_move)
    player_moves[player].append(curr_move)
    if len(player_moves[player]) < 3:
        return 
    if set(player_moves[player]).issubset(winning_set[curr_move]):
        win = True
        return win

#get move
#check if player has made move that is within a winning set based on previous moves
#build all possible winning sets from current move
#check available sets with current move with only numbers inside moves_left









        
            
    

    

def changePlayer(player):
    if spot%2 == 0:
        return 'o'
    else:
        return 'x'

for spot in range(9):
    print('turn for ' + mark + ' Turn ' + str(spot) + ' Type a spot' )
    move = input()
    #check if value exists in key. If so, input a different spot
    while board[int(move)]:
        print('Try another spot')
        printBoard(board)
        move = input()
    board[int(move)] = mark
    #check mark based on turn order
    checkWin(move,mark)
    
    mark = changePlayer(spot)
    printBoard(board)
    
    #based on move, check winning sets
    #2 winning setson sides 
    #3 winning sets on corners
    #4 winning sets in middle



    


        



    





