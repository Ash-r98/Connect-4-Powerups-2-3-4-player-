from time import sleep

class Column():
    def __init__(self, fmaxsize):
        self.maxsize = fmaxsize
        self.stack = []
        for i in range(fmaxsize):
            self.stack.append('-')
        self.top = 0

    def isempty(self):
        if self.top <= 0:
            return True
        return False

    def isfull(self):
        if self.top >= self.maxsize:
            return True
        return False

    def push(self, item):
        if not self.isfull():
            self.stack[self.top] = item
            self.top += 1
        else:
            print("Stack is full")

    def pop(self):
        if not self.isempty():
            self.top -= 1
            temp = self.stack[self.top]
            self.stack[self.top] = '-'
            return temp
        else:
            print("Stack is empty")
            return -1

    def peek(self):
        if not self.isempty():
            temp = self.stack[self.top]
            return temp
        else:
            print("Stack is empty")
            return -1

def display():
    global rowsize
    global colsize
    global columnlist
    global lastmove
    firstobj = True
    top = ''
    for i in range(rowsize):
        top += str(i+1) + ' '
    top.strip()
    print(f"\nBoard:\n\033[2m{top}\033[0m")
    for i in range(colsize-1, -1, -1):
        tempstring = ''
        for j in range(rowsize):
            if columnlist[j].stack[i] == skins[0][0]:
                if j == lastmove and firstobj: # If the first object in the last move column then italic
                    tempstring += f'\033[3;{skins[0][1]}m{skins[0][0]}\033[0m' + ' '
                    firstobj = False
                else:
                    tempstring += f'\033[1;{skins[0][1]}m{skins[0][0]}\033[0m' + ' '
            elif columnlist[j].stack[i] == skins[1][0]:
                if j == lastmove and firstobj:  # If the first object in the last move column then italic
                    tempstring += f'\033[3;{skins[1][1]}m{skins[1][0]}\033[0m' + ' '
                    firstobj = False
                else:
                    tempstring += f'\033[1;{skins[1][1]}m{skins[1][0]}\033[0m' + ' '
            elif columnlist[j].stack[i] == skins[2][0]:
                if j == lastmove and firstobj:  # If the first object in the last move column then italic
                    tempstring += f'\033[3;{skins[2][1]}m{skins[2][0]}\033[0m' + ' '
                else:
                    tempstring += f'\033[1;{skins[2][1]}m{skins[2][0]}\033[0m' + ' '
            elif columnlist[j].stack[i] == skins[3][0]:
                if j == lastmove and firstobj:  # If the first object in the last move column then italic
                    tempstring += f'\033[3;{skins[3][1]}m{skins[3][0]}\033[0m' + ' '
                else:
                    tempstring += f'\033[1;{skins[3][1]}m{skins[3][0]}\033[0m' + ' '
            else:
                tempstring += columnlist[j].stack[i] + ' '
        print(tempstring.strip(' '))
    print()

def powerups(powerupsremaining):
    morepowerups = False
    for i in range(len(powerupsremaining)):
        if powerupsremaining[i]:
            morepowerups = True
    if not morepowerups:
        print("You have no powerups remaining")
        return 0, powerupsremaining
    else:
        print("Powerups:")
        if powerupsremaining[0]:
            print("1 - Skip next player's turn")
        else:
            print("\033[2m1 - Skip next player's turn - Used\033[0m")
        if powerupsremaining[1]:
            print("2 - Double drop")
        else:
            print("\033[2m2 - Double drop - Used\033[0m")#
        if powerupsremaining[2]:
            print("3 - Destroy top of column")
        else:
            print("\033[2m3 - Destroy top of column - Used\033[0m")
        if powerupsremaining[3]:
            print("4 - Destroy bottom of column")
        else:
            print("\033[2m4 - Destroy bottom of column - Used\033[0m")
        if powerupsremaining[4]:
            print("5 - Disable specific enemy powerup")
        else:
            print("\033[2m5 - Disable specific enemy powerup - Used\033[0m")
        if powerupsremaining[5]:
            print("6 - Steal the last move (instead of placing)")
        else:
            print("\033[2m6 - Steal the last move (instead of placing) - Used\033[0m")
        print("\033[31mq - Quit\033[0m")
        while True:
            powerup = input("Input selection:\n")
            if powerup == 'q':
                break
            try:
                powerup = int(powerup)
                if powerupsremaining[powerup - 1]:
                    powerupsremaining[powerup - 1] = False
                    break
                else:
                    1 / 0
            except:
                print("Invalid input")
        return powerup, powerupsremaining

