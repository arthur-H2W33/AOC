# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:54:57 2022

@author: apot
"""

path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"

IPTraw=open(path+'inputd4.txt').read().split("\n")
test=open(path+'inputd4ex.txt').read().split("\n")
IPT=IPTraw

IPT=[elt.split(',') for elt in IPT]
IPT=[elt.split('-')for pair in IPT for elt in pair]
IPT=[int(elt) for pair in IPT for elt in pair]

drawA=[]
drawB=[]

score1=0

for indice in range(int(len(IPT)/4)):
    if (IPT[4*indice]<=IPT[4*indice+2] and IPT[4*indice+1]>=IPT[4*indice+3]) or (IPT[4*indice]>=IPT[4*indice+2] and IPT[4*indice+1]<=IPT[4*indice+3]):
        score1+=1
        
print("Q1", score1)

score2=0
for indice in range(int(len(IPT)/4)):
    if (IPT[4*indice]>IPT[4*indice+3] or IPT[4*indice+1]<IPT[4*indice+2]):
        score2+=1

score2=len(IPTraw)-score2

print("Q2", score2)