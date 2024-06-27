For my forensics science class, we had an assignment where we were supposed to
calculate the temperature of a dead body after it had been dead for x hours,
considering normal ambient temperature. So, I created an algorithm to automate
the calculations of body temperature after death (TOD).

The program begins by greeting the user and explaining its purpose. It then asks
the user to enter the number of hours the body has been dead. The algorithm uses
a normal body temperature of 98.6°F and a cooling rate of 1.4°F per hour for the
first 11 hours and p.7°F per hour thereafter.

Based on the time entered, the program calculates the elapsed time and adjusts
the body temperature accordingly. If the time is between 1 and 11 hours, it
cools at 1.4°F per hour. This is because, in the first hour after death, the
temperature of the body remains the same (98.6°F).

After displaying the result, the program asks the user whether they want to
continue or exit. If 'Q' (or 'q') is entered, the program ends; otherwise it
repeats. (Q and q stand for quit).

Made by danilo.zs
