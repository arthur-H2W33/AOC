import re
#from copy import deepcopy
from timeit import default_timer as timer

IPT=open(path+'D02.txt').read().split('\n')


def print_time(t_start, t_end):
    s = t_end-t_start
    print(int(s*1000), "ms = ", int(s), "s = ", int(s/60), "min")


t_start = timer()



def testgame(game):
    for pierres in game[1]:
        if pierres.split(' ')[-1]=='green':
            if int(pierres.split(' ')[0])>13:
                return 0
        elif pierres.split(' ')[-1]=='blue':
            if int(pierres.split(' ')[0])>14:
                return 0  
        elif pierres.split(' ')[-1]=='red':
            if int(pierres.split(' ')[0])>12:
                return 0
    return game[0]

listeGAME=[]
for ligne in IPT:
    listeGAME.append([int(ligne.split(':')[0].split(' ')[1]),re.split('; |, ',ligne.split(':')[1].strip())])

score1=0
for jeux in listeGAME:
    score1+=testgame(jeux)
   


print('Q1', score1)

t_end=timer()
print_time(t_start, t_end)


######### GO FOR PART 2 #########

t_start = timer()

def minimumdices(game):
    listeRGB=[0,0,0]
    for pierres in game[1]:
        if pierres.split(' ')[-1]=='green':
            listeRGB[1]=max(listeRGB[1],int(pierres.split(' ')[0]))
        elif pierres.split(' ')[-1]=='blue':
            listeRGB[2]=max(listeRGB[2],int(pierres.split(' ')[0]))
        elif pierres.split(' ')[-1]=='red':
            listeRGB[0]=max(listeRGB[0],int(pierres.split(' ')[0]))
    return listeRGB[0]*listeRGB[1]*listeRGB[2]

score2=0
for jeux in listeGAME:
    score2+=minimumdices(jeux)

print('Q2', score2)
