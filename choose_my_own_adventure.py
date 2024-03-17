name=input("Enter your name :")
print("Welcom",name,"to this adveture ! ,let's Go")

answer = input("once upon a time you were going to magical forest. you see a lion ! at the time you dicide run/fight :").lower

if answer == "run":
    answer = input("then you are come to river and you dicide to swim/walk around :").lower()

    if answer == "swim":
        print("you eaten by crocoldils.you lost !")
        quit()
    elif answer == "walk around ":
        print("you were see the stranger !")
    else:
        print("invalid input !")
else:
    answer == "fight"
    print(" you kill the lion . and you save the princess .")

print("you won the game")