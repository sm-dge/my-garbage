import Stuff.players as p
import Stuff.game as g

# File select
while True:
    p.isp1()
    if p.p1 == True:
        break
    if p.p1 == False:
        p.isp2()
        if p.p2 == True:
            break
    if p.p1 == False and p.p2 == False:
        p.isp3()
        if p.p3 == True:
            break
    if p.p1 == False and p.p2 == False and p.p3 == False:
        p.delp()
        if p.p1 == True or p.p2 == True or p.p3 == True:
            break

print(f'\nwelcome, {p.pname}. scores are saved when exiting the game\n')
# Play game
while True:
    g.rps()
    g.again()