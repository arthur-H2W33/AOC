# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:31:54 2022

@author: apot
"""

path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"
from collections import defaultdict
from copy import deepcopy


IPTraw=open(path+'inputd14.txt').read().split("\n")
test=open(path+'inputd14ex.txt').read().split("\n")
IPT=IPTraw

listepaths=[ligne.split(' -> ') for ligne in IPT]
listcoord=[]
for ligne in listepaths:
    listcoord.append([])
    for comb in ligne:
        real=int(comb.split(',')[0])
        imag=int(comb.split(',')[1])
        listcoord[-1].append(complex(real,imag))


dicrocks=defaultdict(list)
for chemin in listcoord:
    for indice in range(len(chemin)-1):
        diff=chemin[indice+1]-chemin[indice]
        if diff.imag==0:
            for index in range(int(abs(diff.real)+1)):
                dicrocks[complex(chemin[indice].real+index*diff.real/abs(diff.real),chemin[indice].imag)]=True
        elif diff.real==0:
            for index in range(int(abs(diff.imag)+1)):
                dicrocks[complex(chemin[indice].real,chemin[indice].imag+index*diff.imag/abs(diff.imag))]=True
dicQ2=deepcopy(dicrocks)

def sanddrop(limite):
    position=complex(500,0)
    while position.imag<limite:
        if dicrocks[complex(position.real,position.imag+1)]!=True:
            position+=complex(0,1)
        elif dicrocks[complex(position.real-1,position.imag+1)]!=True:
            position+=complex(-1,1)
        elif dicrocks[complex(position.real+1,position.imag+1)]!=True:
            position+=complex(1,1)
        else:
            dicrocks[position]=True
            return position.imag
    return position.imag

def sanddrop2(floor):
    position=complex(500,0)
    while position.imag<(floor-1):
        if dicQ2[complex(position.real,position.imag+1)]!=True:
            position+=complex(0,1)
        elif dicQ2[complex(position.real-1,position.imag+1)]!=True:
            position+=complex(-1,1)
        elif dicQ2[complex(position.real+1,position.imag+1)]!=True:
            position+=complex(1,1)
        else:
            dicQ2[position]=True
            return position
    dicQ2[position]=True
    return position

sandcompt=-1
freefall=int(max(elt.imag for elt in dicrocks.keys()))

lastgrain=0
while lastgrain<freefall:
    sandcompt+=1
    lastgrain=sanddrop(freefall)
    
    
print('Q1', sandcompt)

floor=freefall+2

compt2=0
lastgrain=0
while lastgrain!=complex(500,0):
    compt2+=1
    lastgrain=sanddrop2(floor)
    
print('Q2', compt2)
