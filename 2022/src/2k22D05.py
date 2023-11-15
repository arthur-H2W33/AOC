# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:55:19 2022

@author: apot
"""

path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"
from textwrap import wrap

IPTraw=open(path+'D5.txt').read().split("\n")
test=open(path+'D5ex.txt').read().split("\n")
IPT=IPTraw

IPT=[elt for elt in IPT]

demarcation=IPT.index('')

initial=[elt for elt in IPT[:demarcation-1]]
initialf=[]
for indice in range(1,(int(len(initial[0]))),4):
    initialf.append([elt[indice:indice+1] for elt in initial if elt!=' '])


def create_board():    
    board1={}
    for i in range(len(initialf[0])+1):
        board1[i+1]=[elt for elt in initialf[i] if elt!=' ']
    return board1

        
consignes=[elt.split(' ') for elt in IPT[demarcation+1:]]




board=create_board()


listeIN=[]
for elt in consignes:
    listeIN.append([int(elt[1]),int(elt[3]),int(elt[5])])

for consigne in listeIN:
    for occurence in range(consigne[0]):    
        board[consigne[2]].insert(0,board[consigne[1]][0])
        board[consigne[1]].pop(0)

res1=''
for elt in board.keys():
    res1+=board[elt][0]
print("Q1",res1)


board=create_board()

for consigne in listeIN:
    for occurence in range(consigne[0]):    
        board[consigne[2]].insert(0,board[consigne[1]][consigne[0]-occurence-1])
        board[consigne[1]].pop(consigne[0]-occurence-1)


    

res2=''
for elt in board.keys():
    res2+=board[elt][0]
print("Q2",res2)
