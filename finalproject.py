#!/usr/bin/python3
# Mad Libs Final Project
""" Mad Libs Generator

----------------------------------------

"""

#Loop back to this point once code finishes

loop = 1

while (loop < 10):

# All the questions that the program asks the user

	verb_1 = input("Enter a verb of choice, and press enter:"),

	adj_1 = input("Enter an adjective of choice, and press enter:"),

	verb_2 = input("Enter second verb of choice, and press enter:"),

	body_part = input("Enter a body part name of choice, and press enter:"),

	adverb = input("Enter an adverb of choice, and press enter:"),

	body_part_2 = input("Enter any body name of your choice,and press enter:"),

	noun = input("Enter a noun of choice, and press enter:"),

	verb_3 = input("Enter the third verb of choice, and press enter:"),

	animal = input("Enter name of any animal of choice, and press enter:"),

	noun_2 = input("Enter an noun of choice , and press enter:"),

	verb_4 = input("Enter the fourth verb of choice, and press enter:"),

	adj_2 = input("Enter an adjective of chioce, and press enter:"),

	color = input("Enter any color name, and press enter:")

#Displays the story based on the users input

	print(story)

print ("------------------------------------------")

story = "Most doctors agree that bicycle of" + verb_1 + " is a/an " + adj_1 + " form of exercise." + verb_2 +" a bicycle enables you to develop your " + body_part + " muscles as well as " + adverb + " increase the rate of a " + body_part_2+" beat. More " + noun + " around the world "+ verb_3 +" bicycles than drive "+ animal +". No matter what kind of "+ noun_2 +"you "+ verb_4 +", always be sure to wear a/an "+ adj_2 +" helmet.Make sure to have  " + color + " reflectors too! "

print ("------------------------------------------")

# Loop back to "loop = 1"

loop = loop + 1


