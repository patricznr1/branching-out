USERS = [
    {"name": "Alice", "age": 30, "email": "alice@example.com"},
    {"name": "Bob", "age": 25, "email": "bob@example.com"},
    {"name": "Charlie", "age": 35, "email": "charlie@gmail.com"},
    {"name": "Diana", "age": 28, "email": "diana@gmail.com"},
]


def filter_by_name(users, name):
    return [user for user in users if user["name"] == name]


def filter_by_age(users, min_age):
    return [user for user in users if user["age"] >= min_age]


def filter_by_email(users, domain):
    """Filtere User-Liste nach Email-Domain."""
    return [user for user in users if user["email"].endswith('@' + domain)]


if __name__ == "__main__":
    print("By name:", filter_by_name(USERS, "Alice"))
    print("By age (>=30):", filter_by_age(USERS, 30))
    print("By email (gmail.com):", filter_by_email(USERS, "gmail.com"))
