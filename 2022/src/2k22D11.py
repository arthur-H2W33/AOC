# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:30:39 2022

@author: apot
"""

path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"

IPTraw=open(path+'D11.txt').read().split("\n")
test=open(path+'D11ex.txt').read().split("\n")
IPT=IPTraw


dicitemsmonkeys={}
dicmonkeyinspectioncount={}
monkey=[]
for lignes in IPT:
    if lignes.startswith("Monkey"):
        monkey.append(int(lignes.split(" ")[1][0]))
    elif lignes.startswith('  Starting items'):
        dicitemsmonkeys[monkey[-1]]=[int(elt[-2:]) for elt in lignes.split(',')]
        dicmonkeyinspectioncount[monkey[-1]]=0

def monkeybusiness(monkey):
    value=0
    if monkey==0:
        for item in dicitemsmonkeys[monkey]:
            value=item*11
            value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%2==0:
                dicitemsmonkeys[7].append(value%9699690)
            else:
                dicitemsmonkeys[1].append(value%9699690)
        dicitemsmonkeys[monkey]=[]
    elif monkey==1:
        for item in dicitemsmonkeys[monkey]:
            value=item+1
            value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%17==0:
                dicitemsmonkeys[3].append(value%9699690)
            else:
                dicitemsmonkeys[2].append(value%9699690)
        dicitemsmonkeys[monkey]=[]
    elif monkey==2:
        for item in dicitemsmonkeys[monkey]:
            value=item+7
            value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%7==0:
                dicitemsmonkeys[6].append(value%9699690)
            else:
                dicitemsmonkeys[5].append(value%9699690)
        dicitemsmonkeys[monkey]=[]
    elif monkey==3:
        for item in dicitemsmonkeys[monkey]:
            value=item+3
            value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%11==0:
                dicitemsmonkeys[2].append(value%9699690)
            else:
                dicitemsmonkeys[6].append(value%9699690)   
        dicitemsmonkeys[monkey]=[]                
    elif monkey==4:
        for item in dicitemsmonkeys[monkey]:
            value=item*item
            value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%19==0:
                dicitemsmonkeys[7].append(value%9699690)
            else:
                dicitemsmonkeys[0].append(value%9699690) 
        dicitemsmonkeys[monkey]=[]                
    elif monkey==5:
        for item in dicitemsmonkeys[monkey]:
            value=item+4
            value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%5==0:
                dicitemsmonkeys[4].append(value%9699690)
            else:
                dicitemsmonkeys[0].append(value%9699690) 
        dicitemsmonkeys[monkey]=[]
    elif monkey==6:
        for item in dicitemsmonkeys[monkey]:
            value=item*5
            value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%13==0:
                dicitemsmonkeys[4].append(value%9699690)
            else:
                dicitemsmonkeys[5].append(value%9699690)
        dicitemsmonkeys[monkey]=[]
    elif monkey==7:
        for item in dicitemsmonkeys[monkey]:
            value=item+8
            value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%3==0:
                dicitemsmonkeys[1].append(value%9699690)
            else:
                dicitemsmonkeys[3].append(value%9699690)
        dicitemsmonkeys[monkey]=[]

def monkeybusiness2(monkey):
    
    value=0
    if monkey==0:
        for item in dicitemsmonkeys[monkey]:
            value=item*11
            #value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%2==0:
                dicitemsmonkeys[7].append(value%9699690)
            else:
                dicitemsmonkeys[1].append(value%9699690)
        dicitemsmonkeys[monkey]=[]
    elif monkey==1:
        for item in dicitemsmonkeys[monkey]:
            value=item+1
            #value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%17==0:
                dicitemsmonkeys[3].append(value%9699690)
            else:
                dicitemsmonkeys[2].append(value%9699690)
        dicitemsmonkeys[monkey]=[]
    elif monkey==2:
        for item in dicitemsmonkeys[monkey]:
            value=item+7
            #value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%7==0:
                dicitemsmonkeys[6].append(value%9699690)
            else:
                dicitemsmonkeys[5].append(value%9699690)
        dicitemsmonkeys[monkey]=[]
    elif monkey==3:
        for item in dicitemsmonkeys[monkey]:
            value=item+3
            #value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%11==0:
                dicitemsmonkeys[2].append(value%9699690)
            else:
                dicitemsmonkeys[6].append(value%9699690)   
        dicitemsmonkeys[monkey]=[]                
    elif monkey==4:
        for item in dicitemsmonkeys[monkey]:
            value=item*item
            #value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%19==0:
                dicitemsmonkeys[7].append(value%9699690)
            else:
                dicitemsmonkeys[0].append(value%9699690) 
        dicitemsmonkeys[monkey]=[]                
    elif monkey==5:
        for item in dicitemsmonkeys[monkey]:
            value=item+4
            #value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%5==0:
                dicitemsmonkeys[4].append(value%9699690)
            else:
                dicitemsmonkeys[0].append(value%9699690) 
        dicitemsmonkeys[monkey]=[]
    elif monkey==6:
        for item in dicitemsmonkeys[monkey]:
            value=item*5
            #value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%13==0:
                dicitemsmonkeys[4].append(value%9699690)
            else:
                dicitemsmonkeys[5].append(value%9699690)
        dicitemsmonkeys[monkey]=[]
    elif monkey==7:
        for item in dicitemsmonkeys[monkey]:
            value=item+8
            #value=int(value/3)
            dicmonkeyinspectioncount[monkey]+=1
            if value%3==0:
                dicitemsmonkeys[1].append(value%9699690)
            else:
                dicitemsmonkeys[3].append(value%9699690)
        dicitemsmonkeys[monkey]=[]
        
for ronde in range(20):
    for singe in monkey:
        monkeybusiness(singe)
nbrinspections=[elt for elt in dicmonkeyinspectioncount.values()]
nbrinspections.sort()
print('Q1', nbrinspections[-1]*nbrinspections[-2])


# inti dict for part 2
dicitemsmonkeys={}
dicmonkeyinspectioncount={}
monkey=[]
for lignes in IPT:
    if lignes.startswith("Monkey"):
        monkey.append(int(lignes.split(" ")[1][0]))
    elif lignes.startswith('  Starting items'):
        dicitemsmonkeys[monkey[-1]]=[int(elt[-2:]) for elt in lignes.split(',')]
        dicmonkeyinspectioncount[monkey[-1]]=0



for ronde in range(10000):
    for singe in monkey:
        monkeybusiness2(singe)
nbrinspections=[]
nbrinspections=[elt for elt in dicmonkeyinspectioncount.values()]
nbrinspections.sort()
print('Q2', nbrinspections[-1]*nbrinspections[-2])
