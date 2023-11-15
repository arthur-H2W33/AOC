# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 08:39:44 2022

@author: apot
"""

path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"

IPTraw=open(path+'D2.txt').read().split("\n")
IPT=IPTraw


score1=0
score1+=IPT.count('A X')*4
score1+=IPT.count('A Y')*8
score1+=IPT.count('A Z')*3

score1+=IPT.count('B X')*1
score1+=IPT.count('B Y')*5
score1+=IPT.count('B Z')*9

score1+=IPT.count('C X')*7
score1+=IPT.count('C Y')*2
score1+=IPT.count('C Z')*6

print("Q1",score1)


score2=0
score2+=IPT.count('A Y')*4
score2+=IPT.count('B Y')*5
score2+=IPT.count('C Y')*6

score2+=IPT.count('A X')*3
score2+=IPT.count('B X')*1
score2+=IPT.count('C X')*2

score2+=IPT.count('A Z')*8
score2+=IPT.count('B Z')*9
score2+=IPT.count('C Z')*7

print("Q2",score2)
