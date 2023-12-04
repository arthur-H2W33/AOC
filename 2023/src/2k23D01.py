IPT=open(path+'D01.txt').read().split('\n')


def print_time(t_start, t_end):
    s = t_end-t_start
    print(int(s*1000), "ms = ", int(s), "s = ", int(s/60), "min")


t_start = timer()

buildchar=[]
for ligne in IPT:
    buildchar.append('')
    for char in ligne:
        if char.isdigit():
            buildchar[-1]+=char
score1=0
for item in buildchar:
    score1+=int(item[0]+item[-1])

print('Q1', score1)

t_end=timer()
print_time(t_start, t_end)


######### GO FOR PART 2 #########

t_start = timer()

match={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

build2=[]
for idxligne in range(len(IPT)):
    build2.append([])
    for idxlettre in range(len(IPT[idxligne])):
        if IPT[idxligne][idxlettre].isdigit():
            build2[-1].append(IPT[idxligne][idxlettre])
        elif IPT[idxligne][idxlettre:idxlettre+3] in match.keys():
            build2[-1].append(IPT[idxligne][idxlettre:idxlettre+3])
        elif IPT[idxligne][idxlettre:idxlettre+4] in match.keys():
            build2[-1].append(IPT[idxligne][idxlettre:idxlettre+4])
        elif IPT[idxligne][idxlettre:idxlettre+5] in match.keys():
            build2[-1].append(IPT[idxligne][idxlettre:idxlettre+5])

score2=0
for item in build2:
    if len(item)>0:
        score2+=int(str(match[item[0]])+str(match[item[-1]]))
print('Q2', score2)

t_end=timer()
print_time(t_start, t_end)
