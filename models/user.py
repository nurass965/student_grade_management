class User:
    """Base class for all system users."""

    def __init__(self, user_id: int, name: str):
        if user_id <= 0:
            raise ValueError("User ID must be positive")
        if not name.strip():
            raise ValueError("Name cannot be empty")

        self._user_id = user_id
        self._name = name.strip()

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    def get_role(self) -> str:
        return "User"

    def __str__(self) -> str:
        return f"{self.get_role()} #{self.user_id}: {self.name}"
