# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:31:54 2022

@author: apot
"""

path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"


A_IPTraw=open(path+'D13.txt').read().split("\n")
A_test=open(path+'D13ex.txt').read().split("\n")
IPT=A_IPTraw
IPT=[eval(elt) for elt in IPT if len(elt)!=0]
listegauche=[]
listedroite=[]



def compint(intG,intD,indicepair):
    if intG<intD:
        dicplacement[indicepair]=True
    elif intG>intD:
        dicplacement[indicepair]=False
    return

def complist(listG,listD,indicepair):
    lenG=len(listG)
    lenD=len(listD)
    if lenD==lenG==0:
        return
    else:
        comptaille(listG,listD,indicepair)
    if dicplacement[indicepair]==None:    
        for indiceliste in range(min(len(listG),len(listD))):    
            if dicplacement[indicepair]==None:     #je circule sur les items tant que l'on a pas convergé
                typeG=type(listG[indiceliste])
                typeD=type(listD[indiceliste])
                if typeG==typeD==int:
                    compint(listG[indiceliste],listD[indiceliste],indicepair)
                elif typeG==typeD==list:       
                    complist(listG[indiceliste],listD[indiceliste],indicepair)
                elif typeG==list:
                    complist(listG[indiceliste],[listD[indiceliste]],indicepair)
                elif typeD==list:
                    complist([listG[indiceliste]],listD[indiceliste],indicepair)
        if dicplacement[indicepair]==None:
            if lenG==lenD:
                return
            elif lenG>lenD:
                dicplacement[indicepair]=False
            else:
                dicplacement[indicepair]=True
    return

def comptaille(eltG,eltD,indicepair):
    lenG=len(eltG)
    lenD=len(eltD)
    if lenG==0:
        dicplacement[indicepair]=True
    elif lenD==0:
        dicplacement[indicepair]=False

def calculdic(IPT):
    listegauche=[]
    listedroite=[]
    for index in range(len(IPT)):
        if index%2==0: 
            listegauche.append(IPT[index])
        elif index%2==1:
            listedroite.append(IPT[index])
    #je dois donc comparer listedroite vs listegauche
    
    listedroite=[elt for elt in listedroite]
    listedroite.insert(0,[])
    listegauche=[elt for elt in listegauche]
    listegauche.insert(0,[])
    for pair in range(1,len(listegauche)):
        for indicecomp in range(min(len(listegauche[pair]),len(listedroite[pair]))):
            if dicplacement[pair]==None:
                eltG=listegauche[pair][indicecomp]
                eltD=listedroite[pair][indicecomp]
                typeG=type(eltG)
                typeD=type(eltD)
                if typeD==typeG==int:
                    compint(eltG,eltD,pair)   
                elif typeD==typeG==list:
                    complist(eltG,eltD,pair)
                elif typeG==list:
                    complist(eltG,[eltD],pair)
                elif typeD==list:
                    complist([eltG],eltD,pair)
        if dicplacement[pair]==None:
            if len(listegauche[pair])>len(listedroite[pair]):
                dicplacement[pair]=False
            else:
                dicplacement[pair]=True

     


def comparelignes(liste1,liste2,pair=0):
    for indicecomp in range(min(len(liste1),len(liste2))):
            if dicplacement[pair]==None:
                eltG=liste1[indicecomp]
                eltD=liste2[indicecomp]
                typeG=type(eltG)
                typeD=type(eltD)
                if typeD==typeG==int:
                    compint(eltG,eltD,pair)   
                elif typeD==typeG==list:
                    complist(eltG,eltD,pair)
                elif typeG==list:
                    complist(eltG,[eltD],pair)
                elif typeD==list:
                    complist([eltG],eltD,pair)
    if dicplacement[pair]==None:
        if len(liste1)>len(liste2):
            dicplacement[pair]=False
        else:
            dicplacement[pair]=True    





dicplacement={key:None for key in range(int(len(IPT)/2)+1) if key!=0}
#je sauvegarderai mes résultats dans le dictionnaire with True si bien placé or False sinon

calculdic(IPT)
res1=[elt for elt in dicplacement.keys() if dicplacement[elt]==True]
print('Q1', sum(res1),'--',res1)

IPT.append([[2]])
IPT.append([[6]])
dicplacement={key:None for key in range(int(len(IPT))+1) if key!=0}



for indice in range(200):
    for sousindice in range(len(IPT)-1):
        dicplacement[0]=None
        comparelignes(IPT[sousindice],IPT[sousindice+1])
        if dicplacement[0]==False:
            IPT[sousindice],IPT[sousindice+1]=IPT[sousindice+1],IPT[sousindice]

res2=[IPT.index([[2]]),IPT.index([[6]])]
print('Q2',(res2[0]+1)*(res2[1]+1),res2)
#27348 is too low
