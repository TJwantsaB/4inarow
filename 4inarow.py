#This is going to be my first python game :)

from colorama import Fore, Back, Style

playingboard = '''
 /=================================\ 
||___||___||___||___||___||___||___||
||___||___||___||___||___||___||___||
||___||___||___||___||___||___||___||
||___||___||___||___||___||___||___||
||___||___||___||___||___||___||___||
||___||___||___||___||___||___||___||
/\                                 /\ '''
index = 262
#playingboard update function
playingboard = playingboard[:index] + '1' + playingboard[index + 1:]
index = 257
playingboard = playingboard[:index] + '0' + playingboard[index + 1:]
print(playingboard)