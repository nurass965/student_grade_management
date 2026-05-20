import unittest

from services.grade_manager import GradeManager


class TestGradeManager(unittest.TestCase):
    def setUp(self):
        self.manager = GradeManager()
        self.manager.add_student(1, "John")
        self.manager.assign_grade(1, "Math", 85)
        self.manager.assign_grade(1, "Physics", 90)

    def test_calculate_gpa(self):
        student = self.manager.students[1]
        self.assertEqual(student.calculate_gpa(), 3.5)

    def test_top_students(self):
        self.manager.add_student(2, "Alice")
        self.manager.assign_grade(2, "Math", 100)
        top = self.manager.get_top_students(limit=1)
        self.assertEqual(top[0].name, "Alice")

    def test_invalid_grade(self):
        with self.assertRaises(ValueError):
            self.manager.assign_grade(1, "Math", 120)

    def test_unknown_student(self):
        with self.assertRaises(KeyError):
            self.manager.assign_grade(99, "Math", 80)

    def test_report_generation(self):
        report = self.manager.generate_student_reports()
        self.assertEqual(len(report), 1)
        self.assertEqual(report[0]["name"], "John")


if __name__ == "__main__":
    unittest.main()
