# create rock scissors paper program that asks for user input
# 0 = rock 1 = scissors 2 = paper

import random

def whatIsIt(num):
  if num < 0 or num > 2: 
    return "You gave a wrong number! Number has to be between 0 and 2"
  choices = ["Rock", "Scissors", "Paper"]
  return choices[num]

#gives back 0-2 at random
def computerChoice():
  return random.randint(0, 2)

def rockScissorsPaper():
  #Code Here

  choice = input("choose rock or scissors or paper: ")
  print(choice)

  #if statement that checks if user's choice is correct
  if choice == "Rock" or choice == "Scissors" or choice == "Paper":
    print("Your response is valid")
  else:
    print("Your response is not valid")
    
    #computer science
    computer_choice = whatIsIt(computerChoice())
    print("computer choice: ")
    print(computer_choice)

    #print tie if user and computer response is the same
    if choice  == computer_choice:
        print("It's a tie")
    else:
      print("It's not a tie")
    
    if choice == "Rock":
       if  computer_choice  == "Scissors":
          print("The user won!")
       if   computer_choice == "Paper":
          print("The computer won!")
    elif choice == "Scissors":
        if  choice == "Paper":
          print("The user won!")
        if  choice == "Rock": 
           print("The computer won")
    elif choice == "Paper":
       if  choice == "Rock":
          print("The user won!")
       if choice == "Scissors":
          print("The computer won!")

       
    #ask user for a choice of rock scissor paper

    #print random computer response
    print(whatIsIt(computerChoice()))

rockScissorsPaper()


