class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.__salary = salary  # Private attribute

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
            print(f"Salary updated to {self.__salary}.")
        else:
            print("Invalid salary amount. Salary must be greater than 0.")

    def get_salary(self):
        return self.__salary

    def display_info(self):
        print(f"Employee Name: {self.name}, Employee ID: {self.employee_id}")


# Taking input from the user
name = input()
employee_id = input()
initial_salary = int(input())
new_salary = int(input())

# Creating an instance of Employee
employee = Employee(name, employee_id, initial_salary)

# Displaying employee information
employee.display_info()

# Updating salary
employee.set_salary(new_salary)

# Displaying updated salary
print(f"Current Salary: {employee.get_salary()}")