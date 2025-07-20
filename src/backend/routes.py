from fastapi import APIRouter, Request
from src.agents.reasoning_agent import get_report
from src.agents.finance_web_team import get_team_response

router = APIRouter()

@router.post("/api/query")
async def query_agent(request: Request):
    data = await request.json()
    query = data.get("query", "")
    response = get_report(query)
    return {"response": response}

@router.post("/api/team")
async def query_team(request: Request):
    data = await request.json()
    query = data.get("query", "")
    response = get_team_response(query)
    return {"response": response}