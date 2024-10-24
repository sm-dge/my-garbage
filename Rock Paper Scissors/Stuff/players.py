import Stuff.game as g
p1 = False
p2 = False
p3 = False

# Creates/overwrites the file in the player 1 slot
def newp1():
    with open('rpsdata.txt', 'w') as f:
        global pwin
        global cwin
        global pname
        pwin = 0
        cwin = 0
        pname = input('enter your name: ')
        f.write('0' + '\n' + '0' + '\n' + pname)

# Reads from the file in the player 1 slot
def oldp1():
    with open('rpsdata.txt', 'r') as f:
        global data
        global pwin
        global cwin
        global pname
        data = f.readlines()
        data[0] = data[0].strip()
        data[1] = data[1].strip()
        pwin = int(data[0])
        cwin = int(data[1])
        pname = data[2]

# Creates/overwrites the file in the player 2 slot
def newp2():
    with open('rpsdata1.txt', 'w') as f:
        global pwin
        global cwin
        global pname
        pwin = 0
        cwin = 0
        pname = input('enter your name: ')
        f.write('0' + '\n' + '0' + '\n' + pname)

# Reads from the file in the player 2 slot
def oldp2():
    with open('rpsdata1.txt', 'r') as f:
        global data
        global pwin
        global cwin
        global pname
        data = f.readlines()
        data[0] = data[0].strip()
        data[1] = data[1].strip()
        pwin = int(data[0])
        cwin = int(data[1])
        pname = data[2]

# Creates/overwrites the file in the player 3 slot
def newp3():
    with open('rpsdata2.txt', 'w') as f:
        global pwin
        global cwin
        global pname
        pwin = 0
        cwin = 0
        pname = input('enter your name: ')
        f.write('0' + '\n' + '0' + '\n' + pname)

# Reads from the file in the player 3 slot
def oldp3():
    with open('rpsdata2.txt', 'r') as f:
        global data
        global pwin
        global cwin
        global pname
        data = f.readlines()
        data[0] = data[0].strip()
        data[1] = data[1].strip()
        pwin = int(data[0])
        cwin = int(data[1])
        pname = data[2]

# Asks if player 1 is playing
def isp1():
    global p1
    global select
    try:
        oldp1()
        while True:
            select = input(f'is {pname} playing?: ').lower()
            try:
                select = select[0]
            except IndexError:
                print('invalid')
                continue
            if select == 'y':
                p1 = True
                break    
            elif select == 'n':
                p1 = False
                break
    except FileNotFoundError:
        newp1()
        p1 = True

# Asks if player 2 is playing
def isp2():
    global p2
    global select
    try:
        oldp2()
        while True:
            select = input(f'is {pname} playing?: ').lower()
            try:
                select = select[0]
            except IndexError:
                print('invalid')
                continue
            if select == 'y':
                p2 = True
                break    
            elif select == 'n':
                p2 = False
                break
    except FileNotFoundError:
        newp2()
        p2 = True

# Asks if player 3 is playing
def isp3():
    global p3
    global select
    try:
        oldp3()
        while True:
            select = input(f'is {pname} playing?: ').lower()
            try:
                select = select[0]
            except IndexError:
                print('invalid')
                continue
            if select == 'y':
                p3 = True
                break    
            elif select == 'n':
                p3 = False
                break
    except FileNotFoundError:
        newp3()
        p3 = True

# Asks which file to delete
def delp():
    global f1
    global f2
    global f3
    global p1
    global p2
    global p3
    global which
    global pwin
    global cwin
    global pname
    oldp1()
    f1 = pname
    oldp2()
    f2 = pname
    oldp3()
    f3 = pname
    print('all files are full')
    while True:
        which = input(f"type '{f1}', '{f2}', or '{f3}' to delete that file or 'back' to go back: ").lower()
        if which == f1:
            newp1()
            p1 = True
            break
        elif which == f2:
            oldp2()
            p2 = True
            break
        elif which == f3:
            newp3()
            p3 = True
            break
        elif which == 'back':
            print('\n')
            break  