def turn(player, powerupsremaining, powerupused):
    global lastmove
    global enablepowers
    display()
    if player == 0: # 0 = Player 1
        print(f"Player 1 turn - \033[1;{skins[0][1]}m{skins[0][0]}\033[0m")
    elif player == 1: # 1 = Player 2
        print(f"Player 2 turn - \033[1;{skins[1][1]}m{skins[1][0]}\033[0m")
    elif player == 2: # 2 = Player 3
        print(f"Player 3 turn - \033[1;{skins[2][1]}m{skins[2][0]}\033[0m")
    elif player == 3: # 3 = Player 4
        print(f"Player 4 turn - \033[1;{skins[3][1]}m{skins[3][0]}\033[0m")
    if enablepowers:
        print("Input 'p' for powerups menu")
    while True:
        col = input("Column:\n").lower()
        if col == 'p':
            if not enablepowers:
                print("Powerups are disabled")
            else:
                if powerupused:
                    print("You have already used a powerup this turn")
                else:
                    break
        elif col == '`':
            break
        try:
            col = int(col)
            col -= 1
            if col >= 0 and col < rowsize:
                break
            else:
                1 / 0
        except:
            print("Invalid input")
    if col == 'p':
        # Put powerups subroutine in here when completed
        powerup = powerups(powerupsremaining)
        if powerup[0] == 'q':
            return turn(player, powerupsremaining, powerupused)
        else:
            return False, powerup[0], powerup[1]
    elif col == '`':
        return False, '`'
    else:
        lastmove = col
        return True, col

def endgame(x, o, v, t):
    if x == 4:
        display()
        print(f"\033[1;{skins[0][1]}mPlayer 1 wins!\033[0m")
        sleep(5)
        quit()
    elif o == 4:
        display()
        print(f"\033[1;{skins[1][1]}mPlayer 2 wins!\033[0m")
        sleep(5)
        quit()
    elif v == 4:
        display()
        print(f"\033[1;{skins[2][1]}mPlayer 3 wins!\033[0m")
        sleep(5)
        quit()
    elif t == 4:
        display()
        print(f"\033[1;{skins[3][1]}mPlayer 4 wins!\033[0m")
        sleep(5)
        quit()

def findwin():
    global rowsize
    global colsize
    global columnlist
    x = 0
    o = 0
    v = 0
    t = 0
    # Horizontal wins
    for col in range(colsize):
        for row in range(rowsize):
            if columnlist[row].stack[col] == skins[0][0]:
                x += 1
                o = 0
                v = 0
                t = 0
            elif columnlist[row].stack[col] == skins[1][0]:
                x = 0
                o += 1
                v = 0
                t = 0
            elif columnlist[row].stack[col] == skins[2][0]:
                x = 0
                o = 0
                v += 1
                t = 0
            elif columnlist[row].stack[col] == skins[3][0]:
                x = 0
                o = 0
                v = 0
                t += 1
            else:
                x = 0
                o = 0
                v = 0
                t = 0
            endgame(x, o, v, t)
        x = 0
        o = 0
        v = 0
        t = 0
    # Vertical win detection
    for row in range(rowsize):
        for col in range(colsize):
            if columnlist[row].stack[col] == skins[0][0]:
                x += 1
                o = 0
                v = 0
                t = 0
            elif columnlist[row].stack[col] == skins[1][0]:
                x = 0
                o += 1
                v = 0
                t = 0
            elif columnlist[row].stack[col] == skins[2][0]:
                x = 0
                o = 0
                v += 1
                t = 0
            elif columnlist[row].stack[col] == skins[3][0]:
                x = 0
                o = 0
                v = 0
                t += 1
            else:
                x = 0
                o = 0
                v = 0
                t = 0
            endgame(x, o, v, t)
        x = 0
        o = 0
        v = 0
        t = 0
    # Diagonal win detection
    if rowsize >= 4 and colsize >= 4: # If diagonal wins are possible
        for offset in range(3-rowsize, rowsize-3):
            for i in range(colsize):
                if i >= rowsize:
                    break
                temp = i+offset
                if temp < colsize:
                    if columnlist[temp].stack[i] == skins[0][0]:
                        x += 1
                        o = 0
                        v = 0
                        t = 0
                    elif columnlist[temp].stack[i] == skins[1][0]:
                        x = 0
                        o += 1
                        v = 0
                        t = 0
                    elif columnlist[temp].stack[i] == skins[2][0]:
                        x = 0
                        o = 0
                        v += 1
                        t = 0
                    elif columnlist[temp].stack[i] == skins[3][0]:
                        x = 0
                        o = 0
                        v = 0
                        t += 1
                    else:
                        x = 0
                        o = 0
                        v = 0
                        t = 0
                    endgame(x, o, v, t)
        for offset in range(3-rowsize, rowsize-3):
            for i in range(colsize):
                if i >= rowsize:
                    break
                temp = i+offset
                if temp < colsize:
                    if columnlist[temp].stack[colsize-1-i] == skins[0][0]:
                        x += 1
                        o = 0
                        v = 0
                        t = 0
                    elif columnlist[temp].stack[colsize-1-i] == skins[1][0]:
                        x = 0
                        o += 1
                        v = 0
                        t = 0
                    elif columnlist[temp].stack[colsize-1-i] == skins[2][0]:
                        x = 0
                        o = 0
                        v += 1
                        t = 0
                    elif columnlist[temp].stack[colsize-1-i] == skins[3][0]:
                        x = 0
                        o = 0
                        v = 0
                        t += 1
                    else:
                        x = 0
                        o = 0
                        v = 0
                        t = 0
                    endgame(x, o, v, t)


