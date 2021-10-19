#This is going to be my first python game :)
import os

playingboard = '''
 /=================================\ 
||___||___||___||___||___||___||___||
||___||___||___||___||___||___||___||
||___||___||___||___||___||___||___||
||___||___||___||___||___||___||___||
||___||___||___||___||___||___||___||
||___||___||___||___||___||___||___||
/\ 1    2    3    4    5    6    7 /\ '''

game = 0
column = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0}
row1 = {'1': 232, '2': 237, '3': 242, '4': 247, '5': 252, '6': 257, '7': 262}

matrix0 = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]

matrix1 = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]


def checkifwon(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            global game
            #vertically up
            try:
                if matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j] + matrix[i + 3][j] >= 4:
                    game = 'won'
                    break
            except IndexError:
                pass
            #vertically down
            try:
                if matrix[i][j] + matrix[i - 1][j] + matrix[i - 2][j] + matrix[i - 3][j] == 4:
                    game = 'won'
                    break
            except IndexError:
                pass
            #horizontally right
            try:
                if matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i][j + 3] >= 4:
                    game = 'won'
                    break
            except IndexError:
                pass
            #horizontally left
            try:
                if matrix[i][j] + matrix[i][j - 1] + matrix[i][j - 2] + matrix[i][j - 3] == 4:
                    game = 'won'
                    break
            except IndexError:
                pass
            #diagonally up right
            try:
                if matrix[i][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 2] + matrix[i + 3][j + 3] >= 4:
                    game = 'won'
                    break
            except IndexError:
                pass
            #diagonally down left
            try:
                if matrix[i][j] + matrix[i - 1][j - 1] + matrix[i - 2][j - 1] + matrix[i - 3][j - 1] == 4:
                    game = 'won'
                    break
            except IndexError:
                pass
            #diagonally down right
            try:
                if matrix[i][j] + matrix[i - 1][j + 1] + matrix[i - 2][j + 2] + matrix[i - 3][j + 3] >= 4:
                    game = 'won'
                    break
            except IndexError:
                pass
            #diagonally up left
            try:
                if matrix[i][j] + matrix[i + 1][j - 1] + matrix[i + 2][j - 2] + matrix[i + 3][j - 3] == 4:
                    game = 'won'
                    break
            except IndexError:
                pass

        if game == 'won':
            print('game is won by player ' + player + '!')
            return True
            break

print(playingboard)
while game != 'won':
    if checkifwon(matrix0) or checkifwon(matrix1):
        break
    if sum(column.values()) % 2 == 0:
        player = '0'
        matrix = matrix0

    else:
        player = '1'
        matrix = matrix1

    choice = input('Choose column... ')
    if int(choice) >= 1 and int(choice) <= 7 and column[choice] <= 5:
        #calculate index
        index = row1[choice] - (38 * column[choice])
        #update playingboard
        playingboard = playingboard[:index] + player + playingboard[index + 1:]
        #keep track of columns
        column[choice] += 1
        #update matrix
        matrix[6 - column[choice]][int(choice)] = 1
        #refresh terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print(playingboard)
    elif int(choice) == 8:
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(playingboard); print('Invalid move bitch')