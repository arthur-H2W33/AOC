# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:45:37 2023

@author: apot
"""

path='C:\\Users\\apot\\Desktop\\AdventOfCode\\2023\\inputs\\'
#from collections import defaultdict
#from copy import deepcopy
import re
from timeit import default_timer as timer

IPT=open(path+'D03.txt').read().split('\n')


def print_time(t_start, t_end):
    s = t_end-t_start
    print(int(s*1000), "ms = ", int(s), "s = ", int(s/60), "min")


t_start = timer()

testIPT=('''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..''')

#IPT=testIPT.split('\n')

board={}
for idxreal in range(len(IPT)):
    for idximag in range(len(IPT[idxreal])):
        if IPT[idxreal][idximag]!='.':
            board[complex(idxreal,idximag)]=IPT[idxreal][idximag]
            
posspeciaux=[elt for elt in board.keys() if board[elt].isdigit()==False]

posnombres=[elt for elt in board.keys() if board[elt].isdigit()==True]
posnombres=sorted(posnombres, key=lambda x: (x.real, x.imag))    


def nombreactif(clef):
    for elt in dicnombres[clef]:
        voisins=[elt+complex(0,1), elt+complex(0,-1), elt+complex(1,0),elt+complex(-1,0),elt+complex(-1,1), elt+complex(1,-1), elt+complex(1,1),elt+complex(-1,-1)]  
        for vois in voisins:
            if vois in posspeciaux:
                return int(clef[2])
    return 0

def getnumbers(noligne):
    listepos=[]
    listechiffre=[]
    chiffre=''
    init=True
    for idxcol in range(len(IPT[noligne])):
        if complex(noligne,idxcol) in posnombres:
            listepos.append(complex(noligne,idxcol))
            chiffre+=board[complex(noligne,idxcol)]
            init=False
        else:
            if init==False:
                listechiffre.append(int(chiffre))
                init=True
            chiffre=''
    if init==False:
        listechiffre.append(int(chiffre))
    return listepos,listechiffre

dicnombres={}

def assignnumbers(ligne,listepos,listenbr):
    listepos=sorted(listepos, key=lambda x: (x.real, x.imag))    
    compteur=0
    compteurchiffre=0
    for chiffre in listenbr:
        compteurchiffre+=1
        dicnombres[ligne,compteurchiffre,chiffre]=[]
        for _ in range(len(str(chiffre))):
            dicnombres[ligne,compteurchiffre,chiffre].append(listepos[compteur])
            compteur+=1   
            
for idxligne in range(len(IPT)):
    listepos,listenbr=getnumbers(idxligne)
    assignnumbers(idxligne,listepos,listenbr)
    
score1=0    
for nombre in dicnombres.keys():
    score1+=nombreactif(nombre)
    

print('Q1', score1)



t_end=timer()
print_time(t_start, t_end)


# 13683752 is too high
# 527009 not good either
# 529673 same here

#SCORE IS 530495

######### GO FOR PART 2 #########

t_start = timer()

def isgears(elt):
    voisins=[elt+complex(0,1), elt+complex(0,-1), elt+complex(1,0),elt+complex(-1,0),elt+complex(-1,1), elt+complex(1,-1), elt+complex(1,1),elt+complex(-1,-1)]  
    nbvoisins=set()
    score=1
    for vois in voisins:
        if vois in posnombres:
            for clef,val in dicnombres.items():
                if vois in val:
                    nbvoisins.add(clef)
    if len(nbvoisins)==2:
        for item in nbvoisins:
            score*=item[2]
        return score
    else:
        return 0
                    
potgears=[elt for elt in board.keys() if board[elt]=='*']

score2=0
for gear in potgears:
    score2+=isgears(gear)

print('Q2', score2)

t_end=timer()
print_time(t_start, t_end)