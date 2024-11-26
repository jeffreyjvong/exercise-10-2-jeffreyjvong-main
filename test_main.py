#!/usr/bin/env python3
# GitHub 10.2: Student Class

# Import Modules
import main as app, random, string

# Global Variables
value_input = []
value_actual = []
d = lambda s, t : s / t

def mock_input(prompt):
    "Mock the Input Process"
    global value_input, value_actual
    value_actual.append(prompt)
    return str(value_input.pop(0))

def run_main_program():
    "Run the main() program and capture the results"
    global value_input, value_actual

    # Overwrite the input() function
    app.input = mock_input

    # Overwrite the print() function with 1 argument in the print()
    app.print = lambda arg1 : value_actual.extend([arg1])

    # Execute the main() function from the code
    app.main()

    return value_actual

def random_grade_integer():
    "Generate a Random List of Grades with GPA"
    random_grades = []
    stop = random.randint(4,15)
    for x in range(stop):
        g = random.choices((0,1,2,3,4), k=1)[0]
        random_grades.append(g)
    
    return random_grades, d(sum(random_grades), stop)

def random_grade_to_letter(grades):
    "Convert the Random Grades to a Letter Grade"
    letter_grade = ("F","D","C","B","A")
    random_letter = []
    for g in grades:
        random_letter.append(letter_grade[g])
    
    return tuple(random_letter)

def test_case1():
    "Case 1: Test main() with No Grades Entered (4 pt)"
    
    # Setup IO Variables
    global value_input, value_actual
    value_input = ["Wile E. Coyote", 6]
    value_actual = []
    value_expected = ["New Roadrunner has a GPA of 0.00 with no classes completed.", "Name: "]
    value_expected.extend(["Grade: "] * (len(value_input) - 1))
    value_expected.append("Wile E. Coyote has a GPA of 0.00 with no classes completed.")

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == value_expected

def test_case2():
    "Case 2: Test main() with 1 Grade Entered (4 pt)"
    
    # Setup IO Variables
    global value_input, value_actual
    value_input = ["Mike Ayala", 3, 7]
    value_actual = []
    value_expected = ["New Roadrunner has a GPA of 0.00 with no classes completed.", "Name: "]
    value_expected.extend(["Grade: "] * (len(value_input) - 1))
    value_expected.append("Mike Ayala has a GPA of 3.00 with the following letter grades: B.")

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == value_expected

def test_case3():
    "Case 3: Test main() with 3 Grades Entered (4 pt)"
    
    # Setup IO Variables
    global value_input, value_actual
    value_input = ["Thomas Tom", 3, 3, 2, -2]
    value_actual = []
    value_expected = ["New Roadrunner has a GPA of 0.00 with no classes completed.", "Name: "]
    value_expected.extend(["Grade: "] * (len(value_input) - 1))
    value_expected.append("Thomas Tom has a GPA of 2.67 with the following letter grades: B, B, C.")

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == value_expected

def test_case4():
    "Case 4: Test for name attribute and Methods (4 pt)"
    
    # Declare New Object
    test_case = app.Student()

    # Test Default Attribute Values
    assert test_case.name == "New Roadrunner"
    assert test_case.get_name() == "New Roadrunner"

    # Modify Name Attribute via Attribute
    random_name = ''.join(random.choices(string.ascii_letters, k=5))
    test_case.name = random_name
    assert test_case.get_name() == random_name

    # Modify Name Attribute via Method
    random_name = ''.join(random.choices(string.ascii_letters, k=7))
    test_case.set_name(random_name)
    assert test_case.get_name() == random_name

    # Modify Name Attribute via Method Using an "Empty" Value
    test_case.set_name(" ")
    assert test_case.get_name() == "A Roadrunner"

