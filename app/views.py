from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
def Password_Generator():
    uppercaseLetter1=chr(random.randint(65, 90)) #Generate a random Uppercase letter 
    uppercaseLetter2=chr(random.randint(65, 90)) #Generate a random Uppercase letter 
    lowercaseLetter1=chr(random.randint(97, 112))	 #Generate a random Lowercase letter 
    lowercaseLetter2=chr(random.randint(97,112)) #Generate a random Lowercase letter 
    digit1=random.randint(0, 9) #Generate a random Digit
    digit2=random.randint(0, 9) #Generate a random Digit
    symbol=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']',':',';','"',"'",'<','>',',','.','/','?','|',]
    #Generate a random Punctuation Sign
    Symbol_Sign1=random.choice(symbol)
    Symbol_Sign2=random.choice(symbol)
    
    #Generate more characters here
    #....

    #Generate password using all the characters, in random order
    password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + str(digit1) + str(digit2) + Symbol_Sign1 + Symbol_Sign2
    return password
    

def Strong_Password(request):
   password1=Password_Generator()
   password2=Password_Generator()
   Password=password1+password2
   Password = shuffle(Password)
   d={'Password': Password}

   #Ouput
   return render(request, 'RPG.html', d)

