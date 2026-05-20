from models.user import User


class Admin(User):
    """Admin class demonstrates inheritance and polymorphism."""

    def get_role(self) -> str:
        return "Admin"
