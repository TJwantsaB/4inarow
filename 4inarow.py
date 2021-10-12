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

game = 'started'
counter = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0}
row1 = {'1': 232, '2': 237, '3': 242, '4': 247, '5': 252, '6': 257, '7': 262}
print(sum(counter.values()))



print(playingboard)
while game != 'won':
    if sum(counter.values()) % 2 == 0:
        player = '0'
    else:
        player = '1'

    choice = input('Choose column... ')

    index = row1[choice] - (38 * counter[choice])
    playingboard = playingboard[:index] + player + playingboard[index + 1:]
    counter[choice] += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    print(playingboard)

