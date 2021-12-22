class Employee:
    def __init__(self, first, last, pay):  # it is like a constructor, the first argument is self
        self.first = first  # is same as  self.first = first # is same as
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    # class is blueprint


# emp1 = Employee()
# emp2 = Employee()

emp1 = Employee('John', 'Doe', 1000)
emp2 = Employee('John2', 'Doe2', 1000333)

# emp1 and emp2 are separate class instances

# print(emp1, emp2)
# creating instances variables
# emp1.first = 'John'
# emp1.last = 'Doe'
# emp1.email = 'John.Doe@company.com'
# emp1.pay = 1000
#
# emp2.first = 'John1'
# emp2.last = 'Doe1'
# emp1.email = 'John1.Doe1@company.com'
# emp2.pay = 1000

# print(emp)

# To avoid create those many instance variables for each employee, create a init method

print(emp1.first)
print(emp2.pay)
print(emp2.fullname())
print(emp1.fullname())

