from pathlib import Path

from models.admin import Admin
from services.grade_manager import GradeManager


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "students.csv"
REPORT_PATH = BASE_DIR / "data" / "report.json"


def print_menu() -> None:
    print("\n===== Student Grade Management System =====")
    print("1. Load data from CSV")
    print("2. Show all students and GPA")
    print("3. Add student")
    print("4. Assign grade")
    print("5. Show top students")
    print("6. Save report to JSON")
    print("0. Exit")


def main() -> None:
    manager = GradeManager()
    admin = Admin(1, "System Admin")
    print(f"Logged in as: {admin}")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                manager.load_from_csv(str(CSV_PATH))
                print("CSV data loaded successfully.")

            elif choice == "2":
                if not manager.students:
                    print("No students found. Load CSV or add students first.")
                for name, gpa in manager.iter_students_with_gpa():
                    print(f"{name}: GPA {gpa}")

            elif choice == "3":
                student_id = int(input("Student ID: "))
                name = input("Student name: ")
                manager.add_student(student_id, name)
                print("Student added successfully.")

            elif choice == "4":
                student_id = int(input("Student ID: "))
                course = input("Course name: ")
                grade = float(input("Grade 0-100: "))
                manager.assign_grade(student_id, course, grade)
                print("Grade assigned successfully.")

            elif choice == "5":
                top_students = manager.get_top_students()
                print("Top students:")
                for index, student in enumerate(top_students, start=1):
                    print(f"{index}. {student.name} - GPA {student.calculate_gpa()}")

            elif choice == "6":
                manager.save_report_to_json(str(REPORT_PATH))
                print(f"Report saved to {REPORT_PATH}")

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Try again.")

        except Exception as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
