score= []

choice= None

while choice != "0":

    print("score keeper\n0-exit\n1-show scores\n2-add scores\n3-delete scores\n4-sort scores")

    choice=input("choice ")

    if choice=="0":
        print("goodbye")

    elif choice=="1":
        print("high scores")
        
        for score in scores:

            print(score)
        


    elif choice=="2":
            score=int(input("what score did you get"))
            #tacks at the end of list and becomes one element longer
            scores.append(score)
            
    elif choice=="3":
            score=int(input("what score did you get"))
            #removes element based on its value
            scores.remove(score)

    elif choice=="4":
            #ascending order
           # scores.sort()
           scores.reverse()

    elif choice=="5":
           score=int(input("what score did you get"))
           #counts number of ooccurences
           scores.count(score)
           #inserts value at position
           #scores.insert(1,50)
           #pop([i]) returns value at position and removes it

    else:
           print("sorry invalid choice")





