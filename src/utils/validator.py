def validate_query(query: str) -> bool:
    return bool(query and len(query.strip()) > 0)
