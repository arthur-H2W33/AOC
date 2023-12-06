path='C:\\Users\\apot\\Desktop\\AdventOfCode\\2023\\inputs\\'
from timeit import default_timer as timer
import math

IPT=open(path+'D06.txt').read().split('\n')


def print_time(t_start, t_end):
    s = t_end-t_start
    print(int(s*1000), "ms = ", int(s), "s = ", int(s/60), "min")


t_start = timer()

testIPT=('''Time:      7  15   30
Distance:  9  40  200''')

#IPT=testIPT.split('\n')

reftime=[int(elt) for elt in IPT[0].split(':')[1].split(' ') if elt.isdigit()]
refdist=[int(elt) for elt in IPT[1].split(':')[1].split(' ') if elt.isdigit()]

def possiblemove(time,dist):
    possib=[]
    for scenario in range(1,time):
        if ((time-scenario)*scenario)>dist:
            possib.append(scenario)
    return max(len(possib),1)


score1=1

for course in range(len(reftime)):
    score1*=possiblemove(reftime[course],refdist[course])
    
print('Q1', score1)

t_end=timer()
print_time(t_start, t_end)

######### GO FOR PART 2 #########

t_start = timer()

refdist2=[elt for elt in IPT[1].split(' ') if elt.isdigit()]
reftime2=[elt for elt in IPT[0].split(' ') if elt.isdigit()]
dist2=''
time2=''
for item in refdist2:
    dist2+=item
dist2=int(dist2)
for item in reftime2:
    time2+=item
time2=int(time2)



def resoudreEquationSecondDegre(a,b,c):
   delta = b*b-4*a*c
   if delta > 0:
      racineDeDelta=math.sqrt(delta)
      retour = [(-b-racineDeDelta)/(2*a),(-b+racineDeDelta)/(2*a)]
   elif delta < 0:
      retour = []  #liste vide
   else:
      retour = [-b/(2*a)] #liste d'un seul élément
   return retour


racines=resoudreEquationSecondDegre(1,-time2,dist2)

score2=int(racines[1]-racines[0])

print('Q2', score2)
t_end=timer()
print_time(t_start, t_end)