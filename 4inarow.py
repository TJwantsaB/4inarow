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
counter = [0, 0, 0, 0, 0 ,0, 0]
row1 = {'1': 232, '2': 237, '3': 242, '4': 247, '6': 252, '7': 257}
print(sum(counter))


print(playingboard)
while game != 'won':
    if sum(counter) % 2 != 0:
        player = '0'
    else:
        player = '1'

    choice = input('Choose column... ')
    if choice == '1':
        index = 232 - (38 * counter[0])
        playingboard = playingboard[:index] + player + playingboard[index + 1:]
        counter[0] += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(playingboard)
    elif choice == '2':
        break
