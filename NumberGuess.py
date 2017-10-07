'''This is a number guess program. Program rolls two dices randomly and ask the user to guess the total number. If user gives out a larger number, user wins. Vice versa'''
# Shuhui Ding 9/26/2017
# it's a codeacedmy project
from random import randint
from time import sleep
import sys
# get user guess function
def get_user_guess():
  user_guess = int(raw_input("Guess the total values of the dice: \n"))
  return user_guess

def get_answer():
        answer = raw_input("You have tried Five times, do you want to get the result? Y/N")
        if (answer == "Y" or answer == "y"):
          print "the first roll is %d" % (first_roll)
          sleep(0.5)
          print "the second roll is %d" % (second_roll)
          sleep(0.5)
          print "the total roll is %d" % (total_roll)
          sleep(0.5)
          sys.exit()
          return
        elif (answer == "N" or answer == "n"):
          print "Alright, good luck"
          appearance = 1
        return appearance

def roll_dice(number_of_sides):
  global first_roll
  global second_roll
  global total_roll
  global appearance
  first_roll = randint(1, number_of_sides) 
  second_roll = randint(1, number_of_sides)
  total_roll = first_roll + second_roll
  max_val = 2*number_of_sides
  appearance = 0
  print "the maximum possible value is %s" % (str(max_val))
  sleep(1)
  user_guess = get_user_guess()
  if (user_guess > max_val):
    print "The value is invalid"
    return
  else :
    print "Rolling..."
    sleep(2)
    print "Result.."
    count = 1
    last_guess = 0
    while (last_guess != total_roll ) :
      if (user_guess == total_roll) :
        print "Perfect! You guess the number just right in just %s time" % (count)
        return
      elif (user_guess > total_roll) :
        print "Your guess is a bit larger"
        count = count + 1
        last_guess = user_guess
        if (count >= 6 and appearance == 0) :
          appearance = get_answer()
        user_guess = int(raw_input("Try agian: \n"))
      else :
        print "Your guess is a bit smaller"
        count = count + 1
        last_guess = user_guess
        if (count >= 6 and appearance == 0) :
          appearance = get_answer()
        user_guess = int(raw_input("Try agian: \n"))
   
    
roll_dice(6)
                             