def test_case5():
    "Case 5: Test for grades attribute and Methods (4 pt)"
    
    # Declare New Object
    test_case = app.Student()

    # Test Default Attribute Values
    assert test_case.grades == []
    assert test_case.get_grades() == []

    # Modify Grades via Attribute
    test_case.grades = [4, 3, 2, 1, 0]
    assert test_case.get_grades() == [4, 3, 2, 1, 0]

    # Reset and Modify Grades via Method
    test_case.grades = []
    test_case.set_grades(2)
    test_case.set_grades(3)
    test_case.set_grades(1)
    test_case.set_grades(-2)
    test_case.set_grades(4)
    test_case.set_grades(0)
    test_case.set_grades(-4)
    assert test_case.get_grades() == [2, 3, 1, 4, 0]

def test_case6():
    "Case 6: Test for gpa attribute and Methods (8 pt)"
    
    # Declare New Object
    test_case = app.Student()

    # Test Default Attribute Values
    test_case.gpa = 4.0
    assert test_case.gpa == 4.0
    assert test_case.get_gpa() == 4.0

    # Modify Grades & GPA via Attribute
    test_case.gpa = 0.0
    test_case.grades = [3, 3, 3, 2]
    test_case.calculate_gpa()
    assert test_case.get_gpa() == 2.75

    # Reset & Modify Grades & GPA Attribute via Method
    test_case.gpa = 0.0
    test_case.grades = []
    test_case.set_grades(3)
    test_case.set_grades(3)
    test_case.set_grades(2)
    test_case.set_grades(-2)
    test_case.set_grades(3)
    test_case.set_grades(3)
    test_case.set_grades(2)
    test_case.set_grades(9)
    assert test_case.gpa == 2.6666666666666665
    assert test_case.get_gpa() == 2.6666666666666665

    # Reset & Modify Grades & GPA with Random Values via Method
    expected_grades, expected_gpa = random_grade_integer()
    test_case.gpa = 0.0
    test_case.grades = []
    for g in expected_grades:
        test_case.set_grades(g)

    assert test_case.gpa == expected_gpa
    assert test_case.get_gpa() == expected_gpa

def test_case7():
    "Case 7: Test for output message Methods (4 pt)"
    
    # Declare New Object
    test_case = app.Student()

    # Test Default Attribute Values
    assert test_case.message_student_gpa() == "New Roadrunner has a GPA of 0.00 with no classes completed."

    # Modify Grades Attribute & Calculate the GPA via the Method
    test_case.set_name("John Smith")
    test_case.grades = [4, 4, 3, 4]
    test_case.calculate_gpa()
    assert test_case.message_student_gpa() == "John Smith has a GPA of 3.75 with the following letter grades: A, A, B, A."

    # Reset Grades & Modify Grades via Method
    test_case.set_name("")
    test_case.gpa = 0.0
    test_case.grades = []
    test_case.set_grades(4)
    test_case.set_grades(-1)
    test_case.set_grades(3)
    test_case.set_grades(3)
    test_case.set_grades(3)
    test_case.set_grades(3)
    test_case.set_grades(3)
    test_case.set_grades(5)
    assert test_case.message_student_gpa() == "A Roadrunner has a GPA of 3.17 with the following letter grades: A, B, B, B, B, B."

def test_case8():
    "Case 8: Test for Random Values (4 pt)"

    # Declare New Object
    test_case = app.Student()

    # Random Test Values
    expected_name = ''.join(random.choices(string.ascii_letters, k=random.randint(4,10)))
    expected_grades, expected_gpa = random_grade_integer()
    expected_letter = random_grade_to_letter(expected_grades)

    # Modify the Object
    test_case.set_name(expected_name)
    for g in expected_grades:
        test_case.set_grades(g)

    expected_message = (expected_name, "has a GPA of", f"{expected_gpa:.2f}", "with the following letter grades:", ", ".join(expected_letter))

    # Unit Test the Get & Message Methods against the expected results
    assert test_case.get_name() == expected_name
    assert test_case.get_grades() == expected_grades
    assert test_case.get_gpa() == expected_gpa
    assert test_case.message_student_gpa() == " ".join(expected_message)+"."
