#Importing the "random" library
import random

#Defining X as a random number between 1 and 15
x = random.randint(1,15)

#Printing the random number:
#print(x)

#Creating a list
myList = ["rock","paper","scissors"]
#Printing a random choice from the list
z = random.choice(myList)

#Creating a deck of cards
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
#Shuffling the deck
random.shuffle(cards)
#Printing the deck
print(cards)