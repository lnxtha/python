class Vechile():
	#hello = 'hello'

	#number_of_wheels = ''
	def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
		print('this is a constructor and it is called auto')
		self.number_of_wheels = number_of_wheels
	
	def display(self):
		return self.number_of_wheels

a = Vechile('1','2','3','4')
print(a.display())
