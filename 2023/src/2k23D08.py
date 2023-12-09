# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:45:37 2023

@author: apot
"""

path='C:\\Users\\apot\\Desktop\\AdventOfCode\\2023\\inputs\\'
#from collections import defaultdict
from copy import deepcopy
from timeit import default_timer as timer
import math

IPT=open(path+'D08.txt').read().split('\n')


def print_time(t_start, t_end):
    s = t_end-t_start
    print(int(s*1000), "ms = ", int(s), "s = ", int(s/60), "min")


t_start = timer()

testIPT=('''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)''')


#IPT=testIPT.split('\n')


instru=[elt for elt in IPT[0]]
graph={ligne[:3] : [ligne[7:10],ligne[12:15]] for ligne in IPT[2:]}

score1=0
def partone(start):
    pos=start
    score1=0
    while True:
        nextside=instru[score1%len(instru)]
        score1+=1
        if nextside=='L':
            pos=graph[pos][0]
        else:
            pos=graph[pos][1]
        if pos[-1]=='Z':
            return score1

print('Q1', partone('AAA'))

t_end=timer()
print_time(t_start, t_end)


######### GO FOR PART 2 #########

t_start = timer()

startingpoints=[elt for elt in graph.keys() if elt[-1]=='A']

        
def teststep(listestep):
    if len(listestep)<3:
        return [False,0]
    else:
        pas=listestep[-1]-listestep[1]
        if listestep[0]+pas==listestep[-2]:
            return [True,pas]
        else:
            return[False,0]

def getloop(start):
    pos=start
    nbr=0
    steps=[]
    while True:
        nextside=instru[nbr%len(instru)]
        nbr+=1
        if nextside=='L':
            pos=graph[pos][0]
        else:
            pos=graph[pos][1]
        if pos[-1]=='Z':
            steps.append(nbr)            
        if teststep(steps)[0]:
            return teststep(steps)[1]


cyclength=[]
for point in startingpoints:
    cyclength.append(getloop(point))



def ppcmpair(x, y):
    return x * y // math.gcd(x, y)

def ppcmliste(liste):
    currentppcm = liste[0]
    for idx in range(1,len(liste)):
        currentppcm = ppcmpair(currentppcm, liste[idx])
    return currentppcm

score2=ppcmliste(cyclength)

print('Q2',score2)
t_end=timer()
print_time(t_start, t_end)