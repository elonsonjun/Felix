from src.agents.reasoning_agent import get_report
from src.agents.finance_web_team import get_team_response

def handle_query(query: str, agent_type: str = "solo") -> str:
    if agent_type == "team":
        return get_team_response(query)
    return get_report(query)
