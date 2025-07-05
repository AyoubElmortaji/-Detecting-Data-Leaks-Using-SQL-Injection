def is_safe_sql(query: str) -> bool:
    blocked = ['--', ';', 'DROP', ' OR ', ' AND ', '#', 'INSERT', 'DELETE', 'UPDATE']
    return not any(b in query.upper() for b in blocked)

def is_authorized(user, code: str) -> bool:
    return user and user[4] == 'admin' and user[5] == code
