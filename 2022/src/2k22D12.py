# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:31:13 2022

@author: apot
"""

path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"

IPTraw=open(path+'inputd12.txt').read().split("\n")
test=open(path+'inputd12ex.txt').read().split("\n")
IPT=IPTraw

board={}
no_lignes=-1
for lignes in IPT:
    no_lignes+=1
    no_char=-1
    for char in lignes:
        no_char+=1
        board[complex(no_lignes,no_char)]=char
        if char=='S':
            position0=complex(no_lignes,no_char)
        elif char=='E':
            positionf=complex(no_lignes,no_char)
                 
board_value={}
for position in board.keys():
    if board[position]=="S":
        board_value[position]=1
    elif board[position]=="E":
        board_value[position]=26
    else:    
        board_value[position]=(ord(board[position])-96)
        
for lignes in [-1,len(IPT)]:
    for col in range(-1,len(IPT[0])+1):
        board_value[complex(lignes,col)]=999
    

for col in [-1,len(IPT[0])]:
    for lignes in range(-1,len(IPT)+1):
        board_value[complex(lignes,col)]=999        


def voisins(position):
    admissible=[]
    real=position.real
    imag=position.imag
    for voisin in [complex(real+1,imag),complex(real-1,imag),complex(real,imag+1),complex(real,imag-1)]:
        if board_value[voisin]-board_value[position]<2:
            admissible.append(voisin)
    return admissible


dic_accessibles={}
for position in board.keys():
    dic_accessibles[position]=voisins(position)
    

# find bfs traversal from starting vertex
def bfs(noeud):
    visitedSet = set()
    queue =[]
    nouvellequeue=[]
    nouvellequeue.append(noeud)
    visitedSet.add(noeud)
    nbr_ronde=0
    while nouvellequeue:
        queue=nouvellequeue
        nouvellequeue=[]
        nbr_ronde+=1
        for elt in queue:
            for voisin in voisins(elt):
                if voisin==positionf:
                    return nbr_ronde
                elif voisin not in visitedSet:
                        visitedSet.add(voisin)
                        nouvellequeue.append(voisin)
        

parcours=bfs(position0)

print('Q1', parcours)

departpotentiels=[elt for elt in board.keys() if board_value[elt]==1]
dicrando={}
for depart in departpotentiels:
    dicrando[depart]=bfs(depart)


final=[elt for elt in dicrando.values() if elt!=None]
final.sort()
print('Q2', final[0])    
