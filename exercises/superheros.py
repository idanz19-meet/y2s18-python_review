# Write your solutions for 1.5 here!
class superhero:
	def __init__(self, name, superpower, strength):
		self.name = name
		self.superpower = superpower
		self.strength = strength
	def powerlevel(self):
		print(self.name, self.strength)
	def save_civilian(self, work):
		if work > self.strength:
			print(self.name, "is not strong enough!")
		else:
			self.strength -= work
			print(self.strength)

n = superhero("nightingale", "teleportaition", 9000)
n.powerlevel()
n.save_civilian(9500)