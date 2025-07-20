from src.utils.validator import validate_query

def test_validation():
    assert validate_query("Hello") == True
    assert validate_query("   ") == False
