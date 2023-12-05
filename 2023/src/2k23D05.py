# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:45:37 2023

@author: apot
"""

path='C:\\Users\\apot\\Desktop\\AdventOfCode\\2023\\inputs\\'
#from collections import defaultdict
#from copy import deepcopy
from timeit import default_timer as timer

IPT=open(path+'D05.txt').read().split('\n')


def print_time(t_start, t_end):
    s = t_end-t_start
    print(int(s*1000), "ms = ", int(s), "s = ", int(s/60), "min")


t_start = timer()

seeds=[int(elt) for elt in IPT[0].split(':')[1].split(' ') if elt.isdigit()]


compteur=0
convertisseur=dict()
for ligne in range(len(IPT)-1):
    if IPT[ligne+1]=='':
        compteur+=1
        newkey=compteur
        convertisseur[newkey]=[]
    elif IPT[ligne+1][-1]!=':': 
        dest=int(IPT[ligne+1].split(' ')[0])
        source=int(IPT[ligne+1].split(' ')[1])
        rge=int(IPT[ligne+1].split(' ')[2])
        convertisseur[newkey].append([source,source+rge-1,dest-source])

#formalisme du converstisseur :
#convertisseur[CLEF]=[liste des ranges such as : [Begin Range, En Range, Offset] ]    

def transferlevel(seed,clef):
    for rge in convertisseur[clef]:
        if seed>=rge[0] and seed<=rge[1]:
            return seed+rge[2]
    return seed

score1=[]
for seed in seeds:
    res=seed
    for i in list(convertisseur.keys()):
        res=transferlevel(res,i)
    score1.append(res)
print('Q1', min(score1))

t_end=timer()
print_time(t_start, t_end)


######### GO FOR PART 2 #########

t_start = timer()

def reverseconversion(convertedseed,clef):
    for rge in convertisseur[clef]:
        if (convertedseed-rge[2])>=rge[0] and  (convertedseed-rge[2])<=rge[1]:
            return convertedseed-rge[2]
    return convertedseed

def inputseed(final):
    res=final
    liste=list(convertisseur.keys())
    liste.reverse()
    for key in liste:
        res=reverseconversion(res,key)
    return res

startingseedspairs=[]
first=True
for chiffre in IPT[0].split(':')[1].split(' '):
    if chiffre.isdigit():
        if first:
            basrge=int(chiffre)
            first=False
        else:
            startingseedspairs.append(range(basrge,basrge+int(chiffre)))
            first=True

tested=0
bornehaute=0
while bornehaute==0 and tested<=min(score1):
    tested+=500000
    potwin=inputseed(tested)
    for pair in startingseedspairs:
        if potwin in pair:
            bornehaute=tested
            break

tested=bornehaute-500000
score2=0
while score2==0:
    tested+=1
    potwin=inputseed(tested)
    for pair in startingseedspairs:
        if potwin in pair:
            score2=tested
            break
    
print('Q2', score2)

t_end=timer()
print_time(t_start, t_end)