#Write a python program to print the following multiplication table?
#Your program should accept the table size from the user. Any size from
#1 to 15 is the accepted as input. Use Nested loops.

# Name : Sarthak Vaghela
# std no : 110005362
# date : 19 november, 2020


size=int(input("Enter the table size: "))
print("       ",end="")
# we are peinting the first row with row numbers with the code below
for x in range(size):  # simle for loop to print the first line
        if((x+1)<10):
                print("      "+str(x+1),end="")
        elif((x+1)<100):
                print("     "+str(x+1),end="")
#now we are printing the second row with special characters
print("\n      +-",end="")
for a in range(size):
        print("--------",end="")
print("\n")
#now we are writing a code to complete the rest of the multiplication table
for c in range(size):
        if(c<9):
                print("   "+str(c+1)+" | ",end="")
                for j in range(size):
                        if(((c+1)*(j+1))<10):
                                print("      "+str((c+1)*(j+1)),end="")
                        elif(((c+1)*(j+1))<100):
                                print("     "+str((c+1)*(j+1)),end="")
                        elif(((c+1)*(j+1))<1000):
                                print("    "+str((c+1)*(j+1)),end="")
                print("\n")
        else:
                print("  "+str(c+1)+" | ",end="")
                for j in range(size):
                        if(((c+1)*(j+1))<10):
                                print("      "+str((c+1)*(j+1)),end="")
                        elif(((c+1)*(j+1))<100):
                                print("     "+str((c+1)*(j+1)),end="")
                        elif(((c+1)*(j+1))<1000):
                                print("    "+str((c+1)*(j+1)),end="")
                print("\n")
