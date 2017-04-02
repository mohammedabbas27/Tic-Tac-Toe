#Tic Tac Toe
import sys,os,time
from random import *
array=[]
array1=[]
array2=[1,3,7,9]
clear=lambda:os.system("cls")
board={'1':'','2':'','3':'','4':'','5':'','6':'',
        '7':'','8':'','9':''}
cont={3:'Computer',4:'Player',1:'Player 1',2:'Player 2'}
print('\t\t\t          TIC TAC TOE\n')
cpos={1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

#Table Structure
def draw():
    print('\n')
    print('\t\t\t\t     ----- ')
    print('\t\t\t\t    |%s|%s|%s|'%(str(board['1']),str(board['2']),str(board['3'])))
    print('\t\t\t\t    |-----|')
    print('\t\t\t\t    |%s|%s|%s|'%(str(board['4']),str(board['5']),str(board['6'])))
    print('\t\t\t\t    |-----|')
    print('\t\t\t\t    |%s|%s|%s|'%(str(board['7']),str(board['8']),str(board['9'])))
    print('\t\t\t\t     ----- ')

#Assigning Empty Spaces in the Tic Tac TOE Table
def sample():
    global f
    f=1
    for i in board:
        board[i]=i
def empty():
    global f
    f=1
    for i in board:
        board[i]=' '

#######++++++++----++++++xxxxxxxxxxxxxxxxxxxx+++++-----++++################
#Setting the positiong of the Chosen Value i.e X OR O
def setposition(pos,choiceu):
    if board[pos]==' ':
        board[pos]=choiceu
        global count
        count=count+1
        clear()
        draw()
        check(uchoice1,cchoice1)
        dra()
        return 0
    return 1

#######++++++++----++++++xxxxxxxxxxxxxxxxxxxx+++++-----++++################
#asking For the Position
def ask(sect,uchoice):
        flag=1;
        while flag==1:
            print(str(cont[sect]))
            print('Enter Your choice of Position')
            position1=str(input())
            flag=setposition(position1,uchoice)
            if flag==0:
                return
            print('Invalid Choice,Retry!')


def dra():
#    if board['1']
    #j=0
    #for i in range(1,9):
        #i=str(i)
        #if board[i]!=' ':
            #j=j+1
    #print(str(j))
    #j=str(j)
    if count==9:
        print('Its a Draw\n')
        sys.exit()
    return
#######++++++++----++++++xxxxxxxxxxxxxxxxxxxx+++++-----++++################
#Checking for a WIN|LOSS|DRAW
def check(uchoice,cchoice):
    if board['1']==board['2']==board['3']==uchoice:
        print('%s Wins'%(uchoice))
        time.sleep(2)
        sys.exit()
    elif board['1']==board['2']==board['3']==cchoice:
        print('%s Wins'%(cchoice))
        time.sleep(2)
        sys.exit()
    if board['1']==board['5']==board['9']==uchoice:
        print('%s Wins'%(uchoice))
        time.sleep(2)
        sys.exit()
    elif board['1']==board['5']==board['9']==cchoice:
        print('%s Wins'%(cchoice))
        time.sleep(2)
        sys.exit()
    if board['1']==board['4']==board['7']==uchoice:
        print('%s Wins'%(uchoice))
        time.sleep(2)
        sys.exit()
    elif board['1']==board['4']==board['7']==cchoice:
        print('%s Wins'%(cchoice))
        time.sleep(2)
        sys.exit()
    if board['2']==board['5']==board['8']==uchoice:
        print('%s Wins'%(uchoice))
        time.sleep(2)
        sys.exit()
    elif board['2']==board['5']==board['8']==cchoice:
        print('%s Wins'%(cchoice))
        time.sleep(2)
        sys.exit()
    if board['3']==board['5']==board['7']==uchoice:
        print('%s Wins'%(uchoice))
        time.sleep(2)
        sys.exit()
    elif board['3']==board['5']==board['7']==cchoice:
        print('%s Wins'%(cchoice))
        time.sleep(2)
        sys.exit()
    if board['3']==board['6']==board['9']==uchoice:
        print('%s Wins'%(uchoice))
        time.sleep(2)
        sys.exit()
    elif board['3']==board['6']==board['9']==cchoice:
        print('%s Wins'%(cchoice))
        time.sleep(2)
        sys.exit()
    if board['4']==board['5']==board['6']==uchoice:
        print('%s Wins'%(uchoice))
        time.sleep(2)
        sys.exit()
    elif board['4']==board['5']==board['6']==cchoice:
        print('%s Wins'%(cchoice))
        time.sleep(2)
        sys.exit()
    if board['7']==board['8']==board['9']==uchoice:
        print('%s Wins'%(uchoice))
        time.sleep(2)
        sys.exit()
    elif board['7']==board['8']==board['9']==cchoice:
        print('%s Wins'%(cchoice))
        time.sleep(2)
        sys.exit()
    return 0
def offence(uchoic11,chi1):
    global z,rdz
    rdz='1'
    for i in board:
        if board[i]==uchoic11:
            if int(i) not in array1:
                array1.append(int(i))
    l=str(len(array1))
    array1.sort()
    if l=='2':
        x=array1[0]*100
        y=array1[1]*10
        z=x+y
        z=str(int(z/10))
        print(str(z))
        brain(select2,cchoice1,chi1)
        return

    if l=='3':
        w=array1[0]*1000
        x=array1[1]*100
        y=array1[2]*10
        z=w+x+y
        z=str(int(z/10))
        print(str(z))
        brain(select2,cchoice1,chi1)
        return
def defence(uchoic11):
    global z,rdz
    rdz='0'
    for i in board:
        if board[i]==uchoic11:
            if int(i) not in array:
                array.append(int(i))
    l=str(len(array))
    array.sort()
    if l=='2':
        x=array[0]*100
        y=array[1]*10
        z=x+y
        z=str(int(z/10))
        print(str(z))
        return
    if l=='3':
        w=array[0]*1000
        x=array[1]*100
        y=array[2]*10
        z=w+x+y
        z=str(int(z/10))
        print(str(z))
        return

#######++++++++----++++++xxxxxxxxxxxxxxxxxxxx+++++-----++++################
#Deciding Who gets to Play First.....Still Needs Optimization

def decide(ais):
    global select1,select2,uchoice1,cchoice1
    #print('In Order for the selection to be fair, \ni.e which of the two Players\
    #gets to make a move first,\nthe selection is done rXandomly')
    print('Executing the random selection protocol.....')
    time.sleep(3)
    if ais==0:
        select1=randint(1,2)
    #select1=str(select1)
        if select1==1:
            select2=2
        else:
            select2=1
    if ais==1:
        select1=randint(3,4)
        #select1=4
        if select1==3:
            select2=4
        elif select1==4:
            select2=3
        if select1==4:
            print('Player Wins the Selection Protocol....\n')
        if select1==3:
            print('Computer Wins the Selection Protocol....\n')
            time.sleep(2)
            print('Thinking Whether to Take X or O\n')
            time.sleep(3)
            uch1=str(randint(1,2))
            if uch1=='1':
                cchoice1='X'
                uchoice1='O'
            else:
                cchoice1='O'
                uchoice1='X'
            return
    if ais==1:
        print('Player')
    else:
        print('Player '+str(select1))
    print("Do You wanna be 'X' or 'O'")
    uchoice1=str(input())
    if uchoice1=='X':
        cchoice1='O'
    else:
        cchoice1='X'
#######++++++++----++++++xxxxxxxxxxxxxxxxxxxx+++++-----++++################
#Concept of Multiplayer
def human():
    ais=0
    decide(ais)
    print('Player '+str(select1)+': you are '+uchoice1)
    print('Player '+str(select2)+': you are '+cchoice1)
    while check(uchoice1,cchoice1)==0:
        ask(select1,uchoice1)
        ask(select2,cchoice1)
def brain(selec1,cchoic1,chi1):
    #Easy Mode
    if chi1=='1':
        fag=1
        while fag==1:
            fp=randint(1,9)
            fp=cpos[fp]
            fag=setposition(fp,cchoic1)
            if fag==0:
                return
            print('Invalid Choice,Retrying!')
    #Hard Mode
    if chi1=='2':
        print('control reaching')
        j=1
        for i in range(1,9):
            i=str(i)
            if board[i]==' ':
                j=j+1
        if j>=8:
            fag=1
            while fag==1:
                #fp=randint(1,9)
                fp=choice(array2)
                fp=cpos[fp]
                fag=setposition(fp,cchoic1)
                if fag==0:
                    clear()
                    draw()
                    return
        if z=='12':
            if board['3']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=3:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('3',cchoic1)
                    return
        if z=='13':
            if board['2']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=3:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('2',cchoic1)
                    return
        if z=='14':
            if board['7']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=4:
                                    if fp!=7:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('7',cchoic1)
                    return
        if z=='15':
            if board['9']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=5:
                                    if fp!=9:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('9',cchoic1)
                    return
        if z=='17':
            if board['4']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=4:
                                    if fp!=7:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('4',cchoic1)
                    return
        if z=='124':
            if board['3']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=3:
                                        if fp!=4:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('3',cchoic1)
                    return
            elif board['7']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=2:
                                     if fp!=4:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('7',cchoic1)
                     return
        if z=='125':
            if board['3']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=3:
                                        if fp!=5:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('3',cchoic1)
                    return
            elif board['8']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=2:
                                     if fp!=5:
                                         if fp!=8:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('8',cchoic1)
                     return
            elif board['9']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=2:
                                     if fp!=5:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('8',cchoic1)
                     return
        if z=='127':
            if board['3']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=3:
                                        if fp!=7:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('3',cchoic1)
                    return
            elif board['4']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=2:
                                     if fp!=4:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('4',cchoic1)
                     return
        if z=='129':
            if board['3']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=3:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('3',cchoic1)
                    return
            elif board['5']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=2:
                                     if fp!=5:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('5',cchoic1)
                     return
        if z=='134':
            if board['2']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=3:
                                        if fp!=4:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('2',cchoic1)
                    return
            elif board['7']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=3:
                                     if fp!=4:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('7',cchoic1)
                     return
        if z=='135':
            if board['2']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=3:
                                        if fp!=5:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('2',cchoic1)
                    return
            elif board['7']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=3:
                                     if fp!=5:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('7',cchoic1)
                     return
            elif board['9']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=3:
                                     if fp!=5:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('9',cchoic1)
                     return
        if z=='137':
            if board['2']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=3:
                                        if fp!=7:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('2',cchoic1)
                    return
            elif board['4']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=3:
                                     if fp!=4:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('4',cchoic1)
                     return
            elif board['5']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=3:
                                     if fp!=5:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('5',cchoic1)
                     return
        if z=='139':
            if board['2']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=3:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('2',cchoic1)
                    return
            elif board['5']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=3:
                                     if fp!=5:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('5',cchoic1)
                     return
            elif board['6']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=3:
                                     if fp!=6:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('6',cchoic1)
                     return
        if z=='145':
            if board['6']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=4:
                                    if fp!=5:
                                        if fp!=6:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('6',cchoic1)
                    return
            elif board['7']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=4:
                                     if fp!=5:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('7',cchoic1)
                     return
            elif board['9']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=4:
                                     if fp!=5:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('9',cchoic1)
                     return
        if z=='149':
            if board['5']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=4:
                                    if fp!=5:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('5',cchoic1)
                    return
            elif board['7']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=4:
                                     if fp!=7:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('7',cchoic1)
                     return
        if z=='157':
            if board['2']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=5:
                                        if fp!=7:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('2',cchoic1)
                    return
            elif board['4']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=4:
                                     if fp!=5:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('4',cchoic1)
                     return
            elif board['9']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=7:
                                     if fp!=5:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('9',cchoic1)
                     return
        if z=='179':
            if board['4']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=4:
                                    if fp!=7:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('4',cchoic1)
                    return
            elif board['5']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=9:
                                     if fp!=5:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('5',cchoic1)
                     return
            elif board['8']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=7:
                                     if fp!=8:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('8',cchoic1)
                     return
        if z=='189':
            if board['5']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=5:
                                    if fp!=8:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('5',cchoic1)
                    return
            elif board['7']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=7:
                                     if fp!=8:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('7',cchoic1)
                     return
        if z=='23':
            if board['1']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=3:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('1',cchoic1)
                    return
        if z=='25':
            if board['8']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=2:
                                if fp!=5:
                                    if fp!=8:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('8',cchoic1)
                    return
        if z=='28':
            if board['5']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=2:
                                if fp!=5:
                                    if fp!=8:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('5',cchoic1)
                    return
        if z=='235':
            if board['1']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=3:
                                        if fp!=5:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('1',cchoic1)
                    return
            elif board['7']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=2:
                                 if fp!=3:
                                     if fp!=5:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('7',cchoic1)
                     return
            elif board['8']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=2:
                                 if fp!=3:
                                     if fp!=5:
                                         if fp!=8:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('8',cchoic1)
                     return
        if z=='238':
            if board['1']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=3:
                                        if fp!=8:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('1',cchoic1)
                    return
            elif board['5']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=2:
                                 if fp!=3:
                                     if fp!=5:
                                         if fp!=8:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('5',cchoic1)
                     return
        if z=='35':
            if board['7']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=5:
                                    if fp!=7:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('7',cchoic1)
                    return
        if z=='36':
            if board['9']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=6:
                                    if fp!=9:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('9',cchoic1)
                    return
        if z=='37':
            if board['5']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=5:
                                    if fp!=7:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('5',cchoic1)
                    return
        if z=='349':
            if board['6']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=6:
                                    if fp!=9:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('6',cchoic1)
                    return
        if z=='346':
            if board['5']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=4:
                                    if fp!=5:
                                        if fp!=6:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('5',cchoic1)
                    return
            elif board['9']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=3:
                                 if fp!=4:
                                     if fp!=6:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('9',cchoic1)
                     return
        if z=='146':
            if board['5']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=4:
                                    if fp!=5:
                                        if fp!=6:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('5',cchoic1)
                    return
            elif board['7']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=4:
                                     if fp!=6:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('7',cchoic1)
                     return
        if z=='39':
            if board['6']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=6:
                                    if fp!=9:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('6',cchoic1)
                    return
        if z=='356':
            if board['4']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=4:
                                    if fp!=5:
                                        if fp!=6:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('4',cchoic1)
                    return
            elif board['7']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=3:
                                 if fp!=5:
                                     if fp!=6:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('7',cchoic1)
                     return
            elif board['9']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=3:
                                 if fp!=5:
                                     if fp!=6:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('9',cchoic1)
                     return
        if z=='359':
            if board['1']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=3:
                                    if fp!=5:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('1',cchoic1)
                    return
            elif board['6']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=3:
                                 if fp!=5:
                                     if fp!=6:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('6',cchoic1)
                     return
            elif board['7']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=3:
                                 if fp!=5:
                                     if fp!=7:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('7',cchoic1)
                     return
        if z=='367':
            if board['5']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=5:
                                    if fp!=6:
                                        if fp!=7:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('5',cchoic1)
                    return
            elif board['9']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=3:
                                 if fp!=6:
                                     if fp!=7:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('9',cchoic1)
                     return
        if z=='379':
            if board['5']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=5:
                                    if fp!=7:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('5',cchoic1)
                    return
            elif board['6']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=3:
                                 if fp!=6:
                                     if fp!=7:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('6',cchoic1)
                     return
            elif board['8']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=3:
                                 if fp!=7:
                                     if fp!=8:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('8',cchoic1)
                     return
        if z=='178':
            if board['4']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=4:
                                    if fp!=7:
                                        if fp!=8:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('4',cchoic1)
                    return
            elif board['9']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=7:
                                     if fp!=8:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('9',cchoic1)
                     return
        if z=='378':
            if board['5']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=5:
                                    if fp!=7:
                                        if fp!=8:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('5',cchoic1)
                    return
            elif board['9']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=3:
                                 if fp!=7:
                                     if fp!=8:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('9',cchoic1)
                     return
        if z=='167':
            if board['5']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=5:
                                    if fp!=9:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('5',cchoic1)
                    return
        if z=='158':
            if board['2']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=2:
                                    if fp!=5:
                                        if fp!=8:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('2',cchoic1)
                    return
            elif board['9']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=1:
                                 if fp!=5:
                                     if fp!=8:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('9',cchoic1)
                     return
        if z=='358':
            if board['2']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=2:
                                if fp!=3:
                                    if fp!=5:
                                        if fp!=8:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('2',cchoic1)
                    return
            elif board['7']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=3:
                                 if fp!=5:
                                     if fp!=7:
                                         if fp!=8:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('7',cchoic1)
                     return
        if z=='45':
            if board['6']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=4:
                                if fp!=5:
                                    if fp!=6:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('6',cchoic1)
                    return
        if z=='46':
            if board['5']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=4:
                                if fp!=5:
                                    if fp!=6:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('5',cchoic1)
                    return
        if z=='47':
            if board['1']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=4:
                                    if fp!=7:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('1',cchoic1)
                    return
        if z=='457':
            if board['1']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=4:
                                    if fp!=5:
                                        if fp!=7:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('1',cchoic1)
                    return
            elif board['3']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=3:
                                 if fp!=4:
                                     if fp!=5:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('3',cchoic1)
                     return
            elif board['6']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=4:
                                 if fp!=5:
                                     if fp!=6:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('6',cchoic1)
                     return
        if z=='458':
            if board['2']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=2:
                                if fp!=4:
                                    if fp!=5:
                                        if fp!=8:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('2',cchoic1)
                    return
            elif board['6']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=4:
                                 if fp!=5:
                                     if fp!=6:
                                         if fp!=8:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('6',cchoic1)
                     return
        if z=='467':
            if board['1']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=4:
                                    if fp!=6:
                                        if fp!=7:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('1',cchoic1)
                    return
            elif board['5']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=4:
                                 if fp!=5:
                                     if fp!=6:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('5',cchoic1)
                     return
        if z=='469':
            if board['3']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=4:
                                    if fp!=6:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('3',cchoic1)
                    return
            elif board['5']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=4:
                                 if fp!=5:
                                     if fp!=6:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('5',cchoic1)
                     return
        if z=='479':
            if board['1']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=4:
                                    if fp!=7:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('1',cchoic1)
                    return
            elif board['8']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=4:
                                 if fp!=7:
                                     if fp!=8:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('8',cchoic1)
                     return
        if z=='56':
            if board['4']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=4:
                                if fp!=5:
                                    if fp!=6:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('4',cchoic1)
                    return
        if z=='57':
            if board['3']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=5:
                                    if fp!=7:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('3',cchoic1)
                    return
        if z=='58':
            if board['2']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=2:
                                if fp!=5:
                                    if fp!=8:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('2',cchoic1)
                    return
        if z=='59':
            if board['1']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=5:
                                    if fp!=9:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('1',cchoic1)
                    return
        if z=='567':
            if board['3']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=5:
                                    if fp!=6:
                                        if fp!=7:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('3',cchoic1)
                    return
            elif board['4']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=4:
                                 if fp!=5:
                                     if fp!=6:
                                         if fp!=7:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('4',cchoic1)
                     return
        if z=='568':
            if board['2']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=2:
                                if fp!=5:
                                    if fp!=6:
                                        if fp!=8:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('2',cchoic1)
                    return
            elif board['4']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=4:
                                 if fp!=5:
                                     if fp!=6:
                                         if fp!=8:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('4',cchoic1)
                     return
        if z=='569':
            if board['1']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=5:
                                    if fp!=6:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('1',cchoic1)
                    return
            elif board['3']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=3:
                                 if fp!=5:
                                     if fp!=6:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('3',cchoic1)
                     return
            elif board['4']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=4:
                                 if fp!=5:
                                     if fp!=6:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('4',cchoic1)
                     return
        if z=='578':
            if board['1']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=5:
                                    if fp!=7:
                                        if fp!=8:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('1',cchoic1)
                    return
            elif board['9']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=5:
                                 if fp!=7:
                                     if fp!=8:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('9',cchoic1)
                     return
        if z=='579':
            if board['1']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=5:
                                    if fp!=7:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('1',cchoic1)
                    return
            elif board['8']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=5:
                                 if fp!=7:
                                     if fp!=8:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('8',cchoic1)
                     return
        if z=='589':
            if board['1']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=5:
                                    if fp!=8:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('1',cchoic1)
                    return
            elif board['2']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=2:
                                 if fp!=5:
                                     if fp!=8:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('2',cchoic1)
                     return
            elif board['7']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=5:
                                 if fp!=7:
                                     if fp!=8:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('7',cchoic1)
                     return
        if z=='69':
            if board['3']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=6:
                                    if fp!=9:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('3',cchoic1)
                    return
        if z=='679':
            if board['3']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=6:
                                    if fp!=7:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('3',cchoic1)
                    return
            elif board['8']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=6:
                                 if fp!=7:
                                     if fp!=8:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('8',cchoic1)
                     return
        if z=='689':
            if board['3']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=3:
                                if fp!=6:
                                    if fp!=8:
                                        if fp!=9:
                                            if board[fp]==' ':
                                                break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('3',cchoic1)
                    return
            elif board['7']==' ':
                 rd=randint(1,18)
                 rd=rd%2
                 rd=randint(1,18)
                 rd=rd%2
                 if rd>=10:
                     fag=1
                     while fag==1:
                         while 1:
                             fp=randint(1,9)
                             fp=cpos[fp]
                             if fp!=6:
                                 if fp!=7:
                                     if fp!=8:
                                         if fp!=9:
                                             if board[fp]==' ':
                                                 break
                         fag=setposition(fp,cchoic1)
                         if fag==0:
                             return
                 else:
                     setposition('7',cchoic1)
                     return
        if z=='78':
            if board['9']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=7:
                                if fp!=8:
                                    if fp!=9:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('9',cchoic1)
                    return
        if z=='79':
            if board['8']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=7:
                                if fp!=8:
                                    if fp!=9:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('8',cchoic1)
                    return
        if z=='89':
            if board['7']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=7:
                                if fp!=8:
                                    if fp!=9:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('7',cchoic1)
                    return
        if z=='19':
            if board['5']==' ':
                rd=randint(1,18)
                rd=rd%2
                rd=randint(1,18)
                rd=rd%2
                if rd>=10:
                    fag=1
                    while fag==1:
                        while 1:
                            fp=randint(1,9)
                            fp=cpos[fp]
                            if fp!=1:
                                if fp!=5:
                                    if fp!=9:
                                        if board[fp]==' ':
                                            break
                        fag=setposition(fp,cchoic1)
                        if fag==0:
                            return
                else:
                    setposition('5',cchoic1)
                    return
        print('rdz1')
        if rdz=='0':
            print('rdz')
            fag=1
            while fag==1:
                fp=randint(1,9)
                fp=cpos[fp]
                fag=setposition(fp,cchoic1)
                if fag==0:
                    return
#######++++++++----++++++xxxxxxxxxxxxxxxxxxxx+++++-----++++################
#Concept of Aritificial Intelligence
def ai(chi):
    ais=1
    decide(ais)
    print('Player Your Choice is '+uchoice1)
    print('Computer\'s Choice is '+cchoice1)
    while check(uchoice1,cchoice1)==0:
        if select1==4:
            ask(select1,uchoice1)
            print('Thinking.......')
            time.sleep(2)
            offence(cchoice1,chi)
            defence(uchoice1)
            brain(select2,cchoice1,chi)
        elif select1==3:
            print('Thinking.......')
            time.sleep(2)
            offence(cchoice1,chi)
            defence(uchoice1)
            brain(select1,cchoice1,chi)
            #ask(select1,cchoice1)
            ask(select2,uchoice1)
    sys.exit()

#######++++++++----++++++xxxxxxxxxxxxxxxxxxxx+++++-----++++################
#Main Engineering
sample()
draw()
empty()
select1=select2=uchoice1=cchoice1=f=z=count=0
rdz=' '
print('Mode of Play :\n1.Single Player\n2.Multiplayer\n\n')
print('Enter your Selection\n')
sel=str(input())
if sel=='2':
    human()
elif sel=='1':
    print('There are Two Modes\n')
    print('1.Easy\n2.Hard')
    print('Enter Your Choice\n')
    ch=str(input())
    if ch=='1':
        ai(ch)
    else:
        ai(ch)
        print('Invalid Selection\n')
        print('Terminating......')
        time.sleep(2)
        sys.exit()
