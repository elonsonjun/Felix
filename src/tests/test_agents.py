from src.agents.reasoning_agent import get_report

def test_reasoning():
    response = get_report("Test query")
    assert response is not None
