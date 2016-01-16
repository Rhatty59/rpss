#-----------------------------------------
# Rock-paper-scissors-lizard-Spock program
#
# 16 Apr 2015
#
# Richard Smith
#-----------------------------------------
import random

#------ number_to_name function ------
def number_to_name(number):
	"""function returns the name that equates to the number provided"""
	
	if number == 0:
		number_to_name = "rock"
	elif number == 1:
		number_to_name = "Spock"
	elif number == 2:
		number_to_name = "paper"
	elif number == 3:
		number_to_name = "lizard"
	elif number == 4:
		number_to_name = "scissors"
		
	return number_to_name
#------ end of number_to_name function ------

#------ name_to_number function ------
def name_to_number(name):
	"""function returns the number that equates to the name provided"""
	
	if name == "rock":
		name_to_number = 0
	elif name == "Spock":
		name_to_number = 1 
	elif name == "paper":
		name_to_number = 2 
	elif name == "lizard":
		name_to_number = 3
	elif name == "scissors":
		name_to_number = 4
		
	return name_to_number
#------ end of name_to_number function ------

#------ rpsls function ------
def rpsls(name):
	# Convert name to player_number using name_to_number
	player_number = name_to_number(name)
	
	# compute random guess for comp_number using random.randrange()
	# seed it to get truely random numbers
	
	random.seed()
	comp_number = random.randrange(0,5)
	
	#compute difference of player_number and comp_number modulo five(?)
	
	difference = (player_number - comp_number) % 5
	
	# now determine the winner
	
	if difference > 2:
		result = "Computer wins!"
	elif difference == 0:
		result = "Player and computer tie!"
	else:
		result = "Player wins!"
		
	# convert number to name
	comp_name = number_to_name(comp_number)
	
	# print results
	print (" ")
	print ("Player chooses " + name)
	print ("Computer chooses " + comp_name)
	print (result)
#------ end of rpsls function ------

#------ main program ------

# seed random number generator at the start
random.seed()

# Then run an iteration of rpsls with each player
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

#------ end of main program -------
