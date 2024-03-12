score=[]

choice=None

while choice !="0":
    
    print("high score keeper\n0-quit\n1-list scores\n2-add score")

    choice=input("choice ")

    if choice=="0":
        print("good bye")

    elif choice=="1":
        print("NAME\tSCORE")
        for entry in scores:
            score,name=entry
            print(name, "\t", score)

    elif choice=="2":

    name= input("what is the player's name? ")
    score=int(input("what score did you get"))
    entry=(score,name)
    scores.append(entry)
    scores.sort()
    scores.reverse()     #want the highest number first
    scores=scores[:5]    #keep only top 5
    else:
        print("sorry,but","choice,isn't a valid choice")

    
