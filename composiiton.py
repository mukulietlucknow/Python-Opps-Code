class Salary:
    def __init__(self,pay,reward):
        self.pay = pay
        self.reward = reward

    def annual_salary(self):
        return (self.pay * 12) + self.reward

class Employee:
    def __init__(self , name , position , pay ,  reward):
        self.name = name
        self.position = position
        self.final_salary_e = Salary(pay , reward)

    def final_salary(self):
        return self.final_salary_e.annual_salary()


emp = Employee("mukul" , "engineer" , 12000 , 10000)
print(emp.final_salary())
