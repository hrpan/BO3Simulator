import random
import copy
winrate=[]

iterations=int(input("Number of iterations:"))

def delrow( m, i):
    del m[i]

def delcol( m, i):
    for list in m:
        del list[i]

def printTable(m):
    for row in m:
        for e in row:
            print("%.2f"%round(e,2),end=" ")
        print()
        
ifile=open('input','r')


for i in range(4):
    tmplist=[float(x) for x in ifile.readline().split()]
    winrate.append(tmplist)

print("Input win rate:")
printTable(winrate)

table=[]

for yourBan in range(4):
    tmplist=[]
    for enemyBan in range(4):
        winrate_banned=copy.deepcopy(winrate)
        delrow(winrate_banned,enemyBan)
        delcol(winrate_banned,yourBan)
        totWin=0
        for iteration in range(iterations):
            clone=copy.deepcopy(winrate_banned)
            endofgame=False
            nLose=0
            nWin=0            
            while not endofgame:
                yourPick=random.randint(0,len(clone)-1)
                enemyPick=random.randint(0,len(clone[yourPick])-1)
                youWin = random.random()<clone[yourPick][enemyPick]
                if youWin:
                    nWin+=1
                    delrow(clone,yourPick)
                else:
                    nLose+=1
                    delcol(clone,enemyPick)
                if nWin==3 or nLose==3:
                    endofgame=True
            if nWin==3:
                totWin+=1
        tmplist.append(totWin/iterations)
    table.append(tmplist)

print("Win rate table(col:enemy ban, row:your ban):")
printTable(table)
