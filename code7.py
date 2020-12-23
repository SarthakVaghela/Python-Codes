#The factorial of a non-negative integer n, denoted by n! is the product
#of all positive integers less than or equal to n.
#For example, 5! = 5 × 4 × 3 × 2 × 1 = 120.
#The value of 0! is 1
#Write a python program for the following problem
#Ask the user to enter a positive integer n. between 1 and 20; You may
#assume the user will enter a valid input.
#Calculate the factorial of all numbers j (1 < j < n) from 1 – n
#(inclusive).
#For each j, print the value of j and j! with a suitable message and
#append each j! to a list called factorial list.
#Print the final factorial list with a suitable message.
#Write function called factorial that takes the entered number n and
#returns the factorial value, also write another function to print the
#factorial list?


def factPrint(n):
   x=[] # creating a list we will be using in this program 
  
   for a in range(1,n+1): # printing the factorial list for all n and n+1 numbers
       print("j=",end=" ")
       print(a, end="; ")
       print(a,end=" != ")
       R=fact(a)
       print(R)
       x.append(R)
   print("factorial list", end=" ")
   print(x) #output
      
def fact(n):
   R=1; # reseting r to one so we dont reate a new variable
   for a in range(1,n+1): #calculate factorial as n=n*n-1*n-2*...2*1
       R=R*a
   return R

print() # printing an empty line
a=input("please enter a positive integer between 1 and 20:") #taking input from user
a=int(a)
factPrint(a) # calling the function we created to print the output


#Name : SARTHAK VANRAJSINH VAGHELA
#STUDENT NUMBER : 110005362
