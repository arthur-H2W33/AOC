# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:28:30 2022

@author: apot
"""

path = "C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"


IPTraw = open(path+'inputd7.txt').read().split("\n")
test = open(path+'inputd7ex.txt').read().split("\n")
IPT = IPTraw
            

liste_dir=[]
for ligne in IPT:
    if ligne[0:4]=='$ cd':
        liste_dir.append(ligne.split(" ")[2].strip())

liste_path=['']
ongoinglist=[]
for rep in liste_dir:
    tampon=''
    if rep=='..':
        ongoinglist.pop(-1)
    else:
        ongoinglist.append(rep)
        for element in ongoinglist:
            tampon+=element
        liste_path.append(tampon)
liste_path.pop(0)

tailles={}
compteurDir=-1
for elt in IPT:
    if elt[0:4]=='$ cd' and elt!='$ cd ..':
        compteurDir+=1
    if elt[0] in "0123456789":
        tailles[liste_path[compteurDir]+elt.split(" ")[1]]=int(elt.split(' ')[0])

tailles_dir={}        
for folder in liste_path:
    tailles_dir[folder]=sum(tailles[fichier] for fichier in tailles.keys() if fichier.startswith(folder))
        
print("Q1",sum([elt for elt in tailles_dir.values() if elt<=100000]))

needed_mem=30000000-(70000000-tailles_dir['/'])
print("Q2",min([tailles_dir[elt] for elt in tailles_dir.keys() if tailles_dir[elt]>needed_mem]))


