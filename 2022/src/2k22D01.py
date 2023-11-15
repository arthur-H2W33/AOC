path="C:\\Users\\apot\\Desktop\\AdventOfCode\\2022\\inputs\\"

IPTraw=open(path+'D01.txt').read().split("\n")
IPT=IPTraw


compile=[]
compte=0
for elt in IPT:
    if elt!='':
            compte+=int(elt)
    else:
        compile.append(compte)
        compte=0

compile.sort()

print("Q1", compile[-1])        

print("Q2", compile[-1]+compile[-2]+compile[-3])        
