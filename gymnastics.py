# This is the main file of the gymnastics software program.
#
# Author: Luke Sturm
from routine import Routine
import constants

def main():
	data = load_roster("./data/roster.txt")
	load_data("./data/data.txt", data)
	choice = display_menu(constants.MAIN_MENU_TEXT, constants.MAIN_MENU_OPTIONS)

	while (choice != constants.QUIT):
		perform_task(choice)
		choice = display_menu(constants.MAIN_MENU_TEXT, constants.MAIN_MENU_OPTIONS)

	print "\nHave a nice day!"

# Function: perform_task
# This function is the main directory to all the of statistical functions
# in the program
# 
# Input: choice - the users choice from the main menu
# Output: performs task
def perform_task (choice):
	if choice == constants.INDIVIDUAL:
		print "Not yet implemented\n"
	elif choice == constants.TEAM:
		print "Not yet implemented\n"
		# team_menu()

# Function: display_menu
# This function displays a menu and asks the user for an input choice 
#
# Input: script - a string with the menu options, valid_options - an 
# 		 array of all the valid menu options to choose from
# Output: returns the user choice 
def display_menu(script, valid_options):
	print script
	choice = raw_input("Enter an menu option: ")

	while choice not in valid_options:
		choice = raw_input("Error. Enter a valid menu option: ")

	return choice

# Function: load_roster
# This function lods in the list of names of everyone on the roster
#
# Input: filename - the name of the file to read from
# Output: returns a map of names to empty lists, which will hold 
# routine objects
def load_roster(filename):
	file = open(filename, 'r')
	data = {}

	for line in file:
		data[line.rstrip()] = []

	return data


# Function: load_data
# This function loads all the routine data from a file and matches it
# to the person in the roster who did the routine. 
#
# Input: filename - name of the file with the roster names
# Output: updates the data dictionary, adding routine objects to it
def load_data(filename, data):
	file = open(filename, 'r')
	count = 0

	for line in file:
		if (count == 0 or count == 1):
			count += 1
			continue 

		parsed_line = line.split()
		name = parsed_line[0].rstrip()
		rout = Routine(name, parsed_line[1], parsed_line[2], float(parsed_line[3]), float(parsed_line[4]), parsed_line[5])
		data[name].append(rout) 


if __name__ == '__main__':
	main()