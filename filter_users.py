USERS = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Diana", "age": 28},
]


def filter_by_name(users, name):
    """Filtere User-Liste nach Namen."""
    return [user for user in users if user["name"] == name]


if __name__ == "__main__":
    result = filter_by_name(USERS, "Alice")
    print(result)
