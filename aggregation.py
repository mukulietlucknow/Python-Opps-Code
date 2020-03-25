class Salary:
    def __init__(self,pay,reward):
        self.pay = pay
        self.reward = reward

    def annual_salary(self):
        return (self.pay * 12) + self.reward

class Employee:
    def __init__(self , name , position , sal):
        self.name = name
        self.position = position
        self.final_salary_e = sal

    def final_salary(self):
        return self.final_salary_e.annual_salary()


sal = Salary(1000 , 400)
emp = Employee("mukul" , "engineer" , sal)
print(emp.final_salary())
