# Student Grade Management System

## Project Description
This is a Python console application for managing students, courses, and grades.
The system can add students and courses, assign grades, calculate GPA, show top-performing students, and generate JSON reports.

## Case
Case 2: Student Grade Management System

## Features
- Add students
- Add courses
- Assign grades
- Read data from CSV
- Calculate average grade and GPA
- Show top-performing students
- Save reports to JSON
- Basic unit testing with `unittest`

## Project Structure
```text
student_grade_management/
│
├── main.py
├── README.md
│
├── data/
│   ├── students.csv
│   └── report.json
│
├── models/
│   ├── user.py
│   ├── admin.py
│   ├── student.py
│   ├── course.py
│   └── grade.py
│
├── services/
│   └── grade_manager.py
│
├── utils/
│   ├── decorators.py
│   └── validators.py
│
└── tests/
    └── test_grade_manager.py
```

## How to Run
Open the project folder in PyCharm or VS Code.

Run the main program:
```bash
python main.py
```

Run tests:
```bash
python -m unittest discover tests
```

## Input CSV Format
```csv
student_id,name,course,grade
1,John,Math,85
2,Alice,Physics,90
```

## Output
The program shows:
- GPA per student
- Top-performing students
- JSON report in `data/report.json`

## Required Concepts Used

### Functions
The project uses functions with arguments and return values, for example:
- `add_student(student_id, name)`
- `assign_grade(student_id, course_name, grade)`
- `get_top_students(limit)`

### OOP
The project includes several classes:
- `User`
- `Admin`
- `Student`
- `Course`
- `Grade`
- `GradeManager`

Inheritance and polymorphism are shown through `User`, `Admin`, and `Student`.

### Encapsulation
Student data is stored in protected attributes such as `_user_id`, `_name`, and `_grades`.
Access is provided through properties.

### Collections and Data Structures
- List: stores grade records
- Dictionary: stores students by ID for fast lookup
- Set: stores unique course names
- Tuple: represents fixed grade record data

A dictionary is used for students because searching by ID is faster than looping through a list.

### File Handling
- Reads student data from CSV
- Writes reports to JSON

### Error Handling
The project handles:
- invalid grades
- invalid names
- missing CSV files
- unknown student IDs

### Advanced Python Features
- Generator: `iter_students_with_gpa()`
- Decorator: `log_action`
- Lambda: sorting top students
- Regular expressions: validating names

## Team Members
1. Student 1 - Models and OOP classes
2. Student 2 - GradeManager service and algorithms
3. Student 3 - File handling and reports
4. Student 4 - Testing and README

## Algorithmic Efficiency
The system uses a dictionary for student lookup by ID.
This avoids scanning a list every time a grade is assigned.

- List search: O(n)
- Dictionary lookup: O(1) average time

This makes the system more efficient for larger datasets.
