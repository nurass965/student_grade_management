from functools import wraps


def log_action(func):
    """Simple decorator used to show important system actions."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
