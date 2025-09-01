class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Roll: {self.roll_number}, Grade: {self.grade}")

    def updated_grade(self, new_grade):
        self.grade = new_grade
        print(f"{self.name}'s grade has been updated to {new_grade}.")

student = Student("Amit", "S123", "B")

student.display_info()
student.updated_grade("A")
student.display_info()
