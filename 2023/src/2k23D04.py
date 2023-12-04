# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:45:37 2023

@author: apot
"""

path='C:\\Users\\apot\\Desktop\\AdventOfCode\\2023\\inputs\\'
#from collections import defaultdict
#from copy import deepcopy
from timeit import default_timer as timer

IPT=open(path+'D04.txt').read().split('\n')


def print_time(t_start, t_end):
    s = t_end-t_start
    print(int(s*1000), "ms = ", int(s), "s = ", int(s/60), "min")


t_start = timer()

testIPT=('''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11''')

#IPT=testIPT.split('\n')

diccartes={}
for idx in range(len(IPT)):
    diccartes[idx]=[[elt for elt in IPT[idx].split(':')[1].strip().split('|')[0].split(' ') if elt.isdigit()],[elt for elt in IPT[idx].split(':')[1].strip().split('|')[1].split(' ') if elt.isdigit()]]


def pointscartes(board):
    score=0.5
    init=False
    for tirage in board[0]:
        if tirage in board[1]:
            init=True
            score*=2
    if init==False:
        return 0
    else:
        return score


score1=0
for idx in range(len(IPT)):
    score1+= pointscartes(diccartes[idx])
print('Q1', int(score1))

t_end=timer()
print_time(t_start, t_end)

######### GO FOR PART 2 #########

t_start = timer()


def pointscartes2(board):
    score=0
    for tirage in board[0]:
        if tirage in board[1]:
            score+=1
    return score

diccomptecartes={elt:1 for elt in range(len(IPT))}

for carte in range(len(IPT)):
    nbrwon=pointscartes2(diccartes[carte])
    for idx in range(nbrwon):
        diccomptecartes[carte+idx+1]+=diccomptecartes[carte]

score2=0
for value in diccomptecartes.values():
    score2+=value
    
print('Q2', score2)

t_end=timer()
print_time(t_start, t_end)