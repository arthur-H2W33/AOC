# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:31:53 2022

@author: apot
"""

from timeit import default_timer as timer
path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"

IPTraw=open(path+'D15.txt').read().split("\n")
test=open(path+'D15ex.txt').read().split("\n")
IPT=IPTraw
if IPT==test:
    objectif=complex(0,10)
    limite=20
else:
    objectif=complex(0,2000000)   
    limite=4000000

def print_time(t_start, t_end):
    s = t_end-t_start
    print(int(s*1000), "ms = ", int(s), "s = ", int(s/60), "min")


t_start = timer()

IPT=[elt.split(' ') for elt in IPT]
sensors=[]
beacons=[]
for ligne in IPT:
    sensors.append(complex(int(ligne[2].split(',')[0][2:]),int(ligne[3].split(':')[0][2:])))
    beacons.append(complex(int(ligne[8].split(',')[0][2:]),int(ligne[9].split(':')[0][2:])))

couples=[] #couples(sensors position, manhattan difference)
for indice in range(len(sensors)):
    couples.append([sensors[indice],int(abs((sensors[indice]-beacons[indice]).real)+abs((sensors[indice]-beacons[indice]).imag))])

'''
intersection=[] #all couples that are in the objective range
for couple in couples:
    if abs(int(couple[0].imag)-int(objectif.imag))<=couple[2]:
        intersection.append(couple)


dicligneobjectif={}    #dictionnaire des positions sur la ligne objectif
for couple in intersection:
    for possible in range(couple[1]+1): #je parcours la ligne sur la longueur maximum d'intersection
        possible1=complex(couple[0].real+possible,objectif.imag)    #à droite
        possible2=complex(couple[0].real-possible,objectif.imag)    #et à gauche
        if (abs(possible1.real-couple[0].real)+abs(possible1.imag-couple[0].imag))<=(couple[1]):
            dicligneobjectif[possible1]='X'
            dicligneobjectif[possible2]='X'
ans1=[elt for elt in dicligneobjectif.keys() if elt not in beacons]   #je parcours la ligne objectif
sourcesonline=[elt for elt in sensors if elt.imag==objectif.imag]   #je vérifie que les positionsne contienent pas de sensors
ans1+=sourcesonline  
print('Q1',len(set(ans1)))
t_end = timer()
print_time(t_start, t_end)
#ans1 49119281
'''
print('ON DEMARRE')

def drawline(couple):
    positions=set()
    for diff in range(couple[1]+1):
        positions.add(complex(couple[0].real-diff,couple[0].imag+couple[1]-diff))
        positions.add(complex(couple[0].real-diff,couple[0].imag-(couple[1])+diff))
        positions.add(complex(couple[0].real+diff,couple[0].imag+couple[1]-diff))
        positions.add(complex(couple[0].real+diff,couple[0].imag-(couple[1]-diff)))
    return {element for element in positions if element.real>0 and element.real<=limite and element.imag>0 and element.imag<=limite}                
    
listetotale=set()
for couple in couples:
    listetotale=listetotale.union(drawline(couple))
    

print('LISTE DES BORDS CREE, DE TAILLE ', len(listetotale))


mightbewining=set()
for coord in listetotale:
    if (coord+complex(2,0)) in listetotale:
        if (coord+complex(1,0)) not in listetotale:
            if ((coord+complex(1,1)) in listetotale) and ((coord+complex(1,-1)) in listetotale):
                mightbewining.add(coord+complex(1,0))

print('COMB POT DETERMINED, SIZED ', len(mightbewining))

filtered=complex(0,0)
for elt in mightbewining:
    for couple in couples:
        if int(abs((elt-couple[0]).real)+abs((elt-couple[0]).imag))<=couple[1]:
            break
    else:
        filtered=elt
        
print(filtered)
 
print('Q2', int(filtered.real*limite+filtered.imag))   
t_end=timer()
print_time(t_start, t_end)
