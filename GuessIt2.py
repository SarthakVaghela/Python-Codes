# we’ve written a program that “knows” a number and asks a user to guess it.
#This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. 
#The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.


#name : SARTHAK VAGHELA
#date : 01/25/2021 (mm/dd/yyyy)

Min = 0
Max = 100
guess = 0
tries = 1
right = 'first'
running = True

print("think of a umber between 0 and 100.")

while running:
    hl = 'first'
    guess = (Min + Max)/2
    right = input("Is your number"+ str(guess)+ "?")

    if right == 'yes':
        break
    elif right != 'no':
        print("invalid")
    else:
        hl = input("higher or lower?")
    
    if hl == 'lower':
        Max = guess
        tries += 1
    elif hl == 'higher':
        Min = guess
        tries += 1
    elif hl != 'first':
        print("invalid")


print("I guessed it in "+ str(tries)+ "tries")