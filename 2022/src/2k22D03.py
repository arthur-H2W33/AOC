# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 09:19:05 2022

@author: apot
"""

path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"

IPTraw=open(path+'inputd3.txt').read().split("\n")
test=open(path+'inputd3ex.txt').read().split("\n")
IPT=IPTraw


size=0
Rug1=[]
Rug2=[]

for elt in IPT:
    size=int(len(elt)/2)
    Rug1.append(elt[:size])
    Rug2.append(elt[size:])
                 
scoring='0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

score1=0

for indice in range(len(IPT)):
    for indice2 in range(len(Rug1[indice])):
        if Rug2[indice].count(Rug1[indice][indice2])>0:
            score1+=scoring.rindex(Rug1[indice][indice2])
            break
            
print("Q1",score1)

#--

indicefin=int(len(IPT)/3)

score2=0
for indice in range(indicefin):
    for indice2 in range(len(IPT[indice*3])):
        if IPT[indice*3+1].count(IPT[indice*3][indice2])>0 and IPT[indice*3+2].count(IPT[indice*3][indice2])>0:
            score2+=scoring.rindex(IPT[indice*3][indice2])
            break
print("Q2",score2)
