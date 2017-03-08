# This is the main file of the gymnastics software program.
#
# Author: Luke Sturm
from routine import Routine
import constants

def main():
	data = load_roster("./data/roster.txt")
	load_data("./data/data.txt", data)
	choice = display_menu(constants.MAIN_MENU_TEXT, constants.MAIN_MENU_PROMPT, constants.MAIN_MENU_OPTIONS)

	while (choice != constants.QUIT):
		perform_task(choice, data)
		choice = display_menu(constants.MAIN_MENU_TEXT, constants.MAIN_MENU_PROMPT, constants.MAIN_MENU_OPTIONS)

	print "\nHave a nice day!"

# Function: perform_task
# This function is the main directory to all the of statistical functions
# in the program
# 
# Input: choice - the users choice from the main menu, data - all the routine
# 		 data
# Output: performs task
def perform_task (choice, data):
	if choice == constants.INDIVIDUAL:
		name = display_menu(constants.INDIVIDUAL_MENU_TEXT, constants.INDIVIDUAL_MENU_PROMPT, data)
		individual_summary(name, data)
		# athlete_summary(name)
	elif choice == constants.TEAM:
		print "Not yet implemented\n"
		# team_menu()

def individual_summary(name, data):
	sorted_events = sort_by_event(data[name])

	for event in sorted_events:
		print event
		for routine in sorted_events[event]:
			print routine.score
	# event_means = calc_means(sorted_events)
	# event_medians = calc_medians(sorted_events)
	# hit_percentages = calc_hit_percentages(sorted_events)
	# extrema = calc_extrema(sorted_events)


def sort_by_event(routines): 
	# map from event name to routines
	sorted_events = {"FX": [], "PH": [], "SR": [], "VT": [], "PB": [], "HB": []}

	for routine in routines:
		sorted_events[routine.event].append(routine)

	return sorted_events


# Function: display_menu
# This function displays a menu and asks the user for an input choice 
#
# Input: script - a string with the menu options, prompt - the question
# 		 asked of the user. valid_options - an array of all the valid menu 
# 		 options to choose from
# Output: returns the user choice 
def display_menu(script, prompt, valid_options):
	print script
	choice = raw_input(prompt)

	while choice not in valid_options:
		choice = raw_input("Error. Enter a valid option: ")

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