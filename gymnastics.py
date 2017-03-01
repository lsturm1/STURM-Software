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

def perform_task (choice):
	if choice == constants.INDIVIDUAL:
		print "Not yet implemented\n"
	elif choice == constants.TEAM:
		print "Not yet implemented\n"
		# team_menu()


def display_menu(script, valid_options):
	print script
	choice = raw_input("Enter an menu option: ")

	while choice not in valid_options:
		choice = raw_input("Error. Enter a valid menu option: ")

	return choice

def load_roster(filename):
	file = open(filename, 'r')
	data = {}

	for line in file:
		data[line.rstrip()] = []

	return data


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