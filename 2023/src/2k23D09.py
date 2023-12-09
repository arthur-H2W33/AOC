# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:45:37 2023

@author: apot
"""

path='C:\\Users\\apot\\Desktop\\AdventOfCode\\2023\\inputs\\'
#from collections import defaultdict
#from copy import deepcopy
from timeit import default_timer as timer

IPT=open(path+'D09.txt').read().split('\n')


def print_time(t_start, t_end):
    s = t_end-t_start
    print(int(s*1000), "ms = ", int(s), "s = ", int(s/60), "min")


t_start = timer()

testIPT=('''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45''')

#IPT=testIPT.split('\n')


seq=[]
for ligne in IPT:
    seq.append([int(elt) for elt in ligne.split(' ')])

size=len(seq[0])


def getnext(suite):
    diff=getdiff(suite)
    hierlast=[diff[-1]]
    while True:
        diff=getdiff(diff)
        hierlast.append(diff[-1])
        if hierlast[-1]==0:
            res=suite[-1]
            for c in hierlast:
                res+=c
            return res

def getdiff(suite):
    res=[]
    for idx in range(len(suite)-1):
        res.append(suite[idx+1]-suite[idx])
    return res
    
score1=0
for suite in seq:
    score1+=getnext(suite)

print('Q1',score1)

t_end=timer()
print_time(t_start, t_end)


######### GO FOR PART 2 #########

t_start = timer()

def getnext2(suite):
    diff=getdiff(suite)
    hierlast=[diff[-1]]
    while True:
        diff=getdiff(diff)
        hierlast.append(diff[-1])
        if diff[0]==0:
            res=suite[-1]
            for c in hierlast:
                res+=c
            return res


seq2=[]
for item in seq:
    trans=item[::-1]
    seq2.append(trans)
    
score2=0
for suite in seq2:
    score2+=getnext2(suite)

print('Q2', score2)

#983 is too low
#3005 is too high

t_end=timer()
print_time(t_start, t_end)