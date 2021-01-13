#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
#print out a message of congratulations to the winner, and ask if the players want to start a new game)

#Name: SARTHAK VAGHELA
#date: 01/13/2021 (mm/dd/yyyy)

import sys

def compare(p1,p2):
    if p1 == p2:
        return("Its a tie!")
    elif p1 == 'rock':
        if p2 == 'paper':
            return("Paper WINS!")
        else:
            return("Rock WINS")

    elif p1 == 'paper':
        if p2 == 'scissors':
            return("Scisorrs WINS!")
        else:
            return("Paper WINS!")
    
    elif p1 == 'scissors':
        if p2 == 'rock':
            return("Rock WINS!")
        else:
            return("Scissors WINS!")

    else:
        return("Invalid Input!, try again.")

    

while True:
    player1 = input("please enter your name: ")
    player2 = input("please enter your name: ")

    p1_answer = input("%s, please choose from rock, paper or scissors: " %player1)
    p2_answer = input("%s, please choose from rock paper ot scissors: " %player2)
    print(compare(p1_answer, p2_answer))
    x = input("Press any key to continue\nor type done to exit: ")
    if x == 'done': break