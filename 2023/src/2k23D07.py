# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:45:37 2023

@author: apot
"""

path='C:\\Users\\apot\\Desktop\\AdventOfCode\\2023\\inputs\\'
#from collections import defaultdict
#from copy import deepcopy
from timeit import default_timer as timer

IPT=open(path+'D07.txt').read().split('\n')


def print_time(t_start, t_end):
    s = t_end-t_start
    print(int(s*1000), "ms = ", int(s), "s = ", int(s/60), "min")


t_start = timer()

testIPT=('''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483''')


#IPT=testIPT.split('\n')

dichands={}
#DICHANDS[TOUT]=[CARTES, scoring, occurences, RKG occurence, listeforcomparing]

for _ in range(len(IPT)):
    dichands[_]=[IPT[_].split(' ')[0],int(IPT[_].split(' ')[1]),'OCC','OCC RANK','COMPLIST',0]

def analyzehand(tour):
    hand=dichands[tour][0]
    occurences=[]
    for carte in hand:
        occurences.append(hand.count(carte))        
    dichands[tour][2]=occurences
    return



def getoccurenceranking(tour):
    occ=dichands[tour][2]
    rkg=0
    if 5 in occ:
        rkg=6
    elif 4 in occ:
        rkg=5
    elif 3 in occ and 2 in occ:
        rkg=4
    elif 3 in occ:
        rkg=3
    elif occ.count(2)==4 or occ.count(2)==4:
        rkg=2
    elif 2 in occ:
        rkg=1
    dichands[tour][3]=rkg
    return rkg

transrule1=dict(zip('2 3 4 5 6 7 8 9 T J Q K A'.split(' '),['2','3','4','5','6','7','8','9','A','B','C','D','E']))

def translatehandtocompare(tour):
    hand=dichands[tour][0]
    translation=''
    for carte in hand:
        translation+=transrule1[carte]        
    dichands[tour][4]=int(translation,16)
    return


for tour in range(len(IPT)):
    analyzehand(tour)
    translatehandtocompare(tour)
    getoccurenceranking(tour)

orderhands=[]
for cat in range(7):
    orderhands.append([[elt,val[4]] for elt,val in dichands.items() if val[3]==cat])


for cat in orderhands:
    if len(cat)>0:
        cat.sort(key = lambda x: x[1])

score1=0
compteur=1
for cat in orderhands:
    if len(cat)>0:
        for hand in cat:
            score1+=dichands[hand[0]][1]*compteur
            compteur+=1
        

print('Q1', score1)

t_end=timer()
print_time(t_start, t_end)


######### GO FOR PART 2 #########

t_start = timer()


#DICHANDS[TOUT]=[CARTES 0, scoring 1, occurences 2, RKG occurence 3, listeforcomparing 4]



def analyzehand2(tour):
    hand=dichands[tour][0]
    occurences=[]
    nbrjok=0
    for carte in hand:
        if carte!='J':
            occurences.append(hand.count(carte))   
        else:
            nbrjok+=1
    if nbrjok==5:
        dichands[tour][2]=[5,5,5,5,5]
        return
    maxhand=max(occurences)
    count=1
    newocc=[]
    for item in occurences:
        if count<=maxhand:
            if item==maxhand:
                count+=1
                newocc.append(item+nbrjok)
            else:
                newocc.append(item)
        else:
            newocc.append(item)
            
    dichands[tour][2]=newocc
    return


transrule2=dict(zip('2 3 4 5 6 7 8 9 T J Q K A'.split(' '),['2','3','4','5','6','7','8','9','A','1','C','D','E']))

def translatehandtocompare(tour):
    hand=dichands[tour][0]
    translation=''
    for carte in hand:
        translation+=transrule2[carte]        
    dichands[tour][4]=int(translation,16)
    return


for tour in range(len(IPT)):
    analyzehand2(tour)
    translatehandtocompare(tour)
    getoccurenceranking(tour)

orderhands=[]
for cat in range(7):
    orderhands.append([[elt,val[4]] for elt,val in dichands.items() if val[3]==cat])


for cat in orderhands:
    if len(cat)>0:
        cat.sort(key = lambda x: x[1])

score2=0
compteur=1
for cat in orderhands:
    if len(cat)>0:
        for hand in cat:
            score2+=dichands[hand[0]][1]*compteur
            compteur+=1
        

print('Q2', score2)

t_end=timer()
print_time(t_start, t_end)


#251515496 IS THE ANSWER