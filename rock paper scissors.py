import random
import time
bot_choice=""
human_choice=""
stop_yes_no=""
continue_or_first=""
ing_or_not=""
print("Welcome to the rock paper scissors game!")
while stop_yes_no!=2:
    stop_yes_no=int(input("Do you want to "+continue_or_first+"play"+ing_or_not+"? type 1 if yes and 2 if no. "))
    if stop_yes_no==2:
        break
    human_choice=int(input("What is your choice of rock paper or scissors? If it is rock, type 1. If it is paper, type 2. If it is scissors, type 3. "))
    bot_choice=(random.randint(1, 3))
    print("Rock,")
    time.sleep(0.3)
    print("Paper,")
    time.sleep(0.3)
    print("Scissors,")
    time.sleep(0.7)
    print("Shoot!")
    if bot_choice==human_choice:
        print("The game was a draw!")
    if bot_choice==1 and human_choice==2:
            print("Congratulations! Your paper covered your opponent's rock!")
    if bot_choice==1 and human_choice==3:
        print("Sorry, you lost. Your scissors got smashed by your opponent's rock.")
    if bot_choice==2 and human_choice==1:
        print("Sorry, you lost. Your rock got covered by your opponent's paper.")
    if bot_choice==2 and human_choice==3:
        print("Congratulations! Your scissors cut through your opponent's paper.")
    if bot_choice==3 and human_choice==1:
        print("Congratulations! Your rock smashed your opponent's scissors.")
    if bot_choice==3 and human_choice==2:
        print("Sorry, you lost. Your paper got cut by your opponent's scissors.")
    continue_or_first="continue "
    ing_or_not="ing"
    continue
    
print("Thanks for playing!")

