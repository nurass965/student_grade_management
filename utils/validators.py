import re


def validate_student_name(name: str) -> bool:
    """Regular expression checks that name contains letters and spaces only."""
    return bool(re.fullmatch(r"[A-Za-zА-Яа-яЁёӘәІіҢңҒғҮүҰұҚқӨөҺһ ]+", name.strip()))


def validate_grade(value: float) -> bool:
    return 0 <= value <= 100
