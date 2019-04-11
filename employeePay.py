#solution 1
class Person:
  def __init__(self, name, id, payRate, hoursWorked):
    self.name = name
    self.id = id
    self.payRate = payRate
    self.hoursWorked = hoursWorked

  def emplPay(self):
    if self.hoursWorked > 40:
	    totalPay = self.payRate * 40 + (1.5 * self.payRate) * (self.hoursWorked - 40)
    else:
        totalPay = self.payRate * self.hoursWorked
    print('Name: ' + self.name  + ' ID#: ' + self.id + ' Salary: ' + str (totalPay))

p1 = Person("Mary", "001", 15.00, 40)
p1.emplPay()
p2 = Person("John", "002", 22.00, 25)
p2.emplPay()
p3 = Person("Bob", "003", 35.00, 4)
p3.emplPay()
p4 = Person("Mel", "004", 43.00, 62)
p4.emplPay()
p5 = Person("Jen", "005", 17.00, 33)
p5.emplPay()
p6 = Person("Sue", "006", 29.00, 45)
p6.emplPay()
p7 = Person("Ken", "007", 40.00, 36)
p7.emplPay()
p8 = Person("Dave", "008", 20.00, 17)
p8.emplPay()
p9 = Person("Beth", "009", 37.00, 37)
p9.emplPay()
p10 = Person("Ray", "010", 16.50, 80)
p10.emplPay()  


#solution 2
#function to calculate pay
def emplPay(payRate, hoursWorked):
	if hoursWorked > 40:
		pay40 = payRate * 40
		pay40More = (1.5 * payRate) * (hoursWorked - 40)
		totalPay = pay40 + pay40More
	if hoursWorked <= 40:
		totalPay = payRate * hoursWorked
	
	return totalPay

name = input("Please enter your name: ")
print(name)

ID = input("Please enter your ID: ")
print(ID)
	
hoursWorked = input("Please enter your hours worked: ")
print(hoursWorked)

payRate = input("Please enter your pay rate: ")
print(payRate)
	
totalPay = emplPay(float (payRate), int (hoursWorked))
	
print('Your name: ' + name  + ' ID#: ' + ID + ' Salary: ' + str (totalPay))


# Some other thoughts about the solution
#3. dictionaries for records employee, pay rate, time, etc.
#recordsPay = {}

#4. Ziplist


#5. input excel as pd
#read the table and use function
