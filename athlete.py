class Athlete:
	def __init__(self, name):
		self.name = name
		self.current_scores = [0, 0, 0, 0, 0, 0, 0]
		self.current_start_values = [0, 0, 0, 0, 0, 0, 0]

	def get_name(self):
		return self.name