# Python Project One
""" 
	Done by:
		Ahmad Al-Ghzawi
		Ahmad Taha
		Rahma Sandouqa
"""
# Classes
class Person:
	def __init__(self, name, address):
		self._name = str(name)
		self._address = str(address)
		
	def getName(self):
		return self._name
	
	def setName(self, name):
		self._name = str(name)
		
	def getAddress(self):
		return self._address
	
	def setAddress(self, address):
		self._address = address
		
	def __del__(self):
		print('Person', self._name, 'has been deleted')
#==============================================================================
class Employee(Person):
	def __init__(self, name, address, number, salary, jobTitle, loans):
		super().__init__(name, address)
		self.number = int(number)
		self.__salary = float(salary)
		self.__jobTitle = str(jobTitle)
		self.__loans = list(loans)
		
	def getSalary(self):
		return self.__salary
	
	def setSalary(self, salary):
		self.__salary = float(salary)
		
	def getJobTitle(self):
		return self.__jobTitle
		
	def setJobTitle(self, jobTitle):
		self.__jobTitle = jobTitle
		
	def getLoans(self):
		return self.__loans
		
	def getTotalLoans(self):
		totalLoans = sum(self.__loans)
		return totalLoans
		
	def getMaxLoan(self):
		length = len(self.__loans)
		maxLoan = max(self.__loans) if length > 0 else 0
		return maxLoan  
		
	def getMinLoan(self):
		length = len(self.__loans)
		minLoan = min(self.__loans) if length > 0 else 0 
		return minLoan 
		
	def setLoans(self, loans):
		self.__loans = list(loans)
		
	def setNewLoan(self, loan):
		self.__loans.append(int(loan))
		
	def printInfo(self):
		print('EMPLOYEE NUMBER',self.number, '\b:')
		print('Name >>>', self._name)
		print('Job Title >>>', self.__jobTitle)
		print('Salary =', self.__salary, '\bJOD')
		print('Loans >>>', self.__loans)
		print('  Total Loans =', self.getTotalLoans())
		print('Address >>>', self._address, end='\n\n')
		
	def __del__(self):
		super().__del__()
		print('Employee number', self.number, 'has been deleted', end='\n\n')
#==============================================================================
class Student(Person):
	def __init__(self, name, address, number, subject, marks):
		super().__init__(name, address)
		self.number = number
		self.__subject = str(subject)
		self.__marks = dict(marks)
		
	def getSubject(self):
		return self.__subject
	
	def setSubject(self, subject):
		self.__subject = str(subject)
		
	def getMarks(self):
		return self.__marks
	
	def setMarks(self, marks):
		self.__marks = dict(marks)
		
	def setNewMark(self, subject, mark):
		self.__marks[str(subject)] = int(mark)
		
	def getAvg(self):
		numberOfSubjects = len(self.__marks)
		summation = sum(self.__marks.values())
		avg = round(summation / numberOfSubjects, 2)
		return avg
		
	def getAMarks(self):
		aces = list(filter(lambda mark: mark[1] >= 90, self.__marks.items()))
		return aces
	
	def printInfo(self):
		print('STUDENT NUMBER', self.number, '\b:')
		print('Name >>>', self._name)
		print('Subject >>>', self.__subject)
		print('Marks:')
		for subject, mark in self.__marks.items():
			print('   ' + subject, '\b:', mark) 

		print('Average =', self.getAvg(),'\b/100', end='\n\n')
		
	def __del__(self):
		super().__del__()
		print('Student number', self.number, 'has been deleted', end='\n\n')	
		
#==============================================================================
#==============================================================================
#==============================================================================
# Functions
def information(array, title):
	print('ALL', str(title).upper(), 'INFORMATION:')
	for item in array:
		print(item.printInfo)
		item.printInfo()	
#==============================================================================		
def loansInformation(employees):
	print('LOANS INFORMATION:')
	grandTotal = 0
	for employee in employees:
		print('Employee Name >>>', employee.getName())
		print('Loans >>>', employee.getLoans())
		grandTotal = grandTotal + employee.getTotalLoans()
		print('Total Loans =', employee.getTotalLoans(), end='\n\n')
		
	print('Grand Total =', grandTotal, end='\n\n')
#==============================================================================
def loansDictionary(employees):
	loansDic = {}
	for employee in employees:
		loansDic[str(employee.number)] = employee.getLoans()
		
	return loansDic 
#==============================================================================
def highestLoan(loans):
	if(len(loans) == 0): 
		return 0
	
	highest = reduce(lambda highest, loan: 
		highest if highest > loan else loan, loans)
		
	return highest
