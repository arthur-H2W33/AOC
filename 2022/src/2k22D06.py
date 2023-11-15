# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:28:29 2022

@author: apot
"""

path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"

IPTraw=open(path+'D6.txt').read().split("\n")
test=open(path+'D6ex.txt').read().split("\n")
IPT=IPTraw[0]


index1=0
for indice in range(4,len(IPT)):
    if len(set(IPT[indice-4:indice]))==4:
       index1=indice
       break
      
for indice in range(14,len(IPT)):
    if len(set(IPT[indice-14:indice]))==14:
       index2=indice
       break


print("Q1", index1)
print("Q2", index2)
