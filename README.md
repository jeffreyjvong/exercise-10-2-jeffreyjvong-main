# GitHub 10.2: Student Class

## Student Information

* Jeffrey Vong
* Fall/2014
* 77617

## Instructions

Define the Student class that has three attributes, `name`, `grades`, and `gpa` then implement the following instance methods:

* `__init__(self)` - constructor that sets the attributes `name` to the string "New Roadrunner", `gpa` to the float 0.0, and `grades` to an empty list.
* `set_grades(self, grade)` - appends an integer grade element with an allowed value of 4, 3, 2, 1, 0 to the `grades` list attribute and recalculates the gpa. Values that do not meet the allowed value will not be appended.
* `set_name(self, name)` - sets the students name to the `name` attribute. If the argument passed into the method is an empty string, then it should store the name as `A Roadrunner`.
* `get_gpa(self)` - returns the students `gpa` attribute.
* `get_grades(self)` - returns the students `grades` attribute.
* `get_name(self)` - returns the students `name` attribute.
* `calculate_gpa(self)` - calculates the GPA based on the `grades` list and stores it in the `gpa` attribute. Should be called anytime a grade appended to the grades attribute.
* `message_student_gpa(self)` - processes and returns a string message that has one of two possible return values that utilizes all three class attributes.
  * If no grades are entered the message returned will say: `NAME has a GPA of 0.0 with no classes completed.`
  * if grades are entered the message returned will say: `NAME has a GPA of 2.67 with the following letter grades: B, B, C`

Then modify the `main()` program to test the object creation and usage. The main program should first define the object and immediately output the default attribute values using the `message_student_gpa()` method. Then the user should be prompted `input("Name: ")` their name followed by a loop of integer grades between 0 to 4 with the `input("Grade: ")` prompt. Entering a grade greater than 4 or less than 0 will result in the user exiting the loop. After exiting the loop, the program will output the updated attribute values by using the `message_student_gpa()` method.

Need help? Contact the [Math, Science, & Engineering Center](https://www.riohondo.edu/mathematics-and-sciences/math-science-center/) for tutoring assistance. Any form of sharing or uploading of this assignment on external websites is strictly prohibited.

### Tips

* Do not modify the `input()` function prompts as these are setup specifically for this exercise, but you may cast the input as a different data type.
* String inputs may contain a hidden return character that needs to be handled prior to storing in the object.
* Unit tests will test both the `main()` function and `Student()` class methods individually.
* Use the dictionary `{4:"A", 3:"B", 2:"C", 1:"D", 0:"F"}` for conversion from integer grade value to letter grade value during the `message_student_gpa()`.
* Format the GPA in `message_student_gpa()` to be `{your_value:.2f}` but leave the unmodified value in the `gpa` attribute.
* GPA can be calculated as the sum of the grades in the list divided by the total number of grades in the list.

## Exercise Questions

Do not provide code for any of the questions. Delete the text that says *YOUR ANSWER HERE* and provide answers to each of the questions in normal written language answering each of the questions.

### Question 1

**Review the file test_main.py and locate `test_case4()` and `test_case5()`. What did these tests cases do to ensure the class was functioning?**

YOUR ANSWER HERE

**How do get and set methods work within the context of the class and the object? What is the advantage of using this method?**

YOUR ANSWER HERE
