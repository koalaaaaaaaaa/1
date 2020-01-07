import sys
def activate_2048():
    print('welcome to the world of 2048.')
    print()
    print('***produced by koala***')
    print()
    print('i have a few words to tell you')
    print('when you finish reading, please press the "enter" button to continue.')
    a=input()
    print('recommend font:"楷体"')
    a=input()
    print('recommend size:"13"')
    a=input()
    print('please click "Options"(above the surface)-"Configure IDLE" to change your settings ')
    print()
    a=input()
    print('please input "a"(left),"d"(right),"w"(up),"s"(down) to operate the table.')
    print()
    a=input()
    print('please input "start" to start the journey.')
    print()
    print()
    start=input()
    while start!='start':
        print('Hehe')
        print('please input "start" to start the journey.')
        start=input()
    game()

def game():
    global count
    print()
    print()
    print('new game starts!')
    global t
    t=[[0 for i in range(4)] for j in range(4)]
    count=0
    while True:
        count=count+1
        print()
        print()
        print('round '+str(count))
        print()

        add()

        end_check()

        input_move()

        check_move()

        win_check()
        

def input_move():
    import copy
    global check_change
    check_change=copy.deepcopy(t)
    global move
    move=input()
    if move=='a':
        l()
    elif move=='d':
        r()
    elif move=='w':
        u()
    elif move=='s':
        d()
    else:
        print('you are a naughty guy')
        input_move()
    

def add(): 
    check_num2=0
    empty=[]
    for i in range(0,4):
        for j in range(0,4):
            if t[i][j]==0:
                empty.append([i,j])
    if len(empty)!=0:
        from random import randint,choice
        for i in range(2):
            group=randint(0,len(empty)-1)
            a=empty[group][0]
            b=empty[group][1]
            c=choice([2,4])
            t[a][b]=c
            del empty[group]
            if empty==[]:
                break
    print_t()


def print_t():
    for i in range(0,4):
        for j in range(0,4):
            if 1<=(t[i][j]/10)<10:
                print(t[i][j],end='   ')
            elif 1<=(t[i][j]/100)<10:
                print(t[i][j],end='  ')
            elif 1<=(t[i][j]/1000)<10:
                print(t[i][j],end=' ')
            else:
                print(t[i][j],end='    ')
                
        print()
        print()
        print()
    print()


def l():
    global i
    for i in range(0,4):
        
        l_del0()
        
        for j in range(0,3):
            if t[i][j]==t[i][j+1]!=0:
                t[i][j]=2*t[i][j]
                t[i][j+1]=0
                
        l_del0()
        

def l_del0():
    global i
    new=[]
    for k in range(0,4):
        if t[i][k]!=0:
            new.append(t[i][k])
    while len(new)<4:
        new.append(0)
    t[i]=new
    
    
def r():
    global i
    for i in range(0,4):
        
        r_del0()
        
        for j in range(3,0,-1):
            if t[i][j]==t[i][j-1]!=0:
                t[i][j]=2*t[i][j]
                t[i][j-1]=0

        r_del0()
        

def r_del0():
    global i
    new=[]
    for k in range(3,-1,-1):
        if t[i][k]!=0:
            new.insert(0,t[i][k])
    while len(new)<4:
        new.insert(0,0)
    t[i]=new
        

def u():
    global j
    for j in range(0,4):
        
        u_del0()
        
        for i in range(0,3):
            if t[i][j]==t[i+1][j]!=0:
                t[i][j]=2*t[i][j]
                t[i+1][j]=0
                
        u_del0()
        

def u_del0():
    global j
    new=[]
    for k in range(0,4):
        if t[k][j]!=0:
            new.append(t[k][j])
    while len(new)<4:
        new.append(0)
    for m in range(4):
        t[m][j]=new[m]
            

def d():
    global j
    for j in range(0,4):
        
        d_del0()
        
        for i in range(3,0,-1):
            if t[i][j]==t[i-1][j]!=0:
                t[i][j]=2*t[i][j]
                t[i-1][j]=0
                
        d_del0()

        
def d_del0():
    global j
    new=[]
    for k in range(3,-1,-1):
        if t[k][j]!=0:
            new.insert(0,t[k][j])
    while len(new)<4:
        new.insert(0,0)
    for m in range(4):
        t[m][j]=new[m]

def end_check():
    global count
    check_num=0
    for i in range(4):
        for j in range(3):
            if t[i][j]==t[i][j+1] or t[i][j]==0 or t[i][j+1]==0:
                check_num=1
                break
        if check_num==1:
            break
    for j in range(4):
        for i in range(3):
            if t[i][j]==t[i+1][j] or t[i][j]==0 or t[i+1][j]==0:
                check_num=1
                break
        if check_num==1:
            break
    if check_num==0:    
        print('game over')
        print()
        print('you\'ve achieved   '+str(count)+'   round(s)')
        print()
        print('congratulations')
        print()
        print('input "again" to continue')
        print()
        print('input "end" to end')
        print()
        choose=input()
        while True:
            if choose=='end':
                print('goodbye~ have a nice day!')
                sys.exit()
            elif choose=='again':
                game()
            else:
                print('can\'t understand your meaning…')
                print()
                print('input "again" to continue')
                print()
                print('input "end" to end')
                print()
                choose=input()
                continue

def check_move():
    while check_change==t:
        print('useless move! please try another move.')
        input_move()

def win_check():
    for i in range(4):
        for j in range(4):
            if t[i][j]==2048:
                print('excellent! you win the game!')
                    
    
activate_2048()
    
