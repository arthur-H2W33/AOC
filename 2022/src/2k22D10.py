# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:30:05 2022

@author: apot
"""

path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"

import matplotlib.pyplot as plot


IPTraw=open(path+'D10.txt').read().split("\n")
test=open(path+'D10ex.txt').read().split("\n")
test2='''noop
addx 3
addx -5'''.split('\n')
IPT=IPTraw

time=0
registerX=1
dico_X={}
dico_X[0]=0
for elt in IPT:
    if elt=='noop':
        time+=1
        dico_X[time]=registerX
    else:        
        time+=1
        dico_X[time]=registerX
        registerX+=int(elt.split(' ')[1])
        time+=1
        dico_X[time]=registerX

#during the 20th, 60th, 100th, 140th, 180th, and 220th cycles)
resQ1=0
for cycle in [20,60,100,140,180,220]:
    resQ1+=(dico_X[cycle-1]*cycle)
    #print(dico_X[cycle-1]*cycle,"-",cycle,resQ1)
    
print('Q1',resQ1)
#answ Q1 12880

pos_print=[]
sprite_pos=1
for cycle in range(1,241):
    #print("je commence le cyle",cycle)
    #print("sprite is in",dico_X[cycle-1])
    sprite_pos=dico_X[cycle-1]
    if cycle%40 in[sprite_pos,sprite_pos+1,sprite_pos+2]:
        #print("condition met for printing in at cycle", cycle)
        pos_print.append(cycle)

x=[]
y=[]
for elt in pos_print:
    y.append(-int((elt-elt%40)/40))
    x.append(elt%40)

plot.scatter(x,y)
plot.ylim(-20,0)
plot.show()

#answer Q2 is FCJAPJRE
