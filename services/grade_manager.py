import csv
import json
from pathlib import Path
from typing import Dict, Generator, List, Set

from models.course import Course
from models.grade import Grade
from models.student import Student
from utils.decorators import log_action
from utils.validators import validate_student_name


class GradeManager:
    """Main service class for managing students, courses, grades, and reports."""

    def __init__(self):
        # Dictionary is used for fast student lookup by ID: O(1) average time.
        self.students: Dict[int, Student] = {}
        # Set prevents duplicate course names.
        self.courses: Set[str] = set()
        self.grade_records: List[Grade] = []

    def add_student(self, student_id: int, name: str) -> Student:
        if not validate_student_name(name):
            raise ValueError("Student name contains invalid characters")

        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name)
        return self.students[student_id]

    def add_course(self, course_name: str) -> Course:
        course = Course(course_name)
        self.courses.add(course.name)
        return course

    def assign_grade(self, student_id: int, course_name: str, grade: float) -> None:
        if student_id not in self.students:
            raise KeyError(f"Student with ID {student_id} was not found")

        self.add_course(course_name)
        self.students[student_id].add_grade(course_name, grade)
        self.grade_records.append(Grade(student_id, course_name, grade))

    @log_action
    def load_from_csv(self, file_path: str) -> None:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"CSV file was not found: {file_path}")

        with path.open("r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            required_columns = {"student_id", "name", "course", "grade"}
            if not required_columns.issubset(reader.fieldnames or []):
                raise ValueError("CSV must contain student_id, name, course, grade columns")

            for row in reader:
                try:
                    student_id = int(row["student_id"])
                    name = row["name"]
                    course = row["course"]
                    grade = float(row["grade"])

                    self.add_student(student_id, name)
                    self.assign_grade(student_id, course, grade)
                except (ValueError, KeyError) as error:
                    print(f"Skipping invalid row {row}: {error}")

    def generate_student_reports(self) -> List[dict]:
        reports = []
        for student in self.students.values():
            reports.append({
                "student_id": student.user_id,
                "name": student.name,
                "average_grade": student.calculate_average(),
                "gpa": student.calculate_gpa(),
                "courses": student.grades,
            })
        return reports

    def get_top_students(self, limit: int = 3) -> List[Student]:
        # Lambda is used as an advanced Python feature for sorting by GPA.
        return sorted(
            self.students.values(),
            key=lambda student: student.calculate_gpa(),
            reverse=True,
        )[:limit]

    def iter_students_with_gpa(self) -> Generator[tuple, None, None]:
        # Generator saves memory because it produces results one by one.
        for student in self.students.values():
            yield student.name, student.calculate_gpa()

    @log_action
    def save_report_to_json(self, file_path: str) -> None:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as file:
            json.dump(self.generate_student_reports(), file, indent=4, ensure_ascii=False)
