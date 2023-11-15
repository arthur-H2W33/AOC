# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:28:32 2022

@author: apot
"""

path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"

IPTraw=open(path+'D09.txt').read().split("\n")
test=open(path+'D09ex.txt').read().split("\n")
IPT=IPTraw

commandes=[elt.split(" ") for elt in IPT]

def mouvement(pos_head,pos_tail):
    diff=pos_head-pos_tail
    if diff==complex(0,0):
        return pos_tail
    elif diff.real==0:
        return pos_tail+complex(0,diff.imag-(diff.imag/abs(diff.imag)))
    elif diff.imag==0:
        return pos_tail+complex(diff.real-(diff.real/abs(diff.real)),0)
    elif max(abs(diff.real),abs(diff.imag))>1:
        return pos_tail+complex(diff.real/abs(diff.real),diff.imag/abs(diff.imag))
    else:
        return pos_tail

    
   
    
pos_head=complex(0,0)
pos_tail=complex(0,0)
positions_prises=[complex(0,0)]
    
for elt in commandes:
    if elt[0]=='R':
        for decalage in range (int(elt[1])):
            pos_head+=complex(1,0)
            pos_tail=mouvement(pos_head,pos_tail)
            positions_prises.append(pos_tail)
    elif elt[0]=='L':
        for decalage in range (int(elt[1])):
            pos_head-=complex(1,0)
            pos_tail=mouvement(pos_head,pos_tail)
            positions_prises.append(pos_tail)
    elif elt[0]=='U':
        for decalage in range (int(elt[1])):
            pos_head+=complex(0,1)
            pos_tail=mouvement(pos_head,pos_tail)            
            positions_prises.append(pos_tail)
    elif elt[0]=='D':
        for decalage in range (int(elt[1])):
            pos_head-=complex(0,1)
            pos_tail=mouvement(pos_head,pos_tail)
            positions_prises.append(pos_tail)

                          
print("Q1", len(set(positions_prises)))


    
    
positionsc_prises=[[complex(0,0)]]
positionsc_prises[0]=positions_prises
    
for corde in range(9):
   pos_head=complex(0,0)
   pos_tail=complex(0,0)
   positionsc_prises.append([complex(0,0)])
   for elt in positionsc_prises[corde]:
       pos_head=elt
       pos_tail=mouvement(pos_head,pos_tail)
       positionsc_prises[corde+1].append(pos_tail)
       
       
print("Q2", len(set(positionsc_prises[8])))
