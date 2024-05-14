import random

score = 0
matix = [[0 for i in range(4)] for i in range(4)]

def notzero(s):
    return s if s != 0 else ''

def display():
    print("\
        \t┌────┬────┬────┬────┐\n\
        \t│%4s│%4s│%4s│%4s│\n\
        \t│────┼────┼────┼────┤\n\
        \t│%4s│%4s│%4s│%4s│\n\
        \t│────┼────┼────┼────┤\n\
        \t│%4s│%4s│%4s│%4s│\n\
        \t│────┼────┼────┼────┤\n\
        \t│%4s│%4s│%4s│%4s│\n\
        \t└────┴────┴────┴────┘"
        %(notzero(matix[0][0]), notzero(matix[0][1]), notzero(matix[0][2]), notzero(matix[0][3]), \
          notzero(matix[1][0]), notzero(matix[1][1]), notzero(matix[1][2]), notzero(matix[1][3]), \
          notzero(matix[2][0]), notzero(matix[2][1]), notzero(matix[2][2]), notzero(matix[2][3]), \
          notzero(matix[3][0]), notzero(matix[3][1]), notzero(matix[3][2]), notzero(matix[3][3]),)
        )

def init():
    init_num_flag = 0
    while 1:
        k = 2 if random.randrange(0, 10) > 1 else 4
        s = divmod(random.randrange(0, 16), 4)
        if matix[s[0]][s[1]] == 0:
           matix[s[0]][s[1]] = k
           init_num_flag += 1
           if init_num_flag == 2:
              break
    display()

def add_random_num():
    while 1:
        k = 2 if random.randrange(0, 10) > 1 else 4
        s = divmod(random.randrange(0, 16), 4)
        if matix[s[0]][s[1]] == 0:
           matix[s[0]][s[1]]  = k
           break
    display()

def check():
    for i in range(4):
        for j in range(3):
            if matix[i][j] == 0 or matix[i][j] == matix[i][j + 1] or matix[j][i] == matix[j + 1][i]:
                return True
    else:
        return False

def move_right():
    global score
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j - 1, -1, -1):
                if matix[i][k] > 0:
                    if matix[i][j] == 0:
                       matix[i][j] = matix[i][k]
                       matix[i][k] = 0
                    elif matix[i][j] == matix[i][k]:
                         matix[i][j] *= 2
                         score += matix[i][j]
                         matix[i][k] = 0
                    break
    add_random_num()

def move_left():
    global score
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j + 1, 4):
                if matix[i][k] > 0:
                    if matix[i][j] == 0:
                       matix[i][j] = matix[i][k]
                       matix[i][k] = 0
                    elif matix[i][j] == matix[i][k]:
                         matix[i][j] *= 2
                         score += matix[i][j]
                         matix[i][k] = 0
                    break
    add_random_num()

def move_up():
    global score
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j + 1, 4):
                if matix[k][i] > 0:
                    if matix[j][i] == 0:
                       matix[j][i] = matix[k][i]
                       matix[k][i] = 0
                    elif matix[j][i] == matix[k][i]:
                         matix[j][i] *= 2
                         score += matix[j][i]
                         matix[k][i] = 0
                    break
    add_random_num()

def move_down():
    global score
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j - 1, -1, -1):
                if matix[k][i] > 0:
                    if matix[j][i] == 0:
                       matix[j][i] = matix[k][i]
                       matix[k][i] = 0
                    elif matix[j][i] == matix[k][i]:
                         matix[j][i] *= 2
                         score += matix[j][i]
                         matix[k][i] = 0
                    break
    add_random_num()

def main():
    print("\tWelcom to the Game of 2048!")
    flag = True
    init()
    while flag:
        print("\t\tYou Score: %s" %(score))
        d = input("(w:↑) (s:↓) (a:←) (d:→) (q:quit) :")
        if d == 'a':
            move_left
            if not check():
                print("GG")
                flag = False
        elif d == 's':
            move_down()
            if not check():
                print("GG")
                flag = False
        elif d == 'w':
            move_up()
            if not check():
                print("GG")
                flag = False
        elif d == 'd':
            move_right()
            if not check():
                print("GG")
                flag = False
        elif d == 'q':
            break
        else:
            pass

if __name__ == '__main__':
    main()