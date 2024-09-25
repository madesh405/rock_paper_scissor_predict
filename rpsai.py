from random import choice

weapons=["rock","paper","scissor"]

def computer_choice(hist:dict,weapons:list[str]) -> str:

    all=[]

    if hist=={}:
        return choice(weapons)

    else:
        for x in hist:
            if hist[x]==hist[len(hist)]:
                if x-1!=0:
                    all.append(hist[x-1])

        rt=all.count(weapons[0])
        pt=all.count(weapons[1])
        st=all.count(weapons[2])
        rp=rt/len(hist)
        pp=pt/len(hist)
        sp=st/len(hist)
        pdict={rp:"rock",pp:"paper",sp:"scissor"} #have to change this part error in rare cases
        m=max(pdict)
        ind=weapons.index(pdict[m])
        if ind==2:
            return weapons[0]
        else:
            return weapons[ind+1]

def player_choice(weapons:list) -> str:       #the players's choice
    print("\n\nwelcome to rock paper scissor game")
    print("pick 1 for Rock")
    print("pick 2 por Paper")
    print("pick 3 for Scissor")
    intprps=int(input("enter you choice 1, 2 or 3 : "))
    prps=weapons[intprps-1]
    return prps

'''             ***Rules of the game***

1.Rock beats scissor
2.Scissor beats paper
3.Paper beats rock

'''

def rules(crps:str,prps:str,weapons:list) -> int:
    if crps==prps:
        return [0,0]    #(computers point, players point)

    if crps==weapons[0]:
        if prps==weapons[1]:
            return [0,1]
        elif prps==weapons[2]:
            return [1,0]

    elif crps==weapons[1]:
        if prps==weapons[0]:
            return [1,0]
        elif prps==weapons[2]:
            return [0,1]

    elif crps==weapons[2]:
        if prps==weapons[0]:
            return [0,1]
        elif prps==weapons[1]:
             return [1,0]


#__main__
hist={}
score=[0,0]
game=True
t=1
while game:
    crps=computer_choice(hist,weapons)
    prps=player_choice(weapons)
    hist[t]=prps
    print("cmputer:",crps,"player:",prps,"\n\n")
    curscore=rules(crps,prps,weapons)
    score=[curscore[0]+score[0],curscore[1]+score[1]]
    cont=input("wanna continue? (y,n) ")
    if cont=="n":
        t+=1
        break

print("the scores are computer",score[0],"player",score[1])

