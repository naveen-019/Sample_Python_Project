import random

top_of_range = input("Enter your number : ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        print("please enter larger then 0 next time ")
        quit()
else:
    print("please type number next time ")
    quit()

random_num=random.randint(0,top_of_range)
guess=0

while True:
    guess+=1
    user_guess=input("make a guess :")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please enter a next number :")
        continue
    if user_guess == random_num:
        print("you got it !")
        break
    elif user_guess > random_num:
        print("you were above the number !")
    else:
        print("you were below the number !")

print("you got it in",guess,"guesses")




