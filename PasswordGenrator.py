'''Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters,
 uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. '''

#Name : Sarthak Vaghela
#date : 01/26/2021 (mm/dd/yyyy)

import random
import string

def random_string(length = 32, uppercase = True, lowercase = True, numbers = True, symbols = True):     #creating a methode which includes all the character needed for a strong password
    characterset = ''

    if uppercase:                                   #adding uppercase to our passwprds
        characterset += string.ascii_uppercase

    if lowercase:
        characterset += string.ascii_lowercase      #adding lowercase to our passwords
    
    if numbers:
        characterset += string.digits               #adding nmbers to our passwords
    
    if symbols:
        characterset += string.printable            #adding symbols to our passwords
    
    return ''.join(random.choice(characterset) for i in range(length) )     #returnijng a string which is 32 characters long

def remove_whitespace(str1):      # PRINTABLES contains whitespaces which are not allowed in passwords so I created this function to remove any whitespacing in the output
    str1 = str1.replace(' ','')
    return str1

password = remove_whitespace(random_string(16)) # assigning the first 16 letters of 32 letters string to password variable
print(password) #printing output