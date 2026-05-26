"""Branching Out - interactive search over a small user database.

The user picks a search category (name, age, email) and a query value.
The program returns every user record in USERS that matches.
"""
USERS = [
    {"name": "Alice", "age": 30, "email": "alice@example.com"},
    {"name": "Bob", "age": 25, "email": "bob@example.com"},
    {"name": "Charlie", "age": 35, "email": "charlie@gmail.com"},
    {"name": "Diana", "age": 28, "email": "diana@gmail.com"},
    {"name": "Eve", "age": 42, "email": "eve@example.com"},
    {"name": "Frank", "age": 19, "email": "frank@yahoo.com"},
]


def search_by_name(users, query):
    """Return users whose name contains ``query`` (case-insensitive)."""
    q = query.lower()
    return [u for u in users if q in u["name"].lower()]


def search_by_age(users, query):
    """Return users matching an age query.

    The query may be an exact age (``30``), a minimum (``>=30``), or a
    maximum (``<=40``).
    """
    query = query.strip()
    if query.startswith(">="):
        bound = int(query[2:].strip())
        return [u for u in users if u["age"] >= bound]
    if query.startswith("<="):
        bound = int(query[2:].strip())
        return [u for u in users if u["age"] <= bound]
    if query.startswith(">"):
        bound = int(query[1:].strip())
        return [u for u in users if u["age"] > bound]
    if query.startswith("<"):
        bound = int(query[1:].strip())
        return [u for u in users if u["age"] < bound]
    target = int(query)
    return [u for u in users if u["age"] == target]


def search_by_email(users, query):
    """Return users whose email contains ``query`` (case-insensitive).

    A bare domain like ``gmail.com`` matches everyone on that domain.
    """
    q = query.lower().lstrip("@")
    return [u for u in users if q in u["email"].lower()]


SEARCH_HANDLERS = {
    "name": search_by_name,
    "age": search_by_age,
    "email": search_by_email,
}


def print_matches(matches):
    """Print a list of user dicts in a readable form, or a 'no match' note."""
    if not matches:
        print("  no matches.")
        return
    for user in matches:
        print(f"  {user['name']:10}  age={user['age']:3}  {user['email']}")


def main():
    """Run the interactive search loop until the user types 'quit'."""
    print("Branching Out - user search")
    print("Type 'quit' to exit.")
    while True:
        category = input(
            "\nSearch by which category? (name / age / email): "
        ).strip().lower()
        if category in ("quit", "exit", "q"):
            print("Goodbye.")
            break
        if category not in SEARCH_HANDLERS:
            print(f"  unknown category '{category}'. Try name, age or email.")
            continue
        query = input(f"Enter {category} to search for: ").strip()
        if not query:
            print("  empty query, skipping.")
            continue
        try:
            matches = SEARCH_HANDLERS[category](USERS, query)
        except ValueError as exc:
            print(f"  could not parse query: {exc}")
            continue
        print(f"\nResults for {category} ~= {query!r}:")
        print_matches(matches)


if __name__ == "__main__":
    main()
