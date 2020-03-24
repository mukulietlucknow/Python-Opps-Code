n = str(input("your name please : "))
a = int(input("your age please : "))
m = int(input("your marks please : "))


class Student : 
	def __init__ (self , n,a,m):
		self.name = n
		self.marks = m
		self.age = a


	def display(self):
		print ("My name : ", self.name)
		print ("My age : ", self.age)
		print ("My marks : ", self.marks)



student1 = Student(n,a,m)
student1.display()