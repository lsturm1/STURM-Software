from routine import Routine

def main():
	data = load_roster("./data/roster.txt")
	load_data("./data/data.txt", data)


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