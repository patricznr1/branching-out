USERS = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Diana", "age": 28},
]


def filter_by_name(users, name):
    """Filtere User-Liste nach Namen."""
    return [user for user in users if user["name"] == name]


def filter_by_age(users, min_age):
    """Filtere User-Liste nach Mindestalter."""
    return [user for user in users if user["age"] >= min_age]


if __name__ == "__main__":
    print("Filter by name (Alice):", filter_by_name(USERS, "Alice"))
    print("Filter by age (>=30):", filter_by_age(USERS, 30))
