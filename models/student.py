from models.user import User


class Student(User):
    """Student class that stores courses and grades."""

    def __init__(self, student_id: int, name: str):
        super().__init__(student_id, name)
        # Dictionary gives fast lookup by course name: O(1) average time.
        self._grades = {}

    def get_role(self) -> str:
        return "Student"

    def add_grade(self, course_name: str, grade: float) -> None:
        if not course_name.strip():
            raise ValueError("Course name cannot be empty")
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")

        self._grades[course_name.strip()] = float(grade)

    @property
    def grades(self) -> dict:
        return self._grades.copy()

    def calculate_gpa(self) -> float:
        if not self._grades:
            return 0.0
        average = sum(self._grades.values()) / len(self._grades)
        return round(average / 25, 2)  # 100-point scale converted to 4.0 GPA scale

    def calculate_average(self) -> float:
        if not self._grades:
            return 0.0
        return round(sum(self._grades.values()) / len(self._grades), 2)
