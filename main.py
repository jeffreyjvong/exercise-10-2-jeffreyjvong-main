#!/usr/bin/env python3
# GitHub 10.2: Student Class

# MODIFY THE CLASS
class Student:
    def __init__(self):
        self.name = "New Roadrunner"
        self.gpa = 0.0
        self.grades = []

    def set_name(self, name):
        if name.strip() == "":
            self.name = "A Roadrunner"
        else:
            self.name = name

    def get_name(self):
        return self.name
    
    def set_grades(self, grade):
        self.grades.append(grade)
        self.calculate_gpa()

    def get_grades(self):
        return self.grades
    
    def calculate_gpa(self):
        if len(self.grades) == 0:
            self.gpa = 0.0
        else:
            self.gpa = sum(self.grades) / len(self.grades)

    def get_gpa(self):
        return self.gpa
    
    def message_student_gpa(self):
        if len(self.grades) == 0:
            return f"{self.get_name()} has a GPA of {self.get_gpa():.2f} with no classes completed."
        else:
            conversion = {4 : "A", 3 : "B", 2 : "C", 1 : "D", 0 : "F"}
            i = 0
            g = []
            while i < len(self.grades):
                g.append(conversion.get(self.grades[i]))

                i += 1
            return f"{self.get_name()} has a GPA of {self.get_gpa():.2f} with the following letter grades: {', '.join(g)}."

# MODIFY THE MAIN PROGRAM
def main():
    # Task: Create Student object
    stu = Student()
    # Task: Output the result of message_student_gpa()
    print(stu.message_student_gpa())

    # Task: Take input and modify the Name attribute
    name = input("Name: ")
    stu.set_name(name)
    grade = int(input("Grade: "))

    # Task: Take input and modify the Grades & GPA attributes
    while grade >= 0 and grade <= 4:
        stu.set_grades(grade)
        grade = int(input("Grade: "))
        
    
    # Task: Output the result of message_student_gpa()
    print(stu.message_student_gpa())

# DO NOT MODIFY BELOW
if __name__ == "__main__":
    # Call Main Program
    main()
