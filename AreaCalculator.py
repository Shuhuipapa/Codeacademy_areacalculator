'''
Area calcaulator which computes the area of a given shape as selected
by user. the calculator will be able to determine the area of Circle and Triangle
'''
# Creator: Shuhui Ding 9/21/2017
# Codeacademy project
import time
from math import pi # import pi value
from time import sleep 
from datetime import datetime

hint = "Don't forget to include the correct units! \nExiting..."

def dete_input(input_c):
    if input_c == "C":
      radius = float(raw_input ("Please enter the radius of the circle")) # get input from user and store it as a float number
      area = pi*radius**2 # calculate the area
      print ("The pie is baking")
      time.sleep(1) # sleep for 1 second
      print ("%.2f \n" % area) + hint # print area along with the hint
    elif input_c == "T":
      base = float(raw_input ("Please enter the base of the triangle")) # get input from user and store it as a float number\
      height = float(raw_input ("Please enter the height of the triangle")) # get input from user and store it as a float number
      area = 0.5 * base * height # calculate the area
      print "Uni Bi Tri..."
      time.sleep(1)
      print ("%.2f \n" % area) + hint # print area along with the hint
    else: 
      print "invalid input, the program will exist"
      
now = datetime.now()
print "The area calculator is on"
print '%s/%s/%s %s:%s' % ( now.month, now.day, now.year, now.hour, now.minute)
time.sleep(1) # sleep for 1 second
option = raw_input ("Enter C for Circle or T for Triangle \n:")
option = option.upper()
dete_input(option)
