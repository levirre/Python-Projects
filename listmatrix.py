#create function to take in lists within list and transpose it
# [1 2 3]
# [4 5 6]
# [7 8 9] to

# [1 4 7]
# [2 5 8]
# [3 6 9]

matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def transpose(listmatrix):
    row = len(listmatrix)
    col = len(listmatrix[0])
    
    # range(stop)
#stop: Number of integers (whole numbers) to generate, starting from zero. eg. 
# range(3) == [0, 1, 2].
    #initial loop for traversing master list
    for listcounter in range(col):   
        for i in range(row):
            #loop through each individual list
            print(listmatrix[i][listcounter],end=' ')
        print()
           
                
            
        



transpose(grid)
transpose(matrix)