#==============================================================================
def lowestLoan(loans):
	if(len(loans) == 0): 
		return 0
	
	lowest = reduce(lambda lowest, loan: 
		lowest if lowest < loan else loan, loans)
		
	return lowest
#==============================================================================
def AStudents(students):
	print('A STUDENTS ARE:')
	for student in students:
		if(len(student.getAMarks()) > 0):
			print('Name:', student.getName())
			print('Subject:', student.getSubject())
			print('Marks:')
			for subject, mark in student.getMarks().items():
				print('   ' + subject, '\b:', mark)
			
			print()
#==============================================================================
#==============================================================================
#==============================================================================
# Objectives
#1
employees =[
		Employee('Ahmad Yazan', 'Amman,Jordan', 1000, 500, 'HR Consultant', [434, 200, 1020]),
		Employee('Hala Rana', 'Aqaba,Jordan', 2000, 750, 'Department Manager', [150, 3000, 250]),
		Employee('Mariam Ali', 'Mafraq,Jordan', 3000, 600, 'HR S Consultant', [304, 1000, 250, 300, 500, 235]),
		Employee('Yasmeen Mohammad', 'Karak,Jordan', 4000, 865, 'Director', [])
		]

#2
students = [
		Student('Khalid Ali', 'Irbid, Jordan', 20191000,'History', 
		  {
	 'English': 80,
	 'Arabic': 90,
	 'Art': 95,
	 'Management': 75
	 }),
	Student('Reem Hani', 'Zarqa, Jordan', 20182000,'Software Engineering', 
		 {
	'English': 80, 
	'Arabic': 90, 
	'Management': 75, 
	'calculus': 85, 
	'OS': 73, 
	'programming': 90
	}),
	Student('Nawras Abdullah', 'Amman, Jordan', 20161001, 'Arts', 
		 {
	'English': 83, 
	'Arabic': 92, 
	'Art': 90, 
	'Management': 70
	}),
	Student('Amal Raed', 'Tafelah, Jordan', 20172030, 'Computer Engineering', 
		 {
	'English': 83,
	'Arabic': 92, 
	'Management': 70, 
	'calculus': 80, 
	'OS': 79, 
	'programming': 91
	})
	]

#3, 4
numOfEmployees = len(employees)
numOfStudents = len(students)
print('Number of Employees =', numOfEmployees, end='\n\n')
print('Number of Students =', numOfStudents, end='\n\n')

#5, 6
information(employees, 'employees')
information(students, 'students')

#7
from functools import reduce
highestAvg = reduce(lambda avg, student: 
	avg if(avg > student.getAvg()) 
	else student.getAvg(), 
	students, 0)
	
print('The Highest Average =', highestAvg, end='\n\n')

#8, 9
maximumLoan = reduce(lambda loan, employee: 
	loan if(loan > employee.getMaxLoan()) 
	else employee.getMaxLoan(), 
	employees, 0)
	
minimumLoan = reduce(lambda loan, employee: 
	loan if(loan < employee.getMinLoan()) 
	else loan if(employee.getMinLoan() == 0) 
	else employee.getMinLoan(), 
	employees, maximumLoan)
	
print('The Maximum Loan =', maximumLoan, end='\n\n')
print('The Minimum Loan =', minimumLoan, end='\n\n')

#10
loansInformation(employees)

#11
loansData = loansDictionary(employees)
print(loansData,)

#12
for number, loans in loansData.items():
	highest = highestLoan(loans)
	lowest = lowestLoan(loans)
	print('The Highest Loan for Employee Number', number, '=', highest)
	print('The Lowest Loan for Employee Number', number, '=', lowest, end='\n\n')
	
#13
AStudents(students)

#14, 15, 16
highestSalary = reduce(lambda salary, employee: 
	salary if (salary > employee.getSalary()) 
	else employee.getSalary(), 
	employees, 0)
	
lowestSalary = reduce(lambda salary, employee: 
	salary if (salary < employee.getSalary()) 
	else salary if (employee.getSalary() == 0) 
	else employee.getSalary(), 
	employees, highestSalary)
	
totalSalaries = reduce(lambda salary, employee: 
	salary + employee.getSalary(), 
	employees, 0)
	
print('SALARIES:')
print('The Highest Salary =', highestSalary, '\bJOD')
print('The Lowest Salary =', lowestSalary, '\bJOD')
print('Total Salaries =', totalSalaries, '\bJOD', end='\n\n')

#17
del employees, students