# GitHub 10.2: Student Class

You will need to test your solution using two methods, manual testing and via a unit test. We will be using pytest for all Unit Tests as it integrates well with GitHub Classroom. Points will be awarded based on passing the unit test.

## Task 1. Manual Testing in the Terminal

Before you submit your assignment to GitHub, make sure you run the two example test cases below to verify you get the same result. To execute a manual test in the terminal, use one of the following commands:

* Linux / Unix / Mac OS: `python3 main.py`
* Windows: `py main.py`
* Alternative: `python main.py`

Note, your install may differ so you may need to research how to execute your manual python command for your computer.

### Example Case 1 (12 pt)

**Case 1 Input**

```text
Victoria
4
4
4
2
-1
```

**Case 1 Output**

```text
New Roadrunner has a GPA of 0.00 with no classes completed.
Victoria has a GPA of 3.50 with the following letter grades: A, A, A, C.
```

### Example Case 2 (12 pt)

**Case 2 Input**

```text
Jorge
3
3
4
9
```

**Case 2 Output**

```text
New Roadrunner has a GPA of 0.00 with no classes completed.
Jorge has a GPA of 3.33 with the following letter grades: B, B, A.
```

## Task 2. Execute the Unit Test in the Terminal

After pip and pytest are installed, you can run the command to execute all the tests. These are the same tests that GitHub Classroom uses so do not modify the test_main.py file:

* Linux / Unix / Mac OS: `python3 -m pytest`
* Windows: `py -m pytest`
* Alternative 1: `pytest`
* Alternative 2: `python -m pytest`

Note, your install may differ so you may need to research how to execute your pytest command.