# Board size
rowsize = 7
colsize = 6

# Saves last column a move was played in
lastmove = -1

# Player Skins
# [Symbol, ANSI colour code]
p1skin = ['X', 31] # Red
p2skin = ['O', 34] # Blue
p3skin = ['V', 32] # Green
p4skin = ['T', 35] # Purple
skins = [p1skin, p2skin, p3skin, p4skin]

# List of powerups per player
p1powerups = [True, True, True, True, True, True] # True if powerup is unused
p2powerups = [True, True, True, True, True, True] # True if powerup is unused
p3powerups = [True, True, True, True, True, True] # True if powerup is unused
p4powerups = [True, True, True, True, True, True] # True if powerup is unused

# Player powerup variables
skip1 = False
skip2 = False
skip3 = False
skip4 = False
double1 = False
double2 = False
double3 = False
double4 = False
destroytop1 = False
destroytop2 = False
destroytop3 = False
destroytop4 = False
destroybase1 = False
destroybase2 = False
destroybase3 = False
destroybase4 = False
resetcolumn = Column(colsize) # Temporary column used for destruction powerup
disablepower1 = False
disablepower2 = False
disablepower3 = False
disablepower4 = False

p1powerupused = False # Only 1 powerup can be used per turn, resets on other player's turn
p2powerupused = False
p3powerupused = False
p4powerupused = False

while True:
    enablepowers = input("Powerups? (y/n)\n").lower()
    if enablepowers == 'y':
        enablepowers = True
        break
    elif enablepowers == 'n':
        enablepowers = False
        break
    else:
        print("Invalid input")

p3 = False
while True:
    p3 = input("3 players? (y/n)\n").lower()
    if p3 == 'y':
        p3 = True
        break
    elif p3 == 'n':
        p3 = False
        break
    else:
        print("Invalid input")

p4 = False
if p3:
    while True:
        p4 = input("4 players? (y/n)\n").lower()
        if p4 == 'y':
            p4 = True
            break
        elif p4 == 'n':
            p4 = False
            break
        else:
            print("Invalid input")
if p4: # If 4 players, increase board size
    rowsize = 9
    colsize = 8


# Creating board
columnlist = []
for i in range(rowsize):
    columnlist.append(Column(colsize))


