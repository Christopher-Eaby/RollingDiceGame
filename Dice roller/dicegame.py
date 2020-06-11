# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`
Created on Thu Jun 11 10:46:46 2020
@author: Chris


This program is a rolling dice game that includes a database and a text
file containing previous results.
"""
#imports
import time
import sqlite3 as sql #SQL for database
import random as ran #to add a random int
from PIL import Image #for importing the dice images
from IPython.display import display as disp #for displaying images

#variables for the single rolls and the total of all the rolls
totalroll = 0 
roll = ""

#creates a connection between the database and the python file
connection = sql.connect("rollsDB.db") 
#allows the python file to execute SQL queries
crsr = connection.cursor() 

#function to create a new table if there isn't already one
#to store the rolls and a name for the rolls
def create_table(): 
    crsr.execute('CREATE TABLE IF NOT EXISTS rolls (Roll, Number, Name TEXT)')

#creating the table if it doesn't already exist
create_table()

#function to add data to the rolls table, it is then updated.
def data_entry(roll, name): 
    crsr.execute("INSERT INTO rolls (Roll, Name) VALUES(?, ?)", (roll, name)) 
    connection.commit() 

#function to send all the data from the roll and total to a textfile
def outputToFile(output):
    File_object = open("rolls.txt","a")
    File_object.writelines(output)
    File_object.close()

#checking if the user wants to roll the dice
print("--------------------------------------")
print("Welcome to the Dice Rolling simulator!")
print("this program will roll as many dice as") 
print("you want and output the total:")
print("")
print("--------------------------------------")
roll = input("Would you like to roll some dice ? (yes/no) \n> ")

#function to assign specific images to numbers that are entered
#using the PIL module to import the images and save them as variables
def diceimages(num):
    img1 = Image.open(r"Dice\Alea_1.png")
    img2 = Image.open(r"Dice\Alea_2.png")
    img3 = Image.open(r"Dice\Alea_3.png")
    img4 = Image.open(r"Dice\Alea_4.png")
    img5 = Image.open(r"Dice\Alea_5.png")
    img6 = Image.open(r"Dice\Alea_6.png")
    if num == 1:
        return img1
    elif num == 2:
        return img2
    elif num == 3:
        return img3
    elif num == 4:
        return img4
    elif num == 5:
        return img5
    elif num == 6:
        return img6

#runs through the loop while the user still wants to play the game
while roll.lower() == "yes":
    totalroll = 0
    #asks user how many dice they want to roll
    amount = input("How many Dice ? \n> ")
    print("Rolling the dice...")
    
    #rolls the amount dice the user inputted
    for x in range(int(amount)):
        print("Dice " + str(x + 1))
        roll = ran.randint(0, 5) + 1
        #outputs the roll to the text file
        outputToFile("Roll : " + str(roll) + "\n")
        #displays the images inline in the console
        disp(diceimages(roll))
        print("\n")
        #adds to the total roll
        totalroll += roll
        time.sleep(1)
        
    #prints out the total of the rolls
    print("Total of roll : " + str(totalroll))
    #adds the total to the database "rolls"
    data_entry(totalroll, "Dice") 
    #adds it the total to the text file
    outputToFile("Total :" + str(totalroll) + "\n")
    print("Added to Database and text file")
    #checks if user wants to continue
    time.sleep(1)
    roll = input("Would you like to roll again ? (yes/no) \n> ")
    
#closes the database
crsr.close() 
connection.close() 
print("----------------------")
print("Done rolling the Dice!")
print("")
print("")
print("")
print(" Thank you for using ")
print("      my dice roller ")
print("----------------------")
#fin