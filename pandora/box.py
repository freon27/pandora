class Box:
	def __init__(self, levels):
	  	if(not len(levels)):
			raise Exception('You must provide at least one level')
		self._levels = levels
		self._current_level = 0
	
	def current_level(self):
		return self._current_level + 1

	def message(self):
		return self._levels[self._current_level].message

	def solve(self):
		if self._levels[self._current_level].solve():
			self._current_level += 1
			return True
		else:
			return False

	def hint(self):
		return self._levels[self._current_level].get_hint()

class Level:
	def __init__(self, message, hints):
		self.message = message
		self.hints = hints
		self._current_hint = 0 

	def get_hint(self):
		return self.hints[self._current_hint]

	def next_hint(self):
		if self._current_hint < len(self.hints) - 1:
			self._current_hint = self._current_hint + 1
		return self.get_hint()

	def solve(self):
		raise NotImplementedError('You must override the solve method in a subclass of Level')

