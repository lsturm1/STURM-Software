class Routine:
	def __init__(self, name, date, event, start, score, deductions):
		self.name = name
		self.date = date
		self.event = event
		self.start = start
		self.score = score
		self.deductions = deductions
		self.deduction = start + 10.0 - score

	def __str__(self):
		return "Name: %s\t Date: %s\t Event: %s\t Start: %d\t Score: %d" % (self.name, self.date, self.event, self.start, self.score)


     		



