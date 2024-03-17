print("welcome to my copmuter quiz game")
# getting input from user
play=input("Do you want to play ? ")

if play.lower() != "yes":
    quit()

print("let's start quiz game :) ")

score=0 # the score is strat with zero

answer = input("what is the CPU  ")
if answer.lower() =="central proccesing unit":
    print("correct !!")
    score+=1
else:
    print("incorrect ")

answer = input("what is the GPU ")
if answer.lower() =="graphics proccesing unit":
    print("correct !!")
    score+=1
else:
    print("incorrect ")
   

answer = input("what is the RAM ")
if answer.lower() =="random access memory":
    print("correct !!")
    score+=1
else:
    print("incorrect ")
    

answer = input("Which of the following is not a Python data structure? ")
if answer.lower() =="loop":
    print("correct !!")
    score+=1
else:
    print("incorrect ")

print("you got " + str(score) + "questins is correct")
print("you got" + str((score/4)*100) +"%.scores") 




