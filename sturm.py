from athlete import Athlete
import constants

def main():
	print_intro()
	roster = load_roster()

	while True:
		display_menu()
		user_input = raw_input('Enter choice: ')
		if user_input != constants.QUIT:
			perform_action(user_input, roster)
		else:
			print "Have a nice day!"
			break
			

def display_menu():
	print "Menu:"
	print "1) Enter Scores  2) Upload Scores from File -1) Quit"

def perform_action(choice, roster):
	if choice == constants.ENTER_SCORES:
		enter_scores(roster)
	elif choice == constants.UPLOAD_SCORES:
		print "not implemented"

def enter_scores(roster):
	print "\n\nFor each athlete enter their 6 scores and start value in the format start_value/score"
	print "If the athlete did not do that event, enter a 0"
	print "Example: 5.4/14.2 6.0/4.5 0 0 4.2/13.1 5.0/13.5 \n"

	for name in roster:
		scores = raw_input("%s: " % (name))
		# parsed_scores = parse_scores(scores)
		# update_athlete(roster, name, parsed_scores)


def load_roster():
	file = open("roster.txt", 'r')
	roster = {}

	for line in file:
		roster[line.rstrip()] = Athlete(line)

	print "\nRoster Loaded"
	return roster



def print_intro():
	print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
	print "Welcome to STURM Sowftware"
	user_input = raw_input("Press Enter to Continue: ")

if __name__ == '__main__':
	main()