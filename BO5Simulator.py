import random
import copy

classTable={1:'WARRIOR',
            2:'SHAMAN',
            3:'DRUID',
            4:'HUNTER',
            5:'WARLOCK',
            6:'ROGUE',
            7:'MAGE',
            8:'PALADIN',
            9:'PRIEST'}

ifile=open('input','r')

iterations=int(ifile.readline())

print('Number of iterations:%d'%iterations)

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

def printClass(l):
    for e in l:
        print("%s"%classTable[e],end=" ")
    print()

def printResult(c1,c2,m):
    print('        ',end=' ')
    for e in c1:
        print('%8s'%classTable[e],end=' ')
    print()
    tmp=0
    for e in c2:
        print('%8s'%classTable[e],end=' ')
        for i in range(4):
            print('%8.3f'%m[tmp][i],end=' ')
        tmp+=1
        print()
    print()

winrateData=[]
        
for i in range(9):
    tmplist=[float(x) for x in ifile.readline().split()]
    winrateData.append(tmplist)

'''
print("Input win rate:")
printTable(winrateData)
'''

yourClass=[int(x) for x in ifile.readline().split()]
print('Your class : ',end=' ')
printClass(yourClass)

enemyClass=[int(x) for x in ifile.readline().split()]
print('Enemy class: ',end=' ')
printClass(enemyClass)

winrate=[]

for i in yourClass:
    tmplist=[winrateData[i-1][j-1] for j in enemyClass]
    winrate.append(tmplist)
'''
print()
printTable(winrate)
'''
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

printResult(yourClass,enemyClass,table)
