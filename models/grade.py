class Grade:
    """Represents one grade record."""

    def __init__(self, student_id: int, course_name: str, value: float):
        if value < 0 or value > 100:
            raise ValueError("Grade must be between 0 and 100")
        self.student_id = student_id
        self.course_name = course_name.strip()
        self.value = float(value)

    def to_tuple(self) -> tuple:
        # Tuple is useful for fixed-size immutable records.
        return self.student_id, self.course_name, self.value
