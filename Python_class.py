class Student:
	def __init__ (self):
		self.name = "mukul"
		self.marks = 95
		self.age = 20

	def talk(self):
		print ("My name : ", self.name)
		print ("My age : ", self.age)
		print ("My marks : ", self.marks)



s1 = Student()
s1.talk()
print (s1.name)