# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:28:30 2022

@author: apot
"""

path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"

IPTraw=open(path+'D8.txt').read().split("\n")
test=open(path+'D8ex.txt').read().split("\n")
IPT=IPTraw

#reponse for test is 16 + 5 = 21
# reponse for test2 is 8
def frontiere(position):
    maxhaut=int(board[complex(0,position.imag)])
    maxbas=int(board[complex(len(IPT)-1,position.imag)])
    maxd=int(board[complex(position.real,len(IPT[0])-1)])
    maxg=int(board[complex(position.real,0)])
    for lignehaut in range(1,int(position.real)):
        maxhaut=max(maxhaut,int(board[complex(lignehaut,int(position.imag))]))
    for lignebas in range(len(IPT)-int(position.real)-1):
        maxbas=max(maxbas,int(board[complex(len(IPT)-lignebas-1,int(position.imag))]))
    for colg in range(1,int(position.imag)):
        maxg=max(maxg,int(board[complex(int(position.real),colg)]))
    for cold in range(len(IPT[0])-int(position.imag)-1):
        maxd=max(maxd,int(board[complex(int(position.real),len(IPT[0])-1-cold)]))   
    return min(maxbas,maxhaut,maxg,maxd)



def degagement(position):
    v_haut=0
    v_bas=0
    v_d=0
    v_g=0
    for deg_haut in range(int(position.real)):
        v_haut+=1
        if int(board[complex(int(position.real)-deg_haut-1,int(position.imag))])>=int(board[position]):
            break
    for v_g in range(int(position.imag)):
        v_g+=1
        if int(board[complex(int(position.real),int(position.imag)-v_g)])>=int(board[position]):
            break
    for deg_bas in range(len(IPT)-int(position.real)-1):
        v_bas+=1
        if int(board[complex(int(position.real)+deg_bas+1,int(position.imag))])>=int(board[position]):
            break
    for v_d in range(len(IPT[0])-int(position.imag)-1):
        v_d+=1
        if int(board[complex(int(position.real),int(position.imag)+v_d)])>=int(board[position]):
            break
    return (v_haut*v_bas*v_d*v_g)


board={}
for ligne in range(len(IPT)):
    for colonne in range(len(IPT[0])):
        board[complex(ligne,colonne)]=int(IPT[ligne][colonne])
'''
for ligne in range(len(IPT)):
    for colonne in range(len(IPT[0])):
        frontiere(complex(ligne,colonne))


board_visible={}
for ligne in range(len(IPT)):
    for colonne in range(len(IPT[0])):
        board_visible[complex(ligne,colonne)]=frontiere(complex(ligne,colonne))
for col_l_ext in range(len(IPT[0])):
    board_visible[complex(0,col_l_ext)]=-1
    board_visible[complex(len(IPT)-1,col_l_ext)]=-1
for l_col_ext in range (len(IPT)):
    board_visible[complex(l_col_ext,0)]=-1
    board_visible[complex(l_col_ext,len(IPT[0])-1)]=-1


arbres_visibles=[]
for elt in board.keys():
    if board[elt]>board_visible[elt]:
        arbres_visibles.append(elt)
print ("Q1", len(set(arbres_visibles)))'''

print(max([degagement(elt) for elt in board.keys()]))