player = 0 # 0 = player 1, 1 = player 2, 2 = player 3, 3 = player 4
while True:
    findwin()
    # Player 1 time
    player = 0
    if skip1 == False:
        p2powerupused = False
        p3powerupused = False
        p4powerupused = False
        while True:
            if disablepower1:
                while True:
                    disabled = input("Select a powerup to disable:\n")
                    try:
                        disabled = int(disabled)
                        if disabled > 0 and disabled < 7:
                            break
                        else:
                            1 / 0
                    except:
                        print("Invalid input")
                p2powerups[disabled-1] = False
                p3powerups[disabled-1] = False
                p4powerups[disabled - 1] = False
                disablepower1 = False
                continue
            cmd1 = turn(player, p1powerups, p1powerupused)
            if cmd1[0]:
                col1 = cmd1
                if destroytop1:
                    columnlist[col1[1]].pop()
                    columnlist[col1[1]].push('-')
                    columnlist[col1[1]].top -= 1
                    destroytop1 = False
                    continue
                if destroybase1:
                    temptop = columnlist[col1[1]].top-1
                    for i in range(temptop):
                        resetcolumn.push(columnlist[col1[1]].pop())
                    columnlist[col1[1]].pop() # Destroys the final item
                    temptop = resetcolumn.top
                    for i in range(temptop):
                        columnlist[col1[1]].push(resetcolumn.pop())
                    destroybase1 = False
                    continue
                columnlist[col1[1]].push(skins[0][0])
                if double1:
                    columnlist[col1[1]].push(skins[0][0])
                    double1 = False
                break
            else:
                # Passing (`)
                if cmd1[1] == '`':
                    print('Passed')
                    break
                # Powerups
                p1powerupused = True
                p1powerups = cmd1[2]
                if cmd1[1] == 1:
                    skip2 = True
                elif cmd1[1] == 2:
                    double1 = True
                elif cmd1[1] == 3:
                    destroytop1 = True
                elif cmd1[1] == 4:
                    destroybase1 = True
                elif cmd1[1] == 5:
                    disablepower1 = True
                elif cmd1[1] == 6:
                    columnlist[lastmove].pop()
                    columnlist[lastmove].push(skins[0][0])
                    break
    else:
        print("Player 1's turn was skipped!")
        skip1 = False
    findwin()
    # Player 2 time
    player = 1
    if skip2 == False:
        p1powerupused = False
        p3powerupused = False
        p4powerupused = False
        while True:
            if disablepower2:
                while True:
                    disabled = input("Select a powerup to disable:\n")
                    try:
                        disabled = int(disabled)
                        if disabled > 0 and disabled < 7:
                            break
                        else:
                            1 / 0
                    except:
                        print("Invalid input")
                p1powerups[disabled-1] = False
                p3powerups[disabled-1] = False
                p4powerups[disabled - 1] = False
                disablepower2 = False
                continue
            cmd2 = turn(player, p2powerups, p2powerupused)
            if cmd2[0]:
                col2 = cmd2
                if destroytop2:
                    columnlist[col2[1]].pop()
                    columnlist[col2[1]].push('-')
                    columnlist[col2[1]].top -= 1
                    destroytop2 = False
                    continue
                if destroybase2:
                    temptop = columnlist[col2[1]].top-1
                    for i in range(temptop):
                        resetcolumn.push(columnlist[col2[1]].pop())
                    columnlist[col2[1]].pop() # Destroys the final item
                    temptop = resetcolumn.top
                    for i in range(temptop):
                        columnlist[col2[1]].push(resetcolumn.pop())
                    destroybase2 = False
                    continue
                columnlist[col2[1]].push(skins[1][0])
                if double2:
                    columnlist[col2[1]].push(skins[1][0])
                    double2 = False
                break
            else:
                # Passing (`)
                if cmd2[1] == '`':
                    print('Passed')
                    break
                # Powerups
                p2powerupused = True
                p2powerups = cmd2[2]
                if cmd2[1] == 1:
                    if p3:
                        skip3 = True
                    else:
                        skip1 = True
                elif cmd2[1] == 2:
                    double2 = True
                elif cmd2[1] == 3:
                    destroytop2 = True
                elif cmd2[1] == 4:
                    destroybase2 = True
                elif cmd2[1] == 5:
                    disablepower2 = True
                elif cmd2[1] == 6:
                    columnlist[lastmove].pop()
                    columnlist[lastmove].push(skins[1][0])
                    break
    else:
        print("Player 2's turn was skipped!")
        skip2 = False
    findwin()
    # Player 3 time
    if p3:
        player = 2
        if skip3 == False:
            p1powerupused = False
            p2powerupused = False
            p4powerupused = False
            while True:
                if disablepower3:
                    while True:
                        disabled = input("Select a powerup to disable:\n")
                        try:
                            disabled = int(disabled)
                            if disabled > 0 and disabled < 7:
                                break
                            else:
                                1 / 0
                        except:
                            print("Invalid input")
                    p1powerups[disabled - 1] = False
                    p2powerups[disabled - 1] = False
                    p4powerups[disabled - 1] = False
                    disablepower3 = False
                    continue
                cmd3 = turn(player, p3powerups, p3powerupused)
                if cmd3[0]:
                    col3 = cmd3
                    if destroytop3:
                        columnlist[col3[1]].pop()
                        columnlist[col3[1]].push('-')
                        columnlist[col3[1]].top -= 1
                        destroytop3 = False
                        continue
                    if destroybase3:
                        temptop = columnlist[col3[1]].top - 1
                        for i in range(temptop):
                            resetcolumn.push(columnlist[col3[1]].pop())
                        columnlist[col3[1]].pop()  # Destroys the final item
                        temptop = resetcolumn.top
                        for i in range(temptop):
                            columnlist[col3[1]].push(resetcolumn.pop())
                        destroybase3 = False
                        continue
                    columnlist[col3[1]].push(skins[2][0])
                    if double3:
                        columnlist[col3[1]].push(skins[2][0])
                        double3 = False
                    break
                else:
                    # Passing (`)
                    if cmd3[1] == '`':
                        print('Passed')
                        break
                    # Powerups
                    p3powerupused = True
                    p3powerups = cmd3[2]
                    if cmd3[1] == 1:
                        if p4:
                            skip4 = True
                        else:
                            skip1 = True
                    elif cmd3[1] == 2:
                        double3 = True
                    elif cmd3[1] == 3:
                        destroytop3 = True
                    elif cmd3[1] == 4:
                        destroybase3 = True
                    elif cmd3[1] == 5:
                        disablepower3 = True
                    elif cmd3[1] == 6:
                        columnlist[lastmove].pop()
                        columnlist[lastmove].push(skins[2][0])
                        break
        else:
            print("Player 3's turn was skipped!")
            skip3 = False
        findwin()
    if p4:
        player = 3
        if skip4 == False:
            p1powerupused = False
            p2powerupused = False
            p3powerupused = False
            while True:
                if disablepower4:
                    while True:
                        disabled = input("Select a powerup to disable:\n")
                        try:
                            disabled = int(disabled)
                            if disabled > 0 and disabled < 7:
                                break
                            else:
                                1 / 0
                        except:
                            print("Invalid input")
                    p1powerups[disabled - 1] = False
                    p2powerups[disabled - 1] = False
                    p3powerups[disabled - 1] = False
                    disablepower4 = False
                    continue
                cmd4 = turn(player, p4powerups, p4powerupused)
                if cmd4[0]:
                    col4 = cmd4
                    if destroytop4:
                        columnlist[col4[1]].pop()
                        columnlist[col4[1]].push('-')
                        columnlist[col4[1]].top -= 1
                        destroytop4 = False
                        continue
                    if destroybase4:
                        temptop = columnlist[col4[1]].top - 1
                        for i in range(temptop):
                            resetcolumn.push(columnlist[col4[1]].pop())
                        columnlist[col4[1]].pop()  # Destroys the final item
                        temptop = resetcolumn.top
                        for i in range(temptop):
                            columnlist[col4[1]].push(resetcolumn.pop())
                        destroybase4 = False
                        continue
                    columnlist[col4[1]].push(skins[3][0])
                    if double4:
                        columnlist[col4[1]].push(skins[3][0])
                        double4 = False
                    break
                else:
                    # Passing (`)
                    if cmd4[1] == '`':
                        print('Passed')
                        break
                    # Powerups
                    p4powerupused = True
                    p4powerups = cmd4[2]
                    if cmd4[1] == 1:
                        skip1 = True
                    elif cmd4[1] == 2:
                        double4 = True
                    elif cmd4[1] == 3:
                        destroytop4 = True
                    elif cmd4[1] == 4:
                        destroybase4 = True
                    elif cmd4[1] == 5:
                        disablepower4 = True
                    elif cmd4[1] == 6:
                        columnlist[lastmove].pop()
                        columnlist[lastmove].push(skins[2][0])
                        break
        else:
            print("Player 4's turn was skipped!")
            skip4 = False
        findwin()