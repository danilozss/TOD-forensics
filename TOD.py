while True:
   #Imports
   import math


   #Salutations
   print("Welcome to the Amazing digital calculator that will save you from some silly littles calculations on dead bodies")


   #Main
   normal_body_temperature = 98.6
   TOD = int(input("How many hours has the body been dead: "))


   #Cools
   body_cools = 1.4
   body_cools_2 = 0.7


   #Times
   time = TOD - 1
   time2 = time - 12


   #Algorithm


   if time <= 11 and time > 0:
       dozen_less = normal_body_temperature - body_cools * time
       print("Result for " + str(TOD) + " hours: " + str(round(dozen_less, 2)) + "°F")
   elif time >= 11:
       time2 = time - 11
       dozen_less = normal_body_temperature - body_cools * 11
       print("Result for " + str(TOD) + " hours: " + str(round(dozen_less - body_cools_2 * time2, 2)) + "°F")
   elif TOD == 0 or TOD == 1:
       print("Result for " + str(TOD) + " hours: " + str(normal_body_temperature) + "°F")


   #Continue


   choice = input("Enter Q to quit, or any other key to continue: ")
   if choice.lower() == 'q':
       break
#Made by danilo.zs
