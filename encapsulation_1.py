class Speed:
	def __init__(self):
		self.speed = 10
		self.__new_speed  = 60

	def car_speed(self):
		print("your speed id : ",self.speed)
		print("your speed id : ",self.__new_speed)

	def get_speed(self):
		return self.__new_speed

	def set_speed(self, new_speed):
		self.__new_speed = new_speed


s = Speed()
s.speed = 100
print (s.speed)
print (s.get_speed())
s.set_speed(150)
print (s.get_speed())

