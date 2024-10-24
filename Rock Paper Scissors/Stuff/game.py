import random as r
import time as t
import Stuff.players as p

# Plays Rock Paper Scissors
def rps():
    global choices
    global pchoice
    global cchoice
    choices = ['rock', 'paper', 'scissors']
    cchoice = r.choice(choices)
    while True:
        pchoice = input('rock, paper or scissors?: ').lower()
        try:
            pchoice = pchoice[0]
        except IndexError:
            print('invalid')
            continue

        if pchoice == 'r':
            print('you chose rock')
            if cchoice == 'rock':
                print('i chose rock')
                print('tie')
            elif cchoice == 'paper':
                print('i chose paper')
                print('i win')
                p.cwin += 1
            elif cchoice == 'scissors':
                print('you win')
                p.pwin += 1
            
        elif pchoice == 'p':
            print('you chose paper')
            if cchoice == 'rock':
                print('i chose rock')
                print('you win')
                p.pwin += 1
            elif cchoice == 'paper':
                print('i chose paper')
                print('tie')
            elif cchoice == 'scissors':
                print('i win')
                p.cwin += 1
        
        elif pchoice == 's':
            print('you chose scissors')
            if cchoice == 'rock':
                print('i chose rock')
                print('i win')
                p.cwin += 1
            elif cchoice == 'paper':
                print('i chose paper')
                print('you win')
                p.pwin += 1
            elif cchoice == 'scissors':
                print('tie')
            
        else:
            print('invalid')
            continue
        print(f'you have won {p.pwin} games. i have won {p.cwin} games\n')
        break

#Asks to start another game
def again():
    while True:
        ask = input('play again?: ').lower()
        try:
            ask = ask[0]
        except IndexError:
            print('invalid')
            continue
        if ask == 'y':
            print('')
            break
        if ask == 'n':
            p.pwin = str(p.pwin)
            p.cwin = str(p.cwin)
            if p.p1 == True:
                with open('rpsdata.txt', 'w') as f:
                    f.write(p.pwin + '\n' + p.cwin + '\n' + p.pname)
            elif p.p2 == True:
                with open('rpsdata1.txt', 'w') as f:
                    f.write(p.pwin + '\n' + p.cwin + '\n' + p.pname)
            elif p.p3 == True:
                with open('rpsdata2.txt', 'w') as f:
                    f.write(p.pwin + '\n' + p.cwin + '\n' + p.pname)
            exit()
        else:
            print('invalid')
            continue