class Course:
    """Course entity."""

    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Course name cannot be empty")
        self.name = name.strip()

    def __str__(self) -> str:
        return self